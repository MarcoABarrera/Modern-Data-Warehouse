def create_tables(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_products (
        id INT PRIMARY KEY,
        title TEXT,
        price FLOAT,
        category TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_users (
        id INT PRIMARY KEY,
        email TEXT,
        username TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_carts (
        id INT PRIMARY KEY,
        user_id INT,
        date DATE
    );
    """)


def load_products(cur, data):
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


def load_users(cur, data):
    for user in data:
        cur.execute("""
            INSERT INTO raw_users (id, email, username)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            user['id'],
            user['email'],
            user['username']
        ))


def load_carts(cur, data):
    for cart in data:
        cur.execute("""
            INSERT INTO raw_carts (id, user_id, date)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
        """, (
            cart['id'],
            cart['userId'],
            cart['date']
        ))