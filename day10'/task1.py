import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Original shape:", df.shape)

print(df.isna().sum())

numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df = df.drop_duplicates()

print("Cleaned shape:", df.shape)
