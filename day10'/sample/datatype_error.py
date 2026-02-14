import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": ["25", "30", "35"],
}
df =pd.DataFrame(data)      
print(df.dtypes)

df["Age"] = df["Age"].astype(int)
print(df.dtypes)
print(df["Age"].mean())

import pandas as pd

data = {
    "Joining Date": ["2021-01-15", "2020-06-30", "2019-11-20"],
    "Salary": ["$50,000", "$60,000", "$70,000"]
}
df = pd.DataFrame(data)
print(df.dtypes)
df["Joining Date"] = pd.to_datetime(df["Joining Date"])
print(df.dtypes)
print(df["Joining Date"].dt.year)

