from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseEntity
from channely.database.user_status import UserStatus

if TYPE_CHECKING:
    from channely.database.channel import ChannelEntity
    from channely.database.content import ContentEntity
    from channely.database.permissions import (
        ChannelPermissionEntity,
        ContentPermissionEntity,
        SystemPermissionEntity,
    )


class UserEntity(BaseEntity):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    status: Mapped[UserStatus] = mapped_column(default=UserStatus.ACTIVE)
    display_name: Mapped[str | None] = mapped_column(String(255))
    locale: Mapped[str | None] = mapped_column(String(10))
    theme: Mapped[str | None] = mapped_column(String(50))

    # Relationships
    created_channels: Mapped[list[ChannelEntity]] = relationship(
        "ChannelEntity",
        foreign_keys="ChannelEntity.creator_id",
        back_populates="creator",
    )
    created_content: Mapped[list[ContentEntity]] = relationship(
        "ContentEntity",
        foreign_keys="ContentEntity.creator",
        back_populates="creator_user",
    )
    channel_permissions: Mapped[list[ChannelPermissionEntity]] = relationship(
        "ChannelPermissionEntity",
        foreign_keys="ChannelPermissionEntity.creator_id",
        back_populates="creator",
    )
    content_permissions: Mapped[list[ContentPermissionEntity]] = relationship(
        "ContentPermissionEntity",
        foreign_keys="ContentPermissionEntity.user_id",
        back_populates="user",
    )
    system_permissions: Mapped[list[SystemPermissionEntity]] = relationship(
        "SystemPermissionEntity", back_populates="user"
    )
