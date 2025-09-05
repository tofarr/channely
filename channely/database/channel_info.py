from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from channely.database.base import BaseMutableEntity

if TYPE_CHECKING:
    from channely.database.channel import ChannelEntity


class ChannelInfoEntity(BaseMutableEntity):
    __tablename__ = "channel_info"

    channel_id: Mapped[UUID | None] = mapped_column(
        PostgresUUID(as_uuid=True), ForeignKey("channel.id")
    )
    
    locale: Mapped[str]
    title: Mapped[str]
    description: Mapped[str | None]

    # Relationships
    channel: Mapped[ChannelEntity] = relationship(
        "ChannelEntity", foreign_keys=[channel_id], back_populates="info"
    )
