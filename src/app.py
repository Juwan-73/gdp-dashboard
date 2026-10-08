import streamlit as st

st.title("🎓 Student Grade Checker")

name = st.text_input("Enter your name")

num_subjects =st.number_input("Number of subjects", min_value=1, 
max_value=10, value=3)

marks = []

for i in range(num_subjects):
    mark = st.number_input(f"Subject {i + 1}", 0, 100)
    marks.append(mark)
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
    st.write("Total:", total, f"/{len(marks) * 100}")
    st.write("Average:", round(average, 2))
    st.write("Grade:", grade)
    st.write("Status:", status)
