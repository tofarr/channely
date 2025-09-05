from dataclasses import dataclass, field
from uuid import UUID, uuid4

from channely.database.content_event_type import ContentEventType


@dataclass
class ContentWebhook:
    url: str
    id: UUID = field(default_factory=uuid4)
    num_retries: int = 3
    retry_delay: int = 5
    event_type: ContentEventType | None = None
