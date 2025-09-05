from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from channely.database.user_status import UserStatus


@dataclass
class User:
    username: str
    id: UUID = field(default_factory=uuid4)
    status: UserStatus = UserStatus.ACTIVE
    display_name: str | None = None
    locale: str | None = None
    theme: str | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
