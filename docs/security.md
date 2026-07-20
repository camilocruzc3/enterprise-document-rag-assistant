# Security and privacy

This public repository is designed to avoid exposing confidential information.

## Never commit

- `.env` files or API keys.
- Private PDF, Excel or image files.
- Generated embeddings or vector indexes.
- Application logs containing prompts or document content.
- Client names, internal URLs, IP addresses or credentials.
- Production-specific business rules.

## Current controls

- Secrets are loaded from environment variables.
- `.gitignore` excludes generated data, indexes, logs and local documents.
- The default application host is `127.0.0.1`, not all network interfaces.
- Public examples must use synthetic or openly licensed data.

## Before deployment

A production deployment should add authentication, authorization, HTTPS, rate limiting, audit logging, input validation, malware scanning for uploads, encryption at rest and in transit, secret management and retention policies.
