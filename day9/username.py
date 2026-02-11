import pandas as pd

# Create the Series with inconsistent usernames
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

# Remove leading/trailing whitespace and convert to lowercase
cleaned_usernames = usernames.str.strip().str.lower()

# Check which names contain the letter 'a'
contains_a = cleaned_usernames.str.contains('a')

# Print outputs
print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nContains letter 'a':")
print(contains_a)
