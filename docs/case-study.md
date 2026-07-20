# Case Study

## Context

Organizations frequently store operational and policy knowledge in PDF documents, scanned files and spreadsheets. Locating a precise answer may require manually reviewing multiple documents, pages and worksheets.

## Need

Build a local assistant that allows users to query an enterprise document collection using natural language while preserving traceability to the supporting source.

## Solution

A Retrieval-Augmented Generation (RAG) assistant was designed and implemented with the following flow:

1. Extract text from PDF and Excel files.
2. Apply OCR when a PDF page does not contain usable digital text.
3. Split content into token-aware chunks with metadata.
4. Generate embeddings with OpenAI.
5. Store and query vectors with ChromaDB.
6. Combine semantic retrieval with BM25 keyword ranking.
7. Build an answer from the retrieved context.
8. Display citations, similarity scores and the original document evidence.

## My contribution

- Designed the end-to-end RAG architecture.
- Implemented document extraction and OCR support.
- Developed token-aware chunking and metadata preservation.
- Integrated OpenAI embeddings and response generation.
- Implemented persistent vector retrieval with ChromaDB.
- Built a hybrid semantic and BM25 search strategy.
- Developed the Flask-based web experience.
- Added quick and expert query modes.
- Added document filters, citations and an evidence panel.
- Implemented source document highlighting.
- Added local server control and optional PIN access.

## Demonstrated capabilities

- Grounded answers with numbered citations.
- Retrieval metadata by document, page, content type and extraction source.
- Similarity scores for retrieved evidence.
- Original PDF visualization with highlighted supporting passages.
- Query filtering by document type and source.
- Export and user-feedback controls.
- Local and private-network execution.

## Result

The solution transforms unstructured and semi-structured documents into a searchable knowledge base that can be queried through a conversational interface. The user can inspect the evidence used for each answer instead of receiving an unsupported model response.

## Public portfolio scope

This public repository documents and reconstructs the technical concepts of a private implementation. It does not expose confidential documents, generated embeddings, private indexes, credentials, internal network details or client-specific business logic.
