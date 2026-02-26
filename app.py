import streamlit as st
import matplotlib.pyplot as plt

st.title("Student Mark Prediction")

past = st.number_input("Past Semester %", 0, 100)
attendance = st.number_input("Attendance %", 0, 100)
study = st.number_input("Study Hours per Week", 0, 30)
internal = st.number_input("Internal Marks (out of 50)", 0, 50)

if st.button("Predict"):

    # Weights
    weights = [0.5, 0.1, 0.1, 0.3]
    max_values = [100, 100, 30, 50]
    max_marks = 85

    inputs = [past, attendance, study, internal]

    weighted_sum = sum([inputs[i]*weights[i] for i in range(len(inputs))])
    max_weighted_sum = sum([max_values[i]*weights[i] for i in range(len(weights))])

    predicted_mark = (weighted_sum / max_weighted_sum) * max_marks

    st.success(f"Predicted Marks: {round(predicted_mark,2)}")

    # Risk Status
    if predicted_mark >= 70:
        st.info("Low Risk ✅")
    elif predicted_mark >= 50:
        st.warning("Moderate Risk ⚠️")
    else:
        st.error("High Risk ❌")

    # Graph
    fig, ax = plt.subplots()
    ax.bar(["Predicted"], [predicted_mark])
    ax.set_ylim(0, 90)
    ax.set_ylabel("Marks")
    st.pyplot(fig)
