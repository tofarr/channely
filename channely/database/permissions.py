from uuid import UUID

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseEntity, BaseEntityWithoutTimestamps
from channely.database.enums import ChannelPermissionType, ContentPermissionType, SystemPermissionType


class ChannelPermissionEntity(BaseEntityWithoutTimestamps):
    __tablename__ = "channel_permissions"
    __table_args__ = (
        UniqueConstraint('channel_id', 'type', 'creator_id', name='unique_channel_permission'),
    )
    
    channel_id: Mapped[UUID] = mapped_column(PostgresUUID(as_uuid=True), ForeignKey("channels.id"), nullable=False)
    type: Mapped[ChannelPermissionType] = mapped_column(nullable=False)
    creator_id: Mapped[UUID | None] = mapped_column(PostgresUUID(as_uuid=True), ForeignKey("users.id"))
    
    # Relationships
    channel: Mapped["ChannelEntity"] = relationship("ChannelEntity", back_populates="permissions")
    creator: Mapped["UserEntity"] = relationship("UserEntity", foreign_keys=[creator_id], back_populates="channel_permissions")


class ContentPermissionEntity(BaseEntityWithoutTimestamps):
    __tablename__ = "content_permissions"
    __table_args__ = (
        UniqueConstraint('article_id', 'type', 'user_id', name='unique_content_permission'),
    )
    
    article_id: Mapped[UUID] = mapped_column(PostgresUUID(as_uuid=True), ForeignKey("content.id"), nullable=False)
    type: Mapped[ContentPermissionType] = mapped_column(nullable=False)
    user_id: Mapped[UUID | None] = mapped_column(PostgresUUID(as_uuid=True), ForeignKey("users.id"))
    
    # Relationships
    content: Mapped["ContentEntity"] = relationship("ContentEntity", back_populates="permissions")
    user: Mapped["UserEntity"] = relationship("UserEntity", foreign_keys=[user_id], back_populates="content_permissions")


class SystemPermissionEntity(BaseEntityWithoutTimestamps):
    __tablename__ = "system_permissions"
    __table_args__ = (
        UniqueConstraint('type', 'user_id', name='unique_system_permission'),
    )
    
    type: Mapped[SystemPermissionType] = mapped_column(nullable=False)
    user_id: Mapped[UUID | None] = mapped_column(PostgresUUID(as_uuid=True), ForeignKey("users.id"))
    
    # Relationships
    user: Mapped["UserEntity"] = relationship("UserEntity", back_populates="system_permissions")