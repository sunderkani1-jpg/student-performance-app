import matplotlib.pyplot as plt

# ======= Inputs =======
# Each student has 4 features: [Past %, Attendance %, Study Hours/Week, Internal Marks]
students_data = [
    [95, 88, 18, 42],   # Example student 1
    [78, 92, 20, 50],   # Example student 2
    [65, 70, 10, 35],   # Example student 3
    [80, 85, 15, 40]    # Example student 4
]

# Expected max marks for prediction
max_marks = 85

# ======= Step 1: Normalize each feature =======
# Find min & max for each column
columns = list(zip(*students_data))  # transpose to columns
min_vals = [min(col) for col in columns]
max_vals = [max(col) for col in columns]

normalized_data = []
for row in students_data:
    norm_row = [(row[i]-min_vals[i])/(max_vals[i]-min_vals[i]) for i in range(len(row))]
    normalized_data.append(norm_row)

# ======= Step 2: Predict marks =======
# Example prediction: average of normalized features scaled to max_marks
predicted_marks = [sum(row)/len(row) * max_marks for row in normalized_data]

# ======= Step 3: Print results =======
for i, row in enumerate(students_data):
    print(f"Student {i+1} Inputs: {row}")
    print(f"Normalized Inputs: {normalized_data[i]}")
    print(f"Predicted Marks: {predicted_marks[i]:.2f}\n")

# ======= Step 4: Plot graph =======
plt.figure(figsize=(10,6))
student_ids = [f"S{i+1}" for i in range(len(students_data))]
plt.bar(student_ids, predicted_marks, color='skyblue')
plt.xlabel("Students")
plt.ylabel("Predicted Marks")
plt.title("Predicted Marks based on Past %, Attendance %, Study Hours & Internal Marks")
plt.show()
