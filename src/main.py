from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import inngest
import inngest.fast_api

from src.workers.inngest_client import inngest_client
from src.workers.inngest_functions import inngest_functions
from pydantic import BaseModel

from src.ingestion.pipeline import IngestionPipeline

BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = BASE_DIR / "documents_base"
FRONTEND_DIR = BASE_DIR / "src" / "frontend"

DOCUMENTS_DIR.mkdir(exist_ok=True)


def create_app() -> FastAPI:
    app = FastAPI(
        title="Scientific RAG Lab API",
        version="0.1.0",
    )

    app.mount(
        "/static",
        StaticFiles(directory=FRONTEND_DIR),
        name="static",
    )


    @app.get("/", response_class=HTMLResponse)
    async def frontend() -> str:
        return (FRONTEND_DIR / "index.html").read_text(encoding="utf-8")

    @app.post("/api/documents/upload")
    async def upload_document(file: UploadFile = File(...)) -> dict:
        if not file.filename:
            raise HTTPException(status_code=400, detail="Missing filename")

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are supported")

        original_filename = Path(file.filename).name
        source_id = f"{Path(original_filename).stem}-{uuid4().hex[:8]}"
        file_path = DOCUMENTS_DIR / f"{source_id}.pdf"

        content = await file.read()
        file_path.write_bytes(content)

        event_ids = await inngest_client.send(
            inngest.Event(
                name="rag/process-document",
                data={
                    "file_path": str(file_path),
                    "source_id": source_id,
                },
            )
        )

        return {
            "message": "PDF uploaded and ingestion event sent",
            "file_name": original_filename,
            "file_path": str(file_path),
            "source_id": source_id,
            "event_ids": event_ids,
        }


    class ChatQueryRequest(BaseModel):
        query: str
        top_k: int = 5


    @app.post("/api/chat/query")
    async def query_document(request: ChatQueryRequest) -> dict:
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        pipeline = IngestionPipeline()

        retrieval_result = pipeline.query_chunks(
            query=request.query,
            top_k=request.top_k,
        )

        answer_result = pipeline.answer_query(
            query=request.query,
            retrieval_result=retrieval_result,
        )

        return {
            "query": request.query,
            "answer": answer_result["answer"],
            "sources": answer_result["sources"],
            "num_contexts": answer_result["num_contexts"],
            "retrieval": retrieval_result,
        }

    inngest.fast_api.serve(
        app,
        inngest_client,
        inngest_functions,
        serve_path="/api/inngest",
    )

    return app


app = create_app()