import pandas as pd

# Create the Series with custom labels
products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

# Access the price of 'Laptop' using label-based indexing
laptop_price = products['Laptop']

# Slice the first two products using positional indexing
first_two_products = products.iloc[:2]

# Print outputs
print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products (Positional Indexing):")
print(first_two_products)