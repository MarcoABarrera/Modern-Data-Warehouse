import requests
import psycopg2

# -------------------------
# CONFIG
# -------------------------
DB_CONFIG = {
    "host": "localhost",
    "database": "warehouse",
    "user": "user",
    "password": "password"
}

API_URL = "https://fakestoreapi.com/products"


# -------------------------
# FETCH DATA
# -------------------------
def fetch_products():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


# -------------------------
# DB CONNECTION
# -------------------------
def connect_db():
    return psycopg2.connect(**DB_CONFIG)


# -------------------------
# CREATE TABLE
# -------------------------
def create_table(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_products (
        id INT PRIMARY KEY,
        title TEXT,
        price FLOAT,
        category TEXT
    );
    """)


# -------------------------
# INSERT DATA
# -------------------------
def insert_products(cur, data):
    for item in data:
        cur.execute("""
            INSERT INTO raw_products (id, title, price, category)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            item['id'],
            item['title'],
            item['price'],
            item['category']
        ))


# -------------------------
# MAIN PIPELINE
# -------------------------
def main():
    print("Fetching data from API...")
    data = fetch_products()

    print(f"Fetched {len(data)} records")

    conn = connect_db()
    cur = conn.cursor()

    print("Creating table...")
    create_table(cur)

    print("Inserting data...")
    insert_products(cur, data)

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Data successfully loaded into PostgreSQL!")


if __name__ == "__main__":
    main()