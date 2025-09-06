from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Iterator

from pydantic import BaseModel

if TYPE_CHECKING:
    from channely.database.content import ContentEntity


class ContentLoader(BaseModel, ABC):
    """Abstract base class for content loaders.
    
    Content loaders are responsible for fetching new content from various sources
    and converting them into ContentEntity objects.
    """

    @abstractmethod
    def load_new_content(self) -> Iterator[ContentEntity]:
        """Load new content from the source.
        
        Returns:
            Iterator over ContentEntity objects representing new content.
        """
        pass