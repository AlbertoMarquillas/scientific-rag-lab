from typing import Any

from pydantic import BaseModel, Field


class RetrievalResult(BaseModel):
    id: str | int
    text: str
    score: float = Field(ge=0.0)
    source: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class RetrievalResponse(BaseModel):
    query: str
    results: list[RetrievalResult] = Field(default_factory=list)
    num_results: int = Field(ge=0)