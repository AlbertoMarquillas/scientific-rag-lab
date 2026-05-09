from pydantic import BaseModel, Field
from typing import Any


class ChunkMetadata(BaseModel):
    source: str
    file_name: str
    file_stem: str
    file_type: str

    page: int = Field(ge=1)
    chunk_index: int = Field(ge=0)

    extra_metadata: dict[str, Any] = Field(default_factory=dict)


class DocumentChunk(BaseModel):
    id: str
    text: str = Field(min_length=1)

    metadata: ChunkMetadata


class EmbeddedDocumentChunk(BaseModel):
    id: str
    text: str = Field(min_length=1)

    embedding: list[float] = Field(min_length=1)

    metadata: ChunkMetadata