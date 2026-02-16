import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("housing_data_small.csv")
numerical_df = df.select_dtypes(include=['int64', 'float64'])
corr_matrix = numerical_df.corr()
print(corr_matrix)
plt.figure(figsize=(4,4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

threshold = 0.8

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > threshold:
            print(f"{corr_matrix.columns[i]} and {corr_matrix.columns[j]} "
                  f"have correlation = {corr_matrix.iloc[i, j]:.2f}")

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price")
plt.ylabel("Price")
plt.show()
