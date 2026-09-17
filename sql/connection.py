import os

import psycopg
from dotenv import load_dotenv


def get_connection() -> psycopg.Connection:
    """Create a PostgreSQL connection from environment configuration."""
    load_dotenv()

    return psycopg.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        dbname=os.getenv("POSTGRES_DB", "ai_engineering_db"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )