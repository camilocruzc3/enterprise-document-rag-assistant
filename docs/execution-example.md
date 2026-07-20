# Anonymized execution example

This example illustrates the workflow of the private application using synthetic names and representative output. It is documentation evidence, not a claim that the current public repository already exposes every command shown below.

## 1. Extract document content

```text
$ python extract_text.py

Documents discovered: 6
PDF files processed: 4
Excel files processed: 2
Pages processed with OCR: 7
Extraction completed successfully.
```

The extraction stage preserves metadata such as document name, page, worksheet, row range, content type and extraction source.

## 2. Generate chunks and embeddings

```text
$ python generate_embeddings.py

Sections processed: 53
Chunks generated: 186
Target chunk size: 600 tokens
Chunk overlap: 100 tokens
Embedding model: text-embedding-3-small
Embedding generation completed successfully.
```

The values above are representative and are included only to demonstrate the type of operational feedback produced by the application.

## 3. Build the persistent vector index

```text
$ python build_chroma_index.py

Collection: portfolio_documents
Indexed chunks: 186
Vector index persisted successfully.
```

The generated ChromaDB directory is local and is intentionally excluded from the public repository.

## 4. Start the application

```text
$ python app_web.py

Server started successfully.
Local URL: http://localhost:5000
```

The original application also includes a local desktop control panel to start and stop the Flask service.

## 5. Example query

```text
Question:
What responsibilities are assigned to the data owner?
```

```text
Answer:
The data owner is responsible for defining the business use of the data,
approving access criteria and supporting data-quality decisions.

Sources:
[1] data_governance_policy_demo.pdf — page 8
[2] data_roles_demo.xlsx — worksheet Roles, rows 4-7
```

## 6. Evidence inspection

The interface allows the user to inspect:

- Retrieved source document.
- Page or worksheet location.
- Extraction source, including OCR when applicable.
- Retrieved text fragment.
- Similarity score.
- Highlighted passage inside the original PDF.

## Interpretation

This workflow demonstrates the main stages of the implemented RAG system:

```text
Documents
  -> extraction and OCR
  -> chunking and metadata
  -> embeddings and ChromaDB
  -> hybrid retrieval
  -> grounded generation
  -> citations and evidence inspection
```
