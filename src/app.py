import streamlit as st

st.title("🎓 Student Grade Checker")

name = st.text_input("Enter your name")

math = st.number_input("Mathematics", 0, 100)
python = st.number_input("Python", 0, 100)
statistics = st.number_input("Statistics", 0, 100)

if st.button("Calculate Grade"):

    total = math + python + statistics
    average = total / 3

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
if average > 70 and average <= 100:
    st.write("Excellent")
elif average >= 50 and average <= 70:
    st.write("Good")
elif average < 50:
    st.write("Needs Improvement")

    st.subheader(f"{name}'s Results")
    st.write("Total:", total, "/300")
    st.write("Average:", round(average, 2))
    st.write("Grade:", grade)
    st.write("Status:", status)
