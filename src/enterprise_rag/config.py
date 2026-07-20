from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    chat_model: str = "gpt-4.1-mini"
    embedding_model: str = "text-embedding-3-small"
    chroma_path: str = "chroma_db"
    chroma_collection: str = "enterprise_documents"
    app_host: str = "127.0.0.1"
    app_port: int = 5000
    top_k: int = 6
    semantic_weight: float = 0.70
    keyword_weight: float = 0.30

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is required. Copy .env.example to .env and configure it.")

        semantic_weight = float(os.getenv("SEMANTIC_WEIGHT", "0.70"))
        keyword_weight = float(os.getenv("KEYWORD_WEIGHT", "0.30"))
        if semantic_weight < 0 or keyword_weight < 0:
            raise ValueError("Retrieval weights must be non-negative.")
        if semantic_weight + keyword_weight == 0:
            raise ValueError("At least one retrieval weight must be greater than zero.")

        return cls(
            openai_api_key=api_key,
            chat_model=os.getenv("OPENAI_CHAT_MODEL", "gpt-4.1-mini"),
            embedding_model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
            chroma_path=os.getenv("CHROMA_PATH", "chroma_db"),
            chroma_collection=os.getenv("CHROMA_COLLECTION", "enterprise_documents"),
            app_host=os.getenv("APP_HOST", "127.0.0.1"),
            app_port=int(os.getenv("APP_PORT", "5000")),
            top_k=int(os.getenv("TOP_K", "6")),
            semantic_weight=semantic_weight,
            keyword_weight=keyword_weight,
        )
