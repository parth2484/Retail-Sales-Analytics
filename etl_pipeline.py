"""
ETL Pipeline: Load Retail Sales Data from CSV to MySQL Database
Author: (Your Name)
Description:
 - Extract data from a CSV file
 - Transform data by calculating total sale amount
 - Load processed data into MySQL table
"""

import pandas as pd
import mysql.connector

# ---------------------- CONFIGURATION ---------------------- #
CSV_FILE_PATH = "data/sales.csv"     # Path to your dataset
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "YOUR_PASSWORD"        # <-- Replace this
DB_NAME = "retail_sales"
# ------------------------------------------------------------ #

# Step 1: Extract – Read CSV file
df = pd.read_csv(CSV_FILE_PATH)

# Step 2: Transform – Calculate total sale amount
df["total_amount"] = df["quantity"] * df["price"]

# Step 3: Load – Insert into MySQL
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales (sale_date, product_name, quantity, price, total_amount)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row["sale_date"],
        row["product_name"],
        row["quantity"],
        row["price"],
        row["total_amount"]
    ))

conn.commit()
conn.close()

print("✅ Data loaded successfully into MySQL!")
