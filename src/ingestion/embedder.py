from ollama import Client

from src.core.config import settings


class OllamaEmbedder:
    def __init__(
        self,
        base_url: str = settings.ollama_base_url,
        model: str = settings.embed_model,
    ) -> None:
        self.client = Client(host=base_url)
        self.model = model

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        embeddings = self.embed_texts([text])

        if not embeddings:
            raise ValueError(
                "Failed to generate embedding"
            )

        return embeddings[0]

    def embed_texts(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        valid_texts = [
            text.strip()
            for text in texts
            if isinstance(text, str)
            and text.strip()
        ]

        if not valid_texts:
            return []

        try:
            response = self.client.embed(
                model=self.model,
                input=valid_texts,
            )

        except Exception as exc:
            raise RuntimeError(
                f"Failed to generate embeddings: {exc}"
            ) from exc

        embeddings = response.get("embeddings")

        if embeddings is None:
            raise ValueError(
                "Ollama response does not contain embeddings"
            )

        return embeddings