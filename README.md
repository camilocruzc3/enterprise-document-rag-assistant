# Enterprise Document RAG Assistant

Public portfolio implementation of a Retrieval-Augmented Generation (RAG) assistant for querying PDF and Excel documents with natural language.

## What this project demonstrates

- Document ingestion for PDF and Excel.
- Optional OCR for scanned PDFs.
- Token-aware chunking with metadata.
- OpenAI embeddings.
- Persistent local vector storage with ChromaDB.
- Hybrid retrieval combining semantic similarity and BM25.
- Grounded answers with source references.
- Modular Python architecture, tests and Docker support.

## Problem

Organizations often store valuable knowledge across PDF reports, scanned documents and spreadsheets. Finding a precise answer can require manually reviewing many files, pages and worksheets.

This project converts those documents into a searchable knowledge base and lets users ask questions in natural language while preserving traceability to the original sources.

## Architecture

```text
PDF / XLS / XLSX
        |
        v
Text extraction and optional OCR
        |
        v
Token-aware chunking and metadata enrichment
        |
        v
OpenAI embeddings
        |
        v
ChromaDB persistent vector store
        |
        v
Hybrid retrieval: semantic similarity + BM25
        |
        v
Prompt construction with retrieved context
        |
        v
Grounded answer with source references
```

## Main features

- PDF and Excel ingestion.
- OCR fallback for scanned PDF pages.
- Token-aware chunking with overlap.
- Metadata for document, page, sheet and section.
- Local persistent vector index.
- Hybrid ranking using semantic and keyword signals.
- Flask API and lightweight web interface.
- Source references in every answer.
- Environment-based configuration.
- Public sample data only.

## Technology stack

Python 3.11+, Flask, OpenAI API, ChromaDB, PyMuPDF, Tesseract OCR, pandas, openpyxl, NumPy, tiktoken, pytest and Docker.

## Project structure

```text
src/enterprise_rag/
|-- api/
|-- generation/
|-- ingestion/
|-- retrieval/
|-- app.py
`-- config.py

scripts/
tests/
sample_data/
docs/
templates/
static/
```

## Quick start

```bash
git clone https://github.com/camilocruzc3/enterprise-document-rag-assistant.git
cd enterprise-document-rag-assistant
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment file:

```bash
cp .env.example .env
```

Add public or synthetic documents to `sample_data/documents/`, then run:

```bash
python scripts/ingest_documents.py
python scripts/build_index.py
python -m enterprise_rag.app
```

Open `http://localhost:5000`.

## Security and privacy

This repository intentionally excludes private documents, generated embeddings, ChromaDB indexes, logs, API keys, client-specific logic and the commit history of the private implementation.

See [`docs/security.md`](docs/security.md).

## Portfolio context

This repository is a clean public reconstruction of a private enterprise-document assistant. It demonstrates AI engineering practices without exposing confidential information.

## License

MIT License.
