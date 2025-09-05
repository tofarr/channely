from uuid import UUID

from sqlalchemy import ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseEntity
from channely.database.content_status import ContentStatus


class ContentEntity(BaseEntity):
    __tablename__ = "content"

    channel_id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("channels.id"), nullable=False
    )
    text: Mapped[str | None] = mapped_column(Text)
    markdown: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[ContentStatus] = mapped_column(default=ContentStatus.ACTIVE)
    creator: Mapped[UUID | None] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("users.id")
    )

    # Relationships
    channel: Mapped["ChannelEntity"] = relationship(
        "ChannelEntity", foreign_keys=[channel_id], back_populates="content"
    )
    creator_user: Mapped["UserEntity"] = relationship(
        "UserEntity", foreign_keys=[creator], back_populates="created_content"
    )
    subchannels: Mapped[list["ChannelEntity"]] = relationship(
        "ChannelEntity",
        foreign_keys="ChannelEntity.parent_content_id",
        back_populates="parent_content",
    )
    attachments: Mapped[list["AttachmentEntity"]] = relationship(
        "AttachmentEntity", back_populates="content"
    )
    permissions: Mapped[list["ContentPermissionEntity"]] = relationship(
        "ContentPermissionEntity", back_populates="content"
    )
