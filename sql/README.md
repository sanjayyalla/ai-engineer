# PostgreSQL practice

This folder contains the PostgreSQL connection and query experiments for the
Olist dataset.

## Structure

- `connection.py` creates a PostgreSQL connection from environment variables.
- `queries.py` contains reusable database queries.
- `main.py` runs the current query examples.
- `sqlalchemy_practice.py` demonstrates SQLAlchemy Core and ORM queries.
- `postgres_python_conn.py` keeps the original script path as a compatibility entry point.
- `datasets/` contains the source CSV files.

## Configuration

Create a `.env` file in the project root with at least:

```text
POSTGRES_PASSWORD=your_password
```

The remaining connection settings default to `localhost`, port `5432`,
database `ai_engineering_db`, and user `postgres`. They can also be set with
`POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`, and `POSTGRES_USER`.

## Run

From the project root:

```powershell
python sql/postgres_python_conn.py
```

Run the SQLAlchemy example with:

```powershell
python sql/sqlalchemy_practice.py
```