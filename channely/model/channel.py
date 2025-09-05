from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from channely.database.channel_status import ChannelStatus


@dataclass
class Channel:
    """
    A channel within the system which contains pieces of content. If a channel has a parent content, then it is
    a subchannel from a piece of content on another channel.
    The theme is frontend specific, but used to determine UI settings (such as color) associated with a channel.
    A null value for creator implies the creator is unknown or the channel was created automatically.
    """

    id: UUID = field(default_factory=uuid4)
    status: ChannelStatus = ChannelStatus.ACTIVE
    parent_content_id: UUID | None = None
    theme: str | None = None
    creator_id: UUID | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
