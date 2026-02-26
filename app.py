import matplotlib.pyplot as plt

# ======= Student Data =======
# Each student: [Past %, Attendance %, Study Hours/Week, Internal Marks]
students_data = [
    [95, 88, 18, 42],
    [78, 92, 20, 50],
    [65, 70, 10, 35],
    [80, 85, 15, 40]
]

# ======= Step 1: Define fixed ranges for each feature =======
feature_max = [100, 100, 30, 50]  # Past %, Attendance %, Study Hours, Internal Marks
feature_min = [0, 0, 0, 0]

# ======= Step 2: Normalize using fixed range =======
normalized_data = []
for row in students_data:
    norm_row = [(row[i]-feature_min[i])/(feature_max[i]-feature_min[i]) for i in range(len(row))]
    normalized_data.append(norm_row)

# ======= Step 3: Weighted prediction =======
# Assign weights (sum = 1)
weights = [0.5, 0.1, 0.1, 0.3]  # more weight to Past % and Internal Marks

# Calculate max weighted sum for scaling
max_weighted_sum = sum([weights[i]*feature_max[i] for i in range(len(weights))])

# Predict marks scaled to max 85
max_marks = 85
predicted_marks = []
for row in students_data:
    weighted_sum = sum([row[i]*weights[i] for i in range(len(row))])
    mark = (weighted_sum / max_weighted_sum) * max_marks
    predicted_marks.append(mark)

# ======= Step 4: Print results =======
for i, row in enumerate(students_data):
    print(f"Student {i+1} Inputs: {row}")
    print(f"Normalized Inputs: {[round(x,2) for x in normalized_data[i]]}")
    print(f"Predicted Marks: {predicted_marks[i]:.2f}\n")

# ======= Step 5: Plot graph =======
plt.figure(figsize=(10,6))
student_ids = [f"S{i+1}" for i in range(len(students_data))]
plt.bar(student_ids, predicted_marks, color='skyblue')
plt.xlabel("Students")
plt.ylabel("Predicted Marks")
plt.title("Predicted Marks with Fixed Ranges & Proper Weights")
plt.ylim(0, max_marks + 5)
plt.show()
