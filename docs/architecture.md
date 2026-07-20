# Architecture

## Overview

The project separates ingestion, retrieval, generation and delivery concerns so each component can be tested and replaced independently.

```text
Documents
   |
   v
Ingestion layer
- PDF loader
- Excel loader
- OCR adapter
- metadata enrichment
- token-aware chunking
   |
   v
Embedding and indexing layer
- OpenAI embeddings
- ChromaDB persistent collection
   |
   v
Retrieval layer
- vector similarity
- BM25 keyword relevance
- weighted hybrid ranking
   |
   v
Generation layer
- context assembly
- grounded prompt
- answer with citations
   |
   v
Flask API and web client
```

## Design principles

1. No private documents or generated indexes are committed.
2. Configuration is loaded from environment variables.
3. Retrieval logic is independent from the web framework.
4. Metadata is preserved through the full pipeline.
5. The language model must answer from retrieved context and expose sources.
6. Components should be covered by unit and integration tests.

## Planned modules

- `ingestion`: loaders, OCR and chunking.
- `retrieval`: embeddings, vector store, BM25 and hybrid ranking.
- `generation`: prompts and answer generation.
- `api`: HTTP routes and request validation.
