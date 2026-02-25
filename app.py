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
st.write("Final Marks Sample:", df["final_marks"].head())
st.write("Final Marks Max:", df["final_marks"].max())

# ---- USER INPUT ----
past_semester = st.number_input("Past Semester %")
attendance = st.number_input("Attendance %")
study_hours = st.number_input("Study Hours")
internal_marks = st.number_input("Internal Marks")

# ---- ONE Predict BUTTON ----

import pandas as pd

input_data = pd.DataFrame([{
    "past_semester_percentage": past_semester/100,
    "attendance_percentage": attendance/100,
    "study_hours_per_week": study_hours,
    "internal_marks": internal_marks
}])

prediction = model.predict(input_data)

st.write("Predicted Mark:", prediction[0])
    # ----- GRAPH -----
    fig, ax = plt.subplots()
    ax.bar(["Predicted Marks"], [prediction[0]])
    ax.set_ylabel("Marks")
    ax.set_ylim(0, 100)
    st.pyplot(fig)






