from pathlib import Path

from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.file import PDFReader

from src.core.config import settings
from src.models.ingestion import ChunkMetadata, DocumentChunk


class DataLoader:
    def __init__(
        self,
        chunk_size: int = settings.chunk_size,
        chunk_overlap: int = settings.chunk_overlap,
    ) -> None:
        self.pdf_reader = PDFReader()
        self.splitter = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def load_pdf_chunks(
        self,
        file_path: str | Path,
    ) -> list[DocumentChunk]:
        path = Path(file_path)

        self._validate_pdf_path(path)

        documents = self.pdf_reader.load_data(file=path)

        chunks: list[DocumentChunk] = []

        for page_index, document in enumerate(documents):
            text = getattr(document, "text", None)

            if not text or not text.strip():
                continue

            text_chunks = self.splitter.split_text(text)

            for chunk_index, chunk_text in enumerate(text_chunks):
                if not chunk_text.strip():
                    continue

                chunks.append(
                    DocumentChunk(
                        id=f"{path.stem}-p{page_index + 1}-c{chunk_index}",
                        text=chunk_text.strip(),
                        metadata=ChunkMetadata(
                            source=str(path),
                            file_name=path.name,
                            file_stem=path.stem,
                            file_type="pdf",
                            page=page_index + 1,
                            chunk_index=chunk_index,
                        ),
                    )
                )

        return chunks

    @staticmethod
    def _validate_pdf_path(path: Path) -> None:
        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {path}"
            )

        if not path.is_file():
            raise ValueError(
                f"Expected a file, got directory: {path}"
            )

        if path.suffix.lower() != ".pdf":
            raise ValueError(
                f"Expected a PDF file, got: {path.suffix}"
            )