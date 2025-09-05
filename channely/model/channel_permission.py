from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from channely.database.channel_permission_type import ChannelPermissionType


@dataclass
class ChannelPermission:
    """
    Permission related to channels. the combo of user, channel and type should be unique.
    A null value for user implies the permission applies to everybody.
    """

    channel_id: UUID
    type: ChannelPermissionType
    id: UUID = field(default_factory=uuid4)
    creator_id: UUID | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
