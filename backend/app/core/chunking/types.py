# Questo file lo uso per definire le tipizzazioni personalizzate usate nel modulo di chunking.
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from enum import Enum

class ChunkSource(Enum):
    BODY = "body"
    TABLE = "table"

class Chunk(BaseModel):
    id : str
    document_id : str
    project_id : str
    content : str
    page_number : Optional[int] = None
    section : Optional[List[str]] = None
    source : ChunkSource = ChunkSource.BODY
    order : int = 0
    extra_data : Dict[str, Any] = None

class ChunkingConfig(BaseModel):
    chunk_size : int = 500
    overlap_size : int = 50
    min_characters : int = 100
    preserve_headers : bool = True

