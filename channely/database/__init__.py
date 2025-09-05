"""
SQLAlchemy database entities for the Channely application.

This package contains SQLAlchemy entity definitions that correspond to the
dataclasses defined in the channely.model package.
"""

from channely.database.attachment import AttachmentEntity
from channely.database.base import Base, BaseEntity, BaseEntityWithoutTimestamps
from channely.database.channel import ChannelEntity
from channely.database.content import ContentEntity
from channely.database.content_webhook import (
    ContentWebhookEntity,
    ContentWebhookHeaderEntity,
)
from channely.database.channel_permission_type import ChannelPermissionType
from channely.database.channel_status import ChannelStatus
from channely.database.content_event_type import ContentEventType
from channely.database.content_permission_type import ContentPermissionType
from channely.database.content_status import ContentStatus
from channely.database.system_permission_type import SystemPermissionType
from channely.database.user_status import UserStatus
from channely.database.permissions import (
    ChannelPermissionEntity,
    ContentPermissionEntity,
    SystemPermissionEntity,
)
from channely.database.user import UserEntity

__all__ = [
    # Base classes
    "Base",
    "BaseEntity",
    "BaseEntityWithoutTimestamps",
    # Enums
    "ChannelPermissionType",
    "ChannelStatus",
    "ContentEventType",
    "ContentPermissionType",
    "ContentStatus",
    "SystemPermissionType",
    "UserStatus",
    # Main entities
    "AttachmentEntity",
    "ChannelEntity",
    "ContentEntity",
    "ContentWebhookEntity",
    "ContentWebhookHeaderEntity",
    "UserEntity",
    # Permission entities
    "ChannelPermissionEntity",
    "ContentPermissionEntity",
    "SystemPermissionEntity",
]
