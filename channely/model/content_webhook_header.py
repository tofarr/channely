from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class ContentWebhookHeader:
    content_webhook_id: UUID
    key: str
    value: str
    id: UUID = field(default_factory=uuid4)
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
