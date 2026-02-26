import matplotlib.pyplot as plt

# ======= Inputs =======
inputs = [95, 88, 18, 42]  # your input values
min_val = min(inputs)
max_val = max(inputs)

# ======= Step 1: Normalize inputs =======
normalized_inputs = [(x - min_val)/(max_val - min_val) for x in inputs]

# ======= Step 2: Define prediction function =======
# Example: predicted marks proportional to normalized input
def predict_marks(normalized_values, max_marks=85):
    return [x * max_marks for x in normalized_values]

predicted_marks = predict_marks(normalized_inputs)

# ======= Step 3: Print results =======
print("Inputs:", inputs)
print("Normalized Inputs:", normalized_inputs)
print("Predicted Marks:", predicted_marks)

# ======= Step 4: Plot graph =======
plt.figure(figsize=(8,5))
plt.bar(range(len(inputs)), predicted_marks, tick_label=inputs, color='skyblue')
plt.xlabel("Input Values")
plt.ylabel("Predicted Marks")
plt.title("Input vs Predicted Marks")
plt.show()
