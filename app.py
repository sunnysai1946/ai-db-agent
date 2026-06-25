import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="AI Database Assistant")

st.title("🤖 AI Database Assistant")

conn = sqlite3.connect("products.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY,
name TEXT,
price INTEGER
)
""")

cursor.execute("SELECT COUNT(*) FROM products")

if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO products VALUES(1,'Laptop',50000)")
    cursor.execute("INSERT INTO products VALUES(2,'Phone',20000)")
    cursor.execute("INSERT INTO products VALUES(3,'Headphones',3000)")
    conn.commit()

question = st.text_input("Ask a question")

if st.button("Show Products"):
    df = pd.read_sql_query(
        "SELECT * FROM products",
        conn
    )

    st.dataframe(df)
