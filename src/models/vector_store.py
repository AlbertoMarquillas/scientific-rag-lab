from typing import Any

from pydantic import BaseModel, Field


class UpsertResult(BaseModel):
    inserted: int = Field(ge=0)
    collection_name: str


class VectorSearchMatch(BaseModel):
    id: str | int
    score: float
    text: str | None = None
    source: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)


class SearchResult(BaseModel):
    contexts: list[str] = Field(default_factory=list)
    sources: list[str] = Field(default_factory=list)
    matches: list[VectorSearchMatch] = Field(default_factory=list)