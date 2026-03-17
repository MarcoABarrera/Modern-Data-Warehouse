import streamlit as st
import pandas as pd
import psycopg2

# ------------------------
# DB CONNECTION
# ------------------------
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="warehouse",
        user="user",
        password="password"
    )


# ------------------------
# LOAD DATA
# ------------------------
def load_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# ------------------------
# STREAMLIT UI
# ------------------------
st.title("📊 E-Commerce Data Dashboard")

# ------------------------
# KPIs
# ------------------------
kpi_query = """
SELECT
    SUM(total_value) AS revenue,
    COUNT(DISTINCT cart_id) AS orders,
    AVG(total_value) AS avg_order_value
FROM fact_cart_items;
"""

kpis = load_data(kpi_query)

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"${kpis['revenue'][0]:,.2f}")
col2.metric("🛒 Orders", int(kpis['orders'][0]))
col3.metric("📊 Avg Order Value", f"${kpis['avg_order_value'][0]:,.2f}")


# ------------------------
# Revenue per product
# ------------------------
st.subheader("Revenue per Product")

query1 = """
SELECT
    product_id,
    SUM(total_value) AS revenue
FROM fact_cart_items
GROUP BY product_id
ORDER BY revenue DESC;
"""

df1 = load_data(query1)
st.bar_chart(df1.set_index("product_id"))


# ------------------------
# Revenue over time
# ------------------------
st.subheader("Revenue Over Time")

query2 = """
SELECT
    date,
    SUM(total_value) AS revenue
FROM fact_cart_items
GROUP BY date
ORDER BY date;
"""

df2 = load_data(query2)
st.line_chart(df2.set_index("date"))


# ------------------------
# Top users
# ------------------------
st.subheader("Top Users")

query3 = """
SELECT
    user_id,
    SUM(total_value) AS total_spent
FROM fact_cart_items
GROUP BY user_id
ORDER BY total_spent DESC;
"""

df3 = load_data(query3)
st.bar_chart(df3.set_index("user_id"))