import numpy as np

# Step 1: Create a 5x3 array of random student scores (50–100)
np.random.seed(42)  # for reproducibility
scores = np.random.randint(50, 101, size=(5, 3))

# Step 2: Compute column-wise mean (mean score per subject)
subject_means = scores.mean(axis=0)

# Step 3: Subtract the mean using broadcasting
centered_scores = scores - subject_means

# Output
print("Original Scores:")
print(scores)

print("\nSubject-wise Means:")
print(subject_means)

print("\nCentered Scores (after broadcasting):")
print(centered_scores)
