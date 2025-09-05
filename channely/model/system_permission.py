from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from channely.enums.system_permission_type import SystemPermissionType


@dataclass
class SystemPermission:
    type: SystemPermissionType
    user_id: UUID | None
    id: UUID
    created_at: datetime = field(default_factory=datetime.utcnow)
