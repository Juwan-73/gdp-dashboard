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

    st.subheader("Your Results")
    st.write("Name:", name)
    st.write("Total:", total)
    st.write("Average:", round(average, 2))
    st.write("Grade:", grade)