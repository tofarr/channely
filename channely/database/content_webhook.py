from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseEntity
from channely.database.content_event_type import ContentEventType

if TYPE_CHECKING:
    from channely.database.content_webhook_header import ContentWebhookHeaderEntity
    from channely.database.channel import ChannelEntity
    
    
class ContentWebhookEntity(BaseEntity):
    __tablename__ = "content_webhooks"

    channel_id: Mapped[UUID | None] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("channels.id")
    )
    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    timeout: Mapped[int] = mapped_column(Integer, default=15)
    num_retries: Mapped[int] = mapped_column(Integer, default=3)
    retry_delay: Mapped[int] = mapped_column(Integer, default=5)
    event_type: Mapped[ContentEventType | None] = mapped_column()

    # Relationships
    channel: Mapped[ChannelEntity | None] = relationship(
        "ChannelEntity", foreign_keys=[channel_id], back_populates="content"
    )
    headers: Mapped[list[ContentWebhookHeaderEntity]] = relationship(
        "ContentWebhookHeaderEntity", back_populates="webhook"
    )
