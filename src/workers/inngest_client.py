import logging

import inngest

from src.core.config import settings


def create_inngest_client() -> inngest.Inngest:
    return inngest.Inngest(
        app_id=settings.inngest_app_id,
        is_production=settings.inngest_is_production,
        logger=logging.getLogger(settings.inngest_logger),
        serializer=inngest.PydanticSerializer(),
    )


inngest_client = create_inngest_client()