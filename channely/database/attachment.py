from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseImmutableEntity, BaseImmutableEntity

if TYPE_CHECKING:
    from channely.database.content import ContentEntity


class AttachmentEntity(BaseImmutableEntity):
    __tablename__ = "attachments"

    content_id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("content.id"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(100), nullable=False)
    size_in_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)

    # Relationships
    content: Mapped[ContentEntity] = relationship(
        "ContentEntity", back_populates="attachments"
    )
