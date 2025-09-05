from __future__ import annotations

from uuid import UUID

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseEntity, BaseEntityWithoutTimestamps
from channely.database.content_event_type import ContentEventType


class ContentWebhookEntity(BaseEntityWithoutTimestamps):
    __tablename__ = "content_webhooks"

    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    num_retries: Mapped[int] = mapped_column(Integer, default=3)
    retry_delay: Mapped[int] = mapped_column(Integer, default=5)
    event_type: Mapped[ContentEventType | None] = mapped_column()

    # Relationships
    headers: Mapped[list[ContentWebhookHeaderEntity]] = relationship(
        "ContentWebhookHeaderEntity", back_populates="webhook"
    )


class ContentWebhookHeaderEntity(BaseEntity):
    __tablename__ = "content_webhook_headers"

    content_webhook_id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("content_webhooks.id"), nullable=False
    )
    key: Mapped[str] = mapped_column(String(255), nullable=False)
    value: Mapped[str] = mapped_column(String(1024), nullable=False)

    # Relationships
    webhook: Mapped[ContentWebhookEntity] = relationship(
        "ContentWebhookEntity", back_populates="headers"
    )
