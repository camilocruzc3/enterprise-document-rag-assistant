from __future__ import annotations

from dataclasses import dataclass

import tiktoken


@dataclass(frozen=True)
class TextChunk:
    content: str
    chunk_index: int
    token_count: int
    metadata: dict[str, str | int | None]


class TokenChunker:
    """Split text into overlapping token windows while preserving metadata."""

    def __init__(self, model: str = "text-embedding-3-small", chunk_size: int = 600, overlap: int = 100) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero")
        if overlap < 0 or overlap >= chunk_size:
            raise ValueError("overlap must be between zero and chunk_size - 1")

        self.encoding = tiktoken.encoding_for_model(model)
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text: str, metadata: dict[str, str | int | None] | None = None) -> list[TextChunk]:
        clean_text = text.strip()
        if not clean_text:
            return []

        tokens = self.encoding.encode(clean_text)
        step = self.chunk_size - self.overlap
        base_metadata = metadata or {}
        chunks: list[TextChunk] = []

        for chunk_index, start in enumerate(range(0, len(tokens), step)):
            token_slice = tokens[start : start + self.chunk_size]
            if not token_slice:
                continue
            content = self.encoding.decode(token_slice).strip()
            if content:
                chunks.append(
                    TextChunk(
                        content=content,
                        chunk_index=chunk_index,
                        token_count=len(token_slice),
                        metadata={**base_metadata, "chunk_index": chunk_index},
                    )
                )

        return chunks
