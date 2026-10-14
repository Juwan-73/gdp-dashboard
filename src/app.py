import streamlit as st

st.set_page_config(
    page_title="🎓 Student Grade Checker",
    page_icon="🎓",
    layout="centered"
)
st.title("🎓 Student Grade Checker")
st.write("Welcome! Enter your details and marks below to calculate your results.")
st.divider()

st.subheader("Enter Your Marks")
st.caption("Choose the number of subjects then enter each mark out of 100.")

col1, col2 =st.columns(2)
with col1:
    name = st.text_input("Enter Your Name")
                         
with col2:
    num_subjects = st.number_input(
    "Number of subjects", min_value=1,
  max_value=10, value=3
)

marks = []

for i in range(num_subjects):
    mark = st.number_input(f"Subject {i + 1}", 0, 100)
    marks.append(mark)
st.divider()

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
    
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Marks", f"{total}/{len(marks) * 100}")
    col2.metric("Average", round(average, 2))
    col3.metric("Grade", grade)
    
    if status == "Excellent":
        st.success(f"Status: {status}")
    elif status == "Good":
        st.info(f"Status: {status}")
    else:
        st.warning(f"Status: {status}")