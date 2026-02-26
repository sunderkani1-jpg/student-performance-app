import matplotlib.pyplot as plt
print("Program started")

# ======= Student Data =======
# Each student: [Past %, Attendance %, Study Hours/Week, Internal Marks]
students_data = [
    [95, 88, 18, 42],
    [78, 92, 20, 50],
    [65, 70, 10, 35],
    [80, 85, 15, 40]
]

# ======= Feature Ranges =======
feature_max = [100, 100, 30, 50]  # Past %, Attendance %, Study Hours, Internal Marks
feature_min = [0, 0, 0, 0]

# ======= Normalize Inputs =======
normalized_data = []
for row in students_data:
    norm_row = [(row[i]-feature_min[i])/(feature_max[i]-feature_min[i]) for i in range(len(row))]
    normalized_data.append(norm_row)

# ======= Weighted Prediction =======
weights = [0.5, 0.1, 0.1, 0.3]  # Past %, Attendance %, Study Hours, Internal Marks

# Calculate max weighted sum for scaling
max_weighted_sum = sum([feature_max[i]*weights[i] for i in range(len(weights))])

max_marks = 85
predicted_marks = []
for row in students_data:
    weighted_sum = sum([row[i]*weights[i] for i in range(len(row))])
    mark = (weighted_sum / max_weighted_sum) * max_marks
    predicted_marks.append(mark)

# ======= Print Results =======
for i, row in enumerate(students_data):
    print(f"Student {i+1} Inputs: {row}")
    print(f"Normalized Inputs: {[round(x,2) for x in normalized_data[i]]}")
    print(f"Predicted Marks: {predicted_marks[i]:.2f}\n")

# ======= Plot Graph =======
plt.figure(figsize=(10,6))
student_ids = [f"S{i+1}" for i in range(len(students_data))]
plt.bar(student_ids, predicted_marks, color='skyblue')
plt.xlabel("Students")
plt.ylabel("Predicted Marks")
plt.title("Predicted Marks with Weighted Features & Fixed Ranges")
plt.ylim(0, max_marks + 5)
plt.show()

