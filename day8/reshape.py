import numpy as np

# Create a 1D array with values 0 to 23
data = np.arange(24)

# Reshape into (4, 3, 2): 4 batches, each a 3x2 matrix
reshaped = data.reshape(4, 3, 2)

# Transpose to get shape (4, 2, 3)
final_array = reshaped.transpose(0, 2, 1)

# Output
print("Final shape:")
print(final_array.shape)

print("\nFinal array:")
print(final_array)       