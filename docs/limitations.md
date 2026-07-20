# Limitations

This repository represents a public portfolio reconstruction of a private enterprise RAG application. It documents the implemented architecture and includes selected reusable components, but it is not yet a complete production deployment.

## Current limitations

- The public version does not include the full private application.
- The current execution model is primarily local.
- PIN access is only a lightweight control and is not a substitute for enterprise identity management.
- OCR quality depends on document resolution, layout and scan quality.
- Generated answers depend on the quality of document extraction, chunking and retrieval.
- The system relies on external model services for embeddings and answer generation.
- Automated RAG evaluation is not yet included in the public repository.
- Role-based access control by document or user is not implemented.
- The public repository does not yet include a complete Docker deployment.
- Observability for latency, token usage, cost and failures remains part of the roadmap.

## Production considerations

A production-ready version should add:

- Enterprise authentication and authorization.
- HTTPS and secure secret management.
- Document-level permissions.
- File validation and malware scanning.
- Encryption at rest and in transit.
- Rate limiting and abuse controls.
- Audit logs and retention policies.
- Automated tests and continuous integration.
- RAG evaluation datasets and quality thresholds.
- Monitoring for latency, token consumption and cost.

## Portfolio scope

The screenshots and documentation demonstrate a working private implementation. The public code is intentionally reduced and reconstructed to protect confidential information, private documents and organization-specific logic.
