from abc import ABC, abstractmethod
from typing import List
from langchain_text_splitters import (
    MarkdownTextSplitter,
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
    TokenTextSplitter,
)




class BaseSplitter(ABC):
    """Abstract base class for text splitters."""

    @abstractmethod
    def split_text(
        self,
        document_id: str,
        project_id: str,
        text: str,
        page_number: int | None = None,
        section_hint: str | None = None,
    ) -> List[str]:
        pass


class MarkdownTextSplitter(BaseSplitter):
    """Concrete implementation of BaseTextSplitter for Markdown text."""

    def split_text(
        self,
        document_id: str,
        project_id: str,
        text: str,
        page_number: int | None = None,
        section_hint: str | None = None,
    ) -> List[str]:
        # Simple implementation: split by double newlines (paragraphs)
        return [
            paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()
        ]
