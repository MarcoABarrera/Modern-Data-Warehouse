import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

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
# LOAD DATA (CACHED)
# ------------------------
@st.cache_data
def load_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# ------------------------
# TITLE
# ------------------------
st.title("📊 E-Commerce Analytics Dashboard")

# ------------------------
# LOAD BASE DATA
# ------------------------
base_query = "SELECT * FROM fact_cart_items;"
df = load_data(base_query)

# ------------------------
# SIDEBAR FILTERS
# ------------------------
st.sidebar.header("Filters")

# Date filter
df["date"] = pd.to_datetime(df["date"])
min_date = df["date"].min()
max_date = df["date"].max()

date_range = st.sidebar.date_input(
    "Select date range",
    [min_date, max_date]
)

# Product filter
products = df["product_id"].unique()
selected_products = st.sidebar.multiselect(
    "Select products",
    products,
    default=products
)

# Apply filters
filtered_df = df[
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1])) &
    (df["product_id"].isin(selected_products))
]

# ------------------------
# KPIs
# ------------------------
st.subheader("📊 Key Metrics")

total_revenue = filtered_df["total_value"].sum()
total_orders = filtered_df["cart_id"].nunique()
avg_order_value = filtered_df["total_value"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Revenue", f"${total_revenue:,.2f}")
col2.metric("🛒 Orders", total_orders)
col3.metric("📊 Avg Order Value", f"${avg_order_value:,.2f}")

# ------------------------
# REVENUE OVER TIME
# ------------------------
st.subheader("📈 Revenue Over Time")

rev_time = (
    filtered_df.groupby("date")["total_value"]
    .sum()
    .reset_index()
)

st.line_chart(rev_time.set_index("date"))

# ------------------------
# TOP PRODUCTS
# ------------------------
st.subheader("🏆 Top Products")

top_products = (
    filtered_df.groupby("product_id")["total_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# ------------------------
# TOP USERS
# ------------------------
st.subheader("👤 Top Users")

top_users = (
    filtered_df.groupby("user_id")["total_value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_users)

# ------------------------
# RAW DATA VIEW
# ------------------------
with st.expander("🔍 Show Raw Data"):
    st.dataframe(filtered_df)