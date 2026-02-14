import pandas as pd

df = pd.read_csv("customer_orders.csv")

df.columns = df.columns.str.strip().str.lower()

print("Available columns:", df.columns)

if "location" in df.columns:
    print(df["location"].unique())
    df["location"] = df["location"].str.strip().str.title()
    print(df["location"].unique())
else:
    print("Column 'location' does not exist in this dataset.")
