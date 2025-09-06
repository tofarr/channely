from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Iterator, Optional

from channely.loaders.base import ContentLoader

if TYPE_CHECKING:
    from channely.database.content import ContentEntity


class RSSLoader(ContentLoader):
    """Content loader for RSS feeds.
    
    This loader fetches content from RSS feeds.
    """
    
    url: str
    headers: Optional[Dict[str, str]] = None

    def load_new_content(self) -> Iterator[ContentEntity]:
        """Load new content from the RSS feed.
        
        Returns:
            Iterator over ContentEntity objects representing new content.
        """
        # Implementation would fetch and parse the RSS feed
        # using the provided URL and optional headers
        raise NotImplementedError("RSS content loading not yet implemented")