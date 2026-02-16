import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Load dataset
df = pd.read_csv("housing_data_small.csv")

# Plot Histogram with KDE
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()



price_skewness = skew(df['Price'])
price_kurtosis = kurtosis(df['Price'])

print("Skewness:", price_skewness)
print("Kurtosis:", price_kurtosis)

plt.figure(figsize=(8,5))
sns.countplot(x='City', data=df)
plt.title("Count of Houses by City")
plt.xticks(rotation=45)
plt.show()

print(df['City'].value_counts())
import numpy as np
df['Price_log'] = np.log1p(df['Price'])
