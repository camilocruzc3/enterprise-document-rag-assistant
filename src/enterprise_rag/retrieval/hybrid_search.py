from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
from rank_bm25 import BM25Okapi


@dataclass(frozen=True)
class SearchDocument:
    content: str
    embedding: Sequence[float]
    metadata: dict[str, str | int | float | None]


@dataclass(frozen=True)
class SearchResult:
    document: SearchDocument
    semantic_score: float
    keyword_score: float
    hybrid_score: float


def _cosine_similarity(left: Sequence[float], right: Sequence[float]) -> float:
    left_array = np.asarray(left, dtype=float)
    right_array = np.asarray(right, dtype=float)
    denominator = np.linalg.norm(left_array) * np.linalg.norm(right_array)
    if denominator == 0:
        return 0.0
    return float(np.dot(left_array, right_array) / denominator)


def _normalize(scores: Sequence[float]) -> list[float]:
    if not scores:
        return []
    minimum = min(scores)
    maximum = max(scores)
    if maximum == minimum:
        return [1.0 if maximum > 0 else 0.0 for _ in scores]
    return [(score - minimum) / (maximum - minimum) for score in scores]


class HybridRetriever:
    """Combine embedding similarity and BM25 keyword relevance."""

    def __init__(self, documents: Sequence[SearchDocument]) -> None:
        self.documents = list(documents)
        tokenized = [document.content.lower().split() for document in self.documents]
        self.bm25 = BM25Okapi(tokenized) if tokenized else None

    def search(
        self,
        query: str,
        query_embedding: Sequence[float],
        top_k: int = 6,
        semantic_weight: float = 0.70,
        keyword_weight: float = 0.30,
    ) -> list[SearchResult]:
        if not self.documents:
            return []
        if top_k <= 0:
            raise ValueError("top_k must be greater than zero")

        semantic_raw = [
            _cosine_similarity(query_embedding, document.embedding)
            for document in self.documents
        ]
        keyword_raw = list(self.bm25.get_scores(query.lower().split())) if self.bm25 else [0.0] * len(self.documents)
        semantic_scores = _normalize(semantic_raw)
        keyword_scores = _normalize(keyword_raw)

        results = [
            SearchResult(
                document=document,
                semantic_score=semantic_raw[index],
                keyword_score=float(keyword_raw[index]),
                hybrid_score=(semantic_weight * semantic_scores[index]) + (keyword_weight * keyword_scores[index]),
            )
            for index, document in enumerate(self.documents)
        ]
        return sorted(results, key=lambda item: item.hybrid_score, reverse=True)[:top_k]
