import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Page Title
st.title("Student Academic Performance Prediction")

# Load Dataset
data = pd.read_excel("student database final.xlsx")

# Features & Target
X = data[["past_semester_percentage",
          "attendance_percentage",
          "study_hours_per_week",
          "internal_marks"]]

y = data["final_marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# User Input Section
st.header("Enter Student Details")

past = st.number_input("past_semester_percentage")
attendance = st.number_input("attendance_percentage")
study = st.number_input("Study_hours_per_week")
internal = st.number_input("internal_marks")

# Prediction Button
if st.button("Predict"):
    input_data = [[past, attendance, study, internal]]
    prediction = model.predict(input_data)

    # Limit output
    final_marks = max(0, min(100, prediction[0]))

    st.success(f"Predicted Final Marks: {final_marks:.2f}")

    if final_marks < 50:
        st.error("Status: At Risk")
    else:
        st.info("Status: Safe")

# Predict Button
if st.button("Predict",key="predict_button_1"):
    prediction = model.predict([[study_hours, attendance]])
    
    st.write("Predicted Mark:", prediction[0])

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.bar(["Predicted"], [prediction[0]])
    st.pyplot(fig)



