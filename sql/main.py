from connection import get_connection
from queries import fetch_customers, fetch_customers_dataframe


def main() -> None:
    with get_connection() as connection:
        print("Connected")

        customer_dataframe = fetch_customers_dataframe(connection)
        print(customer_dataframe.head())

        customer_rows = fetch_customers(connection)
        print(customer_rows)


if __name__ == "__main__":
    main()