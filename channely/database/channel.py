from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseEntity
from channely.database.channel_status import ChannelStatus


class ChannelEntity(BaseEntity):
    __tablename__ = "channels"

    status: Mapped[ChannelStatus] = mapped_column(default=ChannelStatus.ACTIVE)
    parent_content_id: Mapped[UUID | None] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("content.id")
    )
    theme: Mapped[str | None] = mapped_column(String(50))
    creator_id: Mapped[UUID | None] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("users.id")
    )

    # Relationships
    creator: Mapped["UserEntity"] = relationship(
        "UserEntity", foreign_keys=[creator_id], back_populates="created_channels"
    )
    parent_content: Mapped["ContentEntity"] = relationship(
        "ContentEntity", foreign_keys=[parent_content_id], back_populates="subchannels"
    )
    content: Mapped[list["ContentEntity"]] = relationship(
        "ContentEntity",
        foreign_keys="ContentEntity.channel_id",
        back_populates="channel",
    )
    permissions: Mapped[list["ChannelPermissionEntity"]] = relationship(
        "ChannelPermissionEntity", back_populates="channel"
    )
