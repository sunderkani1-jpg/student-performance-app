import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1️⃣ Load dataset
data = pd.read_excel("student database final.xlsx")  # exact file name
print(data.head())  # optional – check table
print(data['student_id'].values)  # optional – check IDs

# 2️⃣ Prepare features & target
X = data[['past_semester_percentage', 'attendance_percentage', 'study_hours_per_week', 'internal_marks']]
y = data['final_marks']

# 3️⃣ Split & train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 4️⃣ Check model accuracy
print("R2 Score:", model.score(X_test, y_test))

# 5️⃣ Predict for a real student by ID
student_id = "S00011"  # exact match dataset
student_data = data[data['student_id'] == student_id]

if student_data.empty:
    print("Student ID not found!")
else:
    X_new = student_data[['past_semester_percentage','attendance_percentage','study_hours_per_week','internal_marks']]
    predicted_mark = model.predict(X_new)
    print("Student Name:", student_data['name'].values[0])
    print("Actual Final Mark:", student_data['final_marks'].values[0])
    print("Predicted Final Mark:", predicted_mark[0])

# 6️⃣ At-Risk Identification
data['Predicted_Marks'] = model.predict(data[['past_semester_percentage','attendance_percentage','study_hours_per_week','internal_marks']])
data['Risk_Status'] = data['Predicted_Marks'].apply(lambda x: "At Risk" if x < 50 else "Safe")

# 7️⃣ Grade System
def grade(score):
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Fail"

data['grade'] = data['Predicted_Marks'].apply(grade)

# 8️⃣ Grade distribution graph
data['grade'].value_counts().plot(kind='bar')
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()