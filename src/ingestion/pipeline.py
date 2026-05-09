from pathlib import Path
from typing import Any
from uuid import NAMESPACE_URL, uuid5

from src.ingestion.data_loader import DataLoader
from src.ingestion.embedder import OllamaEmbedder
from src.models.ingestion import DocumentChunk, EmbeddedDocumentChunk
from src.vector_database.vector_db import VectorDB
from src.ingestion.generator import OllamaGenerator

class IngestionPipeline:
    def __init__(
        self,
        loader: DataLoader | None = None,
        embedder: OllamaEmbedder | None = None,
        generator: OllamaGenerator | None = None,
        vector_db: VectorDB | None = None,
    ) -> None:
        self.loader = loader or DataLoader()
        self.embedder = embedder or OllamaEmbedder()
        self.generator = generator or OllamaGenerator()
        self.vector_db = vector_db or VectorDB()

    def load_and_chunk_pdf(
        self,
        file_path: str | Path,
        source_id: str | None = None,
    ) -> dict[str, Any]:
        path = Path(file_path)
        resolved_source_id = source_id or str(path)

        chunks = self.loader.load_pdf_chunks(path)

        valid_chunks = [
            chunk
            for chunk in chunks
            if chunk.text.strip()
        ]

        return {
            "source_id": resolved_source_id,
            "file_path": str(path),
            "chunks": [
                chunk.model_dump()
                for chunk in valid_chunks
            ],
        }

    def embed_chunks(
        self,
        chunks_and_source: dict[str, Any],
    ) -> dict[str, Any]:
        source_id = chunks_and_source["source_id"]
        file_path = chunks_and_source["file_path"]

        document_chunks = [
            DocumentChunk.model_validate(chunk)
            for chunk in chunks_and_source["chunks"]
        ]

        texts = [
            chunk.text
            for chunk in document_chunks
        ]

        embeddings = self.embedder.embed_texts(texts)

        if len(document_chunks) != len(embeddings):
            raise ValueError(
                "Number of chunks and embeddings does not match"
            )

        embedded_chunks = [
            EmbeddedDocumentChunk(
                id=chunk.id,
                text=chunk.text,
                metadata=chunk.metadata,
                embedding=embedding,
            )
            for chunk, embedding in zip(document_chunks, embeddings)
        ]

        return {
            "source_id": source_id,
            "file_path": file_path,
            "chunks": [
                chunk.model_dump()
                for chunk in embedded_chunks
            ],
        }

    def upsert_chunks(
        self,
        embedded_chunks_and_source: dict[str, Any],
    ) -> dict[str, Any]:
        source_id = embedded_chunks_and_source["source_id"]
        file_path = embedded_chunks_and_source["file_path"]

        chunks = [
            EmbeddedDocumentChunk.model_validate(chunk)
            for chunk in embedded_chunks_and_source["chunks"]
        ]

        vector_ids = [
            str(uuid5(NAMESPACE_URL, f"{source_id}:{chunk.id}"))
            for chunk in chunks
        ]

        vectors = [
            chunk.embedding
            for chunk in chunks
        ]

        payloads = [
            {
                "source_id": source_id,
                "chunk_id": chunk.id,
                "text": chunk.text,
                "source": chunk.metadata.source,
                "file_path": file_path,
                "metadata": chunk.metadata.model_dump(),
            }
            for chunk in chunks
        ]

        inserted = self.vector_db.add_vectors(
            vector_ids=vector_ids,
            vectors=vectors,
            payloads=payloads,
        )

        return {
            "source_id": source_id,
            "file_path": file_path,
            "inserted": inserted,
            "collection_name": self.vector_db.collection_name,
        }

    def ingest_pdf(
        self,
        file_path: str | Path,
        source_id: str | None = None,
    ) -> dict[str, Any]:
        chunks_and_source = self.load_and_chunk_pdf(
            file_path=file_path,
            source_id=source_id,
        )

        embedded_chunks_and_source = self.embed_chunks(
            chunks_and_source
        )

        upsert_result = self.upsert_chunks(
            embedded_chunks_and_source
        )

        return {
            "source_id": chunks_and_source["source_id"],
            "file_path": chunks_and_source["file_path"],
            "chunks": len(chunks_and_source["chunks"]),
            "embedded_chunks": len(embedded_chunks_and_source["chunks"]),
            "upsert": upsert_result,
        }
    
    def query_chunks(
        self,
        query: str,
        top_k: int = 5,
    ) -> dict[str, Any]:
        if not query or not query.strip():
            raise ValueError("Query cannot be empty")

        query_embedding = self.embedder.embed_text(query.strip())

        search_result = self.vector_db.search_vector(
            query_vector=query_embedding,
            results_num=top_k,
        )

        return {
            "query": query.strip(),
            "top_k": top_k,
            "contexts": search_result["contexts"],
            "sources": search_result["sources"],
            "matches": search_result["matches"],
        }
    
    def answer_query(
        self,
        query: str,
        retrieval_result: dict[str, Any],
    ) -> dict[str, Any]:
        contexts = retrieval_result.get("contexts", [])
        sources = retrieval_result.get("sources", [])

        if not isinstance(contexts, list):
            raise ValueError("retrieval_result['contexts'] must be a list")

        answer = self.generator.generate_answer(
            question=query,
            contexts=contexts,
        )

        return {
            "answer": answer,
            "sources": sources,
            "num_contexts": len(contexts),
        }