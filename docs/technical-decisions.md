# Technical decisions

This document summarizes the main engineering decisions behind the private RAG application and the public portfolio reconstruction.

## OpenAI embeddings

The system uses OpenAI embeddings to represent document chunks as vectors and support semantic retrieval.

Why this choice:

- Strong semantic representation for natural-language queries.
- Simple API integration from Python.
- Good fit for multilingual enterprise documents.
- Compatible with persistent vector stores such as ChromaDB.

Trade-off:

- Embedding generation depends on an external service and introduces usage cost, latency and data-governance considerations.

## ChromaDB as the vector store

ChromaDB was selected for local persistence and straightforward integration with Python.

Why this choice:

- Easy local development.
- Persistent collections without requiring a separate database server.
- Metadata filtering.
- Suitable for prototypes and internal applications.

Trade-off:

- A larger production deployment may require a managed or distributed vector database with stronger scalability, access control and operational guarantees.

## Hybrid retrieval: semantic similarity and BM25

The application combines vector similarity with BM25 keyword retrieval.

Why this choice:

- Semantic retrieval captures meaning and paraphrases.
- BM25 improves exact matching for names, codes, dates and domain-specific terms.
- Combining both signals reduces the limitations of relying on only one retrieval method.

The current public example uses configurable weights so retrieval behavior can be adjusted during evaluation.

## Token-aware chunking

Documents are divided using token limits rather than only character counts.

Initial project parameters:

- Target chunk size: approximately 600 tokens.
- Overlap: approximately 100 tokens.

Why this choice:

- Keeps chunks within model context constraints.
- Preserves enough context for coherent answers.
- Overlap reduces information loss across chunk boundaries.

These values are starting points, not universal defaults. They should be tuned with retrieval evaluation and representative documents.

## Metadata preservation

Each chunk preserves contextual metadata such as:

- Document name.
- File type.
- PDF page.
- Excel worksheet.
- Row range.
- Section or content type.
- Extraction source, such as direct text or OCR.

Why this choice:

Metadata enables source citations, filtering, evidence inspection and traceability.

## OCR fallback

Tesseract OCR is used when a PDF page does not contain usable embedded text.

Why this choice:

- Local execution.
- Open-source tooling.
- Useful fallback for scanned documents.

Trade-off:

OCR quality depends on scan resolution, orientation, language and document layout. Production use may benefit from managed document-intelligence services.

## Flask and local execution

The original application uses Flask with a lightweight web interface and a local server-control panel.

Why this choice:

- Fast development cycle.
- Simple integration with Python services.
- Appropriate for a controlled internal proof of concept.

Trade-off:

A production environment should add stronger authentication, authorization, observability, deployment automation and horizontal scalability.

## Grounded response behavior

The answer-generation prompt is designed to use retrieved context and expose numbered references.

The intended behavior is:

- Answer from the available evidence.
- Cite the supporting chunks.
- Avoid inventing information when evidence is insufficient.
- Allow users to inspect the original source passage.

## Public reconstruction strategy

The public repository does not copy the complete private implementation. It publishes:

- Sanitized screenshots.
- Architecture and design decisions.
- Reusable, generic technical components.
- No private documents, embeddings, indexes, credentials or client-specific logic.
