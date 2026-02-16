import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("housing_data_small.csv")

# 1️⃣ Scatter Plot: Size vs Price
plt.figure()
plt.scatter(df["Size_sqft"], df["Price"])
plt.xlabel("Size (Square Footage)")
plt.ylabel("Price")
plt.title("Scatter Plot: Size vs Price")
plt.show()

# 2️⃣ Boxplot: City vs Price
plt.figure()
df.boxplot(column="Price", by="City")
plt.xlabel("City")
plt.ylabel("Price")
plt.title("Boxplot: City vs Price")
plt.suptitle("")  # removes automatic subtitle
plt.show()

# Optional: Correlation
correlation = df["Size_sqft"].corr(df["Price"])
print("Correlation between Size and Price:", correlation)
