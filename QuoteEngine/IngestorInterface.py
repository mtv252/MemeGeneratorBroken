"""Defines the abstract IngestorInterface, which will be inherited by Ingestor classes for specific filetypes."""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """The IngestorInterface creates a framework that will apply to any Ingestor class

    :var allowed_extensions: A list that each specific class will use to list their
    supported filetypes.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determines if a file type can be ingested by the specific Ingestor"""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
