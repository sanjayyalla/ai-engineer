import pandas as pd
import psycopg


def fetch_customers_dataframe(
    connection: psycopg.Connection,
    limit: int = 10,
) -> pd.DataFrame:
    """Return a limited customer result as a DataFrame."""
    query = """
        SELECT *
        FROM customers
        LIMIT %s;
    """
    with connection.cursor() as cursor:
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        columns = [column.name for column in cursor.description]

    return pd.DataFrame(rows, columns=columns)


def fetch_customers(
    connection: psycopg.Connection,
    limit: int = 5,
) -> list[tuple]:
    """Return a limited customer result as Python rows."""
    query = """
        SELECT *
        FROM customers
        LIMIT %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (limit,))
        return cursor.fetchall()