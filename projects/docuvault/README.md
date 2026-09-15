# DocuVault

DocuVault is a small Python project that ingests text documents from a folder, builds a vocabulary, vectorizes each document, and then performs cosine-similarity search over the stored content.

## Project purpose

This project demonstrates a simple retrieval workflow:

- read `.txt` files from a folder
- clean text and build a shared vocabulary
- convert each document into a term-frequency vector
- compare a query vector against document vectors using cosine similarity
- return the most relevant document matches

## Folder structure

- `cli.py` — command-line interface
- `models.py` — `Document` and `KnowledgeBase` classes
- `vectorizer.py` — text preprocessing, frequency counting, and cosine similarity
- `search.py` — retrieval function
- `storage.py` — save/load knowledge base to JSON
- `logging_store.py` — search log and report generation
- `docs/` — sample documents used for testing
- `tests/` — regression tests

## Requirements

- Python 3.10+
- NumPy

If you are using a virtual environment, activate it first:

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

## Run the app

From the project directory (`projects/docuvault`):

```bash
python cli.py ingest docs
python cli.py search "python programming" --top_k 3
python cli.py report
```

## Commands

### Ingest documents

```bash
python cli.py ingest <folder_path>
```

Example:

```bash
python cli.py ingest docs
```

This reads all `.txt` files in the folder and rebuilds the knowledge base.

### Search documents

```bash
python cli.py search "your query here" --top_k 5
```

Example:

```bash
python cli.py search "python programming" --top_k 3
```

The output shows the ranked results as:

```text
[0.4581] python_book (id=10)
```

### Generate report

```bash
python cli.py report
```

This prints a simple summary of the saved search activity from `search_log.csv`.

## Validation checks

A good smoke test for this project is:

1. ingest the folder
2. run a query that matches a known document
3. ensure the matching document appears near the top
4. run ingest again and confirm the document count does not grow unexpectedly

Example:

```bash
python cli.py ingest docs
python cli.py search "This is a Python programming book" --top_k 3
```

A healthy result should rank the `python_book` document highly.

## Notes

This project is intentionally lightweight and educational. It is not a production-grade search engine, but it demonstrates the essential pieces of a basic retrieval system:

- indexing
- token cleaning
- vocabulary construction
- vectorization
- cosine similarity search
- basic logging

## Running tests

```bash
python -m pytest -q
```

If `pytest` is not installed in your environment, install it first:

```bash
pip install pytest
```
