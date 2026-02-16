import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    "Salary": [30070, 83500, 49000, 45500, 58450, 55000, 60080, 65000, 38000, 75000, 80670, 85000],
    "Department": ["HR", "Finance", "IT", "Marketing", "HR", "Finance", "IT", "Marketing", "HR", "Finance", "IT", "Marketing"],
    "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
    "Experience": [2, 5, 7, 10, 12, 15, 20, 25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)
print(df)

plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")      
plt.show()

plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Experience vs Salary")
plt.show()

plt.figure()
sns.boxplot(x="Gender", y="Salary", data=df)
plt.title("Salary by Gender")
plt.show()

plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary by Department")
plt.show()

#correlation matrix

corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="seismic", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()



#outlier detection
plt.figure()
sns.boxplot(x=df["Age"])
plt.title("Age Outlier")
plt.show()

plt.figure()
sns.boxplot(x=df["Experience"])
plt.title("Experience Outliers")
plt.show()

#document insights
#FINAL STEP — DOCUMENT INSIGHTS (PRINT SAMPLE INSIGHTS)
# Students should write their own observations here.


print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary increases with Experience and Age (positive correlation).")
print("2. Finance department shows higher salary range.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")