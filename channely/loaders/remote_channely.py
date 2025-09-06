from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

from channely.loaders.base import ContentLoader

if TYPE_CHECKING:
    from channely.database.content import ContentEntity


class RemoteChannelyLoader(ContentLoader):
    """Content loader for remote Channely sources.
    
    This loader fetches content from a remote Channely instance via API.
    """
    
    url: str
    api_key: str

    def load_new_content(self) -> Iterator[ContentEntity]:
        """Load new content from the remote Channely instance.
        
        Returns:
            Iterator over ContentEntity objects representing new content.
        """
        # Implementation would make HTTP requests to the remote Channely API
        # using the provided URL and API key
        raise NotImplementedError("Remote Channely content loading not yet implemented")