import streamlit as st

st.title("🎓 Student Grade Checker")

name = st.text_input("Enter your name")

math = st.number_input("Mathematics", 0, 100)
python = st.number_input("Python", 0, 100)
statistics = st.number_input("Statistics", 0, 100)
marks = [math, python, statistics]
if st.button("Calculate Grade"):

    total = sum(marks)
    average = total / len(marks)

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "E"
    if average >= 70:
        status = "Excellent"
    elif average >= 50:
        status = "Good"
    else:
        status = "Needs Improvement"

    st.subheader(f"{name}'s Results")
    st.write("Total:", total, f"/{300}")
    st.write("Average:", round(average, 2))
    st.write("Grade:", grade)
    st.write("Status:", status)
