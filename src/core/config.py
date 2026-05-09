from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================================
    # Ollama
    # =========================================

    ollama_base_url: str
    llm_model: str
    embed_model: str

    # =========================================
    # Qdrant
    # =========================================

    qdrant_host: str
    qdrant_port: int = Field(gt=0)

    qdrant_collection: str

    # =========================================
    # Chunking
    # =========================================

    chunk_size: int = Field(gt=0)
    chunk_overlap: int = Field(ge=0)

    # =========================================
    # Inngest
    # =========================================

    inngest_app_id: str
    inngest_is_production: bool
    inngest_logger: str

    # =========================================
    # Pydantic settings config
    # =========================================

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()