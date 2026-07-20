# Roadmap

The public repository is currently focused on architecture, technical evidence and selected reusable components. The following roadmap describes the path toward a reproducible public demo.

## Phase 1 — Portfolio documentation

- [x] Publish a recruiter-facing README.
- [x] Add sanitized application screenshots.
- [x] Document the case study.
- [x] Document the architecture.
- [x] Document security and privacy controls.
- [x] Document technical decisions.
- [x] Document current limitations.
- [x] Add an anonymized execution example.

## Phase 2 — Minimal reproducible demo

- [ ] Add synthetic PDF and Excel documents.
- [ ] Implement public PDF ingestion.
- [ ] Implement public Excel ingestion.
- [ ] Add optional OCR fallback.
- [ ] Persist normalized chunks and metadata.
- [ ] Generate embeddings from environment-based credentials.
- [ ] Build a local ChromaDB index.
- [ ] Add a command-line query workflow.
- [ ] Return answers with source references.

## Phase 3 — Quality and evaluation

- [ ] Add unit tests for chunking and retrieval.
- [ ] Add integration tests for the ingestion pipeline.
- [ ] Create a small evaluation dataset.
- [ ] Measure Precision@K and Recall@K.
- [ ] Evaluate answer groundedness and citation correctness.
- [ ] Track latency, token usage and estimated cost.
- [ ] Tune chunk size, overlap and hybrid-search weights.

## Phase 4 — Application and deployment

- [ ] Add a public Flask API.
- [ ] Add a lightweight demonstration interface.
- [ ] Package the application with Docker.
- [ ] Add CI checks for tests and formatting.
- [ ] Add structured logging and health checks.
- [ ] Document deployment options.

## Potential enterprise extensions

- Enterprise identity and role-based access control.
- Document-level authorization.
- Managed secret storage.
- Encryption at rest and in transit.
- Audit trails and retention policies.
- Azure OpenAI or another managed model provider.
- Managed document-intelligence and vector-search services.
- Monitoring for retrieval quality, model drift and operational cost.
