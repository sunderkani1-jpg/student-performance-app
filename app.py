import matplotlib.pyplot as plt

# ======= Student Data =======
# Each student: [Past %, Attendance %, Study Hours/Week, Internal Marks]
students_data = [
    [95, 88, 18, 42],
    [78, 92, 20, 50],
    [65, 70, 10, 35],
    [80, 85, 15, 40]
]

# Max marks
max_marks = 85

# ======= Step 1: Normalize each feature =======
columns = list(zip(*students_data))
min_vals = [min(col) for col in columns]
max_vals = [max(col) for col in columns]

normalized_data = []
for row in students_data:
    norm_row = []
    for i in range(len(row)):
        if max_vals[i] - min_vals[i] == 0:
            norm_val = 0
        else:
            norm_val = (row[i] - min_vals[i]) / (max_vals[i] - min_vals[i])
        norm_row.append(norm_val)
    normalized_data.append(norm_row)

# ======= Step 2: Weighted prediction =======
# Assign weights to features (sum = 1)
weights = [0.4, 0.2, 0.1, 0.3]  # Past %, Attendance %, Study Hours, Internal Marks

predicted_marks = []
for row in normalized_data:
    mark = sum([row[i]*weights[i] for i in range(len(row))]) * max_marks
    predicted_marks.append(mark)

# ======= Step 3: Print results =======
for i, row in enumerate(students_data):
    print(f"Student {i+1} Inputs: {row}")
    print(f"Normalized Inputs: {[round(x,2) for x in normalized_data[i]]}")
    print(f"Predicted Marks: {predicted_marks[i]:.2f}\n")

# ======= Step 4: Plot graph =======
plt.figure(figsize=(10,6))
student_ids = [f"S{i+1}" for i in range(len(students_data))]
plt.bar(student_ids, predicted_marks, color='skyblue')
plt.xlabel("Students")
plt.ylabel("Predicted Marks")
plt.title("Predicted Marks with Weighted Features")
plt.ylim(0, max_marks + 5)
plt.show()
