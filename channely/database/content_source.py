from __future__ import annotations

import json
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from channely.database.base import BaseMutableEntity

if TYPE_CHECKING:
    from channely.loaders.base import ContentLoader


class ContentSourceEntity(BaseMutableEntity):
    __tablename__ = "content_sources"

    # Type contains the class name of the ContentLoader implementation
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    
    # Data contains the JSON-serialized ContentLoader instance
    data: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Scheduling fields
    next_update_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    update_frequency_seconds: Mapped[int | None] = mapped_column(Integer)

    def get_loader(self) -> ContentLoader:
        """Deserialize and return the ContentLoader instance."""
        # This would need to be implemented with proper class registry
        # For now, this is a placeholder showing the intended interface
        loader_data = json.loads(self.data)
        # Implementation would dynamically import and instantiate the loader class
        # based on self.type and loader_data
        raise NotImplementedError("Loader deserialization not yet implemented")

    def set_loader(self, loader: ContentLoader) -> None:
        """Serialize and store the ContentLoader instance."""
        self.type = loader.__class__.__name__
        self.data = loader.model_dump_json()