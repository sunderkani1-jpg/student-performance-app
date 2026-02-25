import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_excel("student database final.xlsx")
st.write("Column Names:", df.columns)
st.write(df.head())
# Features & target
X = df[["past_semester_percentage",
        "attendance_percentage",
        "study_hours_per_week",
        "internal_marks"]]

y = df["final_marks"]

# Model create & train once
model = LinearRegression()
model.fit(X, y)

past_semester = st.number_input("Past Semester %")
attendance = st.number_input("Attendance %")
study_hours = st.number_input("Study Hours")
internal_marks = st.number_input("Internal Marks")
# 🔵 PREDICT BUTTON
if st.button("Predict"):

    input_data = pd.DataFrame([{
        "past_semester_percentage": past_semester/100,
        "attendance_percentage": attendance/100,
        "study_hours_per_week": study_hours,
        "internal_marks": internal_marks
    }])

    prediction = model.predict(input_data)

    st.session_state.prediction = prediction[0]

    st.write("Predicted Mark:", prediction[0])
        
# 🟢 SHOW GRAPH BUTTON (👇 EXACTLY HERE)
if st.button("Show Graph") and "prediction" in st.session_state:

    fig, ax = plt.subplots()
    ax.bar(["Prediction"], [st.session_state.prediction])
    st.pyplot(fig)
