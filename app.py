import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ---- LOAD DATA ----
df = pd.read_excel("student database final.xlsx")

# ---- FEATURES & TARGET ----
X = df[["past_semester_percentage",
        "attendance_percentage",
        "study_hours_per_week",
        "internal_marks"]]
y = df["final_marks"]

# ---- MODEL ----
model = LinearRegression()
model.fit(X, y)  # Train once

# ---- USER INPUT ----
st.title("Student Academic Performance Prediction")
st.subheader("Enter Student Details")

past_semester = st.number_input("Past Semester % (0/100)")
attendance = st.number_input("Attendance % (0/100)")
study_hours = st.number_input("Study Hours per Week")
internal_marks = st.number_input("Internal Marks (out of 50)")

# ---- PREDICT BUTTON ----
if st.button("Predict"):
    # Input data in correct scale
    input_data = pd.DataFrame([{
        "past_semester_percentage": past_semester/100,
        "attendance_percentage": attendance/100,
        "study_hours_per_week": study_hours,
        "internal_marks": internal_marks
    }])

    prediction = model.predict(input_data)
    st.session_state.prediction = prediction[0]

    st.write("### Predicted Final Mark:", round(prediction[0], 2))

    # ---- RISK STATUS ----
    if prediction[0] >= 70:
        status = "Low Risk ✅"
    elif prediction[0] >= 50:
        status = "Moderate Risk ⚠️"
    else:
        status = "High Risk ❌"
    st.write("### Academic Risk Status:", status)

# ---- SHOW GRAPH BUTTON ----
if st.button("Show Graph") and "prediction" in st.session_state:
    fig, ax = plt.subplots()
    ax.bar(["Predicted Mark"], [st.session_state.prediction], color='skyblue')
    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")
    ax.set_title("Predicted Student Performance")
    st.pyplot(fig)

