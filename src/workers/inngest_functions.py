import datetime
import uuid

import inngest

from src.ingestion.pipeline import IngestionPipeline
from src.workers.inngest_client import inngest_client


@inngest_client.create_function(
    fn_id="rag-process-document",
    trigger=inngest.TriggerEvent(event="rag/process-document"),
)
async def rag_process_document(ctx: inngest.Context) -> dict:
    ctx.logger.info("Event received: %s", ctx.event)

    event_data = ctx.event.data or {}

    file_path = event_data.get("file_path")
    source_id = event_data.get("source_id") or file_path

    if not file_path:
        raise ValueError("Event must include 'file_path'")

    pipeline = IngestionPipeline()

    chunks_and_source = await ctx.step.run(
        "load-and-chunk-pdf",
        lambda: pipeline.load_and_chunk_pdf(
            file_path=file_path,
            source_id=source_id,
        ),
    )

    embedded_chunks_and_source = await ctx.step.run(
        "embed-chunks",
        lambda: pipeline.embed_chunks(chunks_and_source),
    )

    upsert_result = await ctx.step.run(
        "upsert-vectors",
        lambda: pipeline.upsert_chunks(embedded_chunks_and_source),
    )

    return {
        "message": "Document processed successfully",
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "request_id": str(uuid.uuid4()),
        "document": {
            "file_path": file_path,
            "source_id": source_id,
        },
        "chunks": len(chunks_and_source["chunks"]),
        "embedded_chunks": len(embedded_chunks_and_source["chunks"]),
        "upsert": upsert_result,
    }


@inngest_client.create_function(
    fn_id="rag-query-document",
    trigger=inngest.TriggerEvent(event="rag/query-document"),
)
async def rag_query_document(ctx: inngest.Context) -> dict:
    ctx.logger.info("Event received: %s", ctx.event)

    event_data = ctx.event.data or {}

    query = event_data.get("query")
    top_k = int(event_data.get("top_k", 5))

    if not query:
        raise ValueError("Event must include 'query'")

    pipeline = IngestionPipeline()

    retrieval_result = await ctx.step.run(
        "embed-and-search",
        lambda: pipeline.query_chunks(
            query=query,
            top_k=top_k,
        ),
    )

    answer_result = await ctx.step.run(
        "llm-answer",
        lambda: pipeline.answer_query(
            query=query,
            retrieval_result=retrieval_result,
        ),
    )

    return {
        "message": "Query processed successfully",
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "request_id": str(uuid.uuid4()),
        "query": query,
        "top_k": top_k,
        "answer": answer_result["answer"],
        "sources": answer_result["sources"],
        "num_contexts": answer_result["num_contexts"],
        "retrieval": retrieval_result,
    }

inngest_functions = [
    rag_process_document,
    rag_query_document,
]