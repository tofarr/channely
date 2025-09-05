from dataclasses import field
from datetime import datetime
from uuid import UUID, uuid4

from channely.enums.content_permission_type import ContentPermissionType


class ContentPermission:
    """
    Permission related to articles. the combo of user, article and type should be unique.
    A null value for user implies the permission applies to everybody.
    """

    article_id: UUID
    type: ContentPermissionType
    id: UUID = field(default_factory=uuid4)
    user_id: UUID | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
