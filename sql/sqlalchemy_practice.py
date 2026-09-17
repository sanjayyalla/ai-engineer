import os

from dotenv import load_dotenv
from sqlalchemy import Integer, String, create_engine, select, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[str] = mapped_column(String, primary_key=True)
    customer_unique_id: Mapped[str] = mapped_column(String)
    customer_zip_code_prefix: Mapped[int] = mapped_column(Integer)
    customer_city: Mapped[str] = mapped_column(String)
    customer_state: Mapped[str] = mapped_column(String)


def create_database_engine():
    """Create a SQLAlchemy engine using the project's PostgreSQL settings."""
    load_dotenv()

    database_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        database=os.getenv("POSTGRES_DB", "ai_engineering_db"),
    )
    return create_engine(database_url, echo=False)


def run_core_example(engine) -> None:
    """Run a SQLAlchemy Core query with a parameterized SQL statement."""
    statement = text(
        """
        SELECT customer_id, customer_city, customer_state
        FROM customers
        WHERE customer_state = :state
        ORDER BY customer_city
        LIMIT :limit
        """
    )

    with engine.connect() as connection:
        rows = connection.execute(statement, {"state": "SP", "limit": 5})
        print("SQLAlchemy Core results:")
        for row in rows:
            print(row)


def run_orm_example(engine) -> None:
    """Run the equivalent query through SQLAlchemy's ORM Session API."""
    statement = (
        select(Customer)
        .where(Customer.customer_state == "SP")
        .order_by(Customer.customer_city)
        .limit(5)
    )

    with Session(engine) as session:
        customers = session.scalars(statement).all()

    print("\nSQLAlchemy ORM results:")
    for customer in customers:
        print(f"{customer.customer_id}: {customer.customer_city}, {customer.customer_state}")


def main() -> None:
    engine = create_database_engine()
    try:
        run_core_example(engine)
        run_orm_example(engine)
    finally:
        engine.dispose()


if __name__ == "__main__":
    main()