
from uuid import UUID
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column

from channely.database.base import BaseImmutableEntity
from channely.database.content_event_type import ContentEventType
from channely.database.content_status import ContentStatus


class ContentEventEntity(BaseImmutableEntity):
    """ Events take a snapshot of the entity they are based upon and do not include foreign key references. """
    channel_id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True), nullable=False
    )
    content_id: Mapped[UUID] = mapped_column(
        PostgresUUID(as_uuid=True), nullable=False
    )
    type: Mapped[ContentEventType] = mapped_column()
    
    # Attributes copied from content
    text: Mapped[str | None] = mapped_column(Text)
    markdown: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[ContentStatus] = mapped_column(default=ContentStatus.ACTIVE)
    creator: Mapped[UUID | None] = mapped_column(
        PostgresUUID(as_uuid=True)
    )