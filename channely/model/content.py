from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from channely.database.content_status import ContentStatus


@dataclass
class Content:
    """
    A piece of content within a channel created by a single user
    A null value for creator implies the creator is unknown or the content was created automatically.
    """

    channel_id: UUID
    text: str | None
    markdown: str
    id: UUID = field(default_factory=uuid4)
    status: ContentStatus = ContentStatus.ACTIVE
    creator: UUID | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
