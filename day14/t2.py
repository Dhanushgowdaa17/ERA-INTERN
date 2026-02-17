import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
    "Age": [22, 25, 47, 52, 46, 56, 48, 30],
    "Salary": [30000, 35000, 80000, 90000, 85000, 95000, 87000, 40000]
})

scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(
    scaler_standard.fit_transform(df),
    columns=df.columns
)

scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_minmax.fit_transform(df),
    columns=df.columns
)

plt.figure()
plt.hist(df["Salary"])
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()


plt.figure()
plt.hist(df_standardized["Salary"])
plt.title("Salary After Standardization")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.hist(df_normalized["Salary"])
plt.title("Salary After Normalization")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()
