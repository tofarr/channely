from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseEntity
from channely.database.user_event_type import UserEventType

if TYPE_CHECKING:
    from channely.database.user_webhook_header import UserWebhookHeaderEntity
    
    
class UserWebhookEntity(BaseEntity):
    __tablename__ = "user_webhooks"
    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    num_retries: Mapped[int] = mapped_column(Integer, default=3)
    retry_delay: Mapped[int] = mapped_column(Integer, default=5)
    event_type: Mapped[UserEventType | None] = mapped_column()

    # Relationships
    headers: Mapped[list[UserWebhookHeaderEntity]] = relationship(
        "UserWebhookHeaderEntity", back_populates="webhook"
    )
