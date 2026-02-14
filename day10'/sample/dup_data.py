import pandas as pd

data = {
    "CustomerID": [101, 102, 102, 104],
    "Name": ["Alice", "Bob", "Bob", "Charlie"],
    "Purchase": [500, 300, 300, 700]
}

df = pd.DataFrame(data)

print(df.duplicated())

print("Number of duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print(df)

print(df.duplicated(subset="CustomerID"))
