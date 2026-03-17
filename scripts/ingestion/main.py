from config import API_ENDPOINTS
from db import get_connection
from api import fetch_data
from loaders import create_tables, load_products, load_users, load_carts


def main():
    print("Starting ingestion pipeline...")

    conn = get_connection()
    cur = conn.cursor()

    print("Creating tables...")
    create_tables(cur)

    print("Fetching and loading PRODUCTS...")
    products = fetch_data(API_ENDPOINTS["products"])
    load_products(cur, products)

    print("Fetching and loading USERS...")
    users = fetch_data(API_ENDPOINTS["users"])
    load_users(cur, users)

    print("Fetching and loading CARTS...")
    carts = fetch_data(API_ENDPOINTS["carts"])
    load_carts(cur, carts)

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Pipeline finished successfully!")


if __name__ == "__main__":
    main()