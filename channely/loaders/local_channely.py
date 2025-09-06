from __future__ import annotations

from typing import TYPE_CHECKING, Iterator
from uuid import UUID

from channely.loaders.base import ContentLoader

if TYPE_CHECKING:
    from channely.database.content import ContentEntity


class LocalChannelyLoader(ContentLoader):
    """Content loader for local Channely sources.
    
    This loader fetches content from a local Channely user.
    """
    
    user_id: UUID

    def load_new_content(self) -> Iterator[ContentEntity]:
        """Load new content from the local Channely user.
        
        Returns:
            Iterator over ContentEntity objects representing new content.
        """
        # Implementation would query the local database for new content
        # from the specified user
        raise NotImplementedError("Local Channely content loading not yet implemented")