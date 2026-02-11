import pandas as pd

# Create the Series with missing values
grades = pd.Series([85, None, 92, 45, None, 78, 55])

# Identify missing values
missing_values = grades.isnull()

# Fill missing values with 0
filled_grades = grades.fillna(0)

# Apply boolean mask to filter scores greater than 60
filtered_grades = filled_grades[filled_grades > 60]

# Print outputs
print("Original Series:")
print(grades)

print("\nMissing Values (True indicates missing):")
print(missing_values)

print("\nFilled Series (Missing values replaced with 0):")
print(filled_grades)

print("\nScores Greater Than 60:")
print(filtered_grades)
