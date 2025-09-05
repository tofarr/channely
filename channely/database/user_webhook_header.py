from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseMutableEntity

if TYPE_CHECKING:
    from channely.database.user_webhook import UserWebhookEntity
    

class UserWebhookHeaderEntity(BaseMutableEntity):
    __tablename__ = "user_webhook_headers"

    user_webhook_id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("user_webhooks.id"), nullable=False
    )
    key: Mapped[str] = mapped_column(String(255), nullable=False)
    value: Mapped[str] = mapped_column(String(1024), nullable=False)

    # Relationships
    webhook: Mapped[UserWebhookEntity] = relationship(
        "UserWebhookEntity", back_populates="headers"
    )
