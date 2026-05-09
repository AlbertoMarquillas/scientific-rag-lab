from typing import Any

from ollama import Client

from src.core.config import settings


class OllamaGenerator:
    def __init__(
        self,
        base_url: str = settings.ollama_base_url,
        model: str = settings.llm_model,
    ) -> None:
        self.client = Client(host=base_url)
        self.model = model

    def generate_answer(
        self,
        question: str,
        contexts: list[str],
    ) -> str:
        if not question or not question.strip():
            raise ValueError("Question cannot be empty")

        if not contexts:
            return (
                "I could not find enough relevant context to answer "
                "the question."
            )

        context_block = "\n\n".join(
            f"[Context {index + 1}]\n{context}"
            for index, context in enumerate(contexts)
        )

        user_prompt = (
            "Use only the following context to answer the question.\n\n"
            f"{context_block}\n\n"
            f"Question: {question}\n\n"
            "Answer in a detailed but clear way. Use several paragraphs if needed. "
            "If the context does not contain enough information, say that the answer"
            "cannot be confirmed from the provided context."
        )

        response: dict[str, Any] = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a scientific RAG assistant. "
                        "You answer only using the provided context. "
                        "Do not invent information."
                    ),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            options={
                "temperature": 0.2,
                "num_predict": 2048,
            }
        )

        message = response.get("message", {})
        answer = message.get("content")

        if not isinstance(answer, str) or not answer.strip():
            raise ValueError("Ollama response does not contain a valid answer")

        return answer.strip()