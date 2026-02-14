import matplotlib.pyplot as plt

# X values
study_hours = [1, 2, 3, 4, 5]

# Y values
marks = [40, 50, 65, 70, 85]

plt.scatter(study_hours, marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.show()