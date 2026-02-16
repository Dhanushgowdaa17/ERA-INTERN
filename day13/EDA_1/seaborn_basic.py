import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    "Salary": [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000],
    "Department": ["HR", "Finance", "IT", "Marketing", "HR", "Finance", "IT", "Marketing", "HR", "Finance", "IT", "Marketing"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F"]
}

df = pd.DataFrame(data)
print(df)

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Info:")
print(df.info())
df.describe()