from abc import ABC, abstractmethod
from requests import Session


class AdBoardSearch(ABC):
    """
    Abstract ad board search
    """
    query = ''
    base_url = ''

    session = Session()

    @abstractmethod
    def check_new(self):
        """Check if a new ad was posted"""

    @abstractmethod
    def _extract_ads(self, html):
        """Get the ads payload (url and title) from raw html search results page"""
