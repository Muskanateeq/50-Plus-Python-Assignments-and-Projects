import streamlit as st

# Set the title of the web app
st.title("BMI Calculator")

# Brief description
st.write("Enter your weight and height below to calculate your Body Mass Index (BMI).")

# Input fields for weight (in kg) and height (in m)
weight = st.number_input("Weight (kg):", min_value=0.0, step=0.1)
height = st.number_input("Height (m):", min_value=0.0, step=0.01)

# When the "Calculate BMI" button is pressed, compute and display the BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: **{bmi:.2f}**")
        
        # Display BMI category
        if bmi < 18.5:
            st.write("Category: Underweight")
        elif bmi < 24.9:
            st.write("Category: Normal weight")
        elif bmi < 29.9:
            st.write("Category: Overweight")
        else:
            st.write("Category: Obese")
    else:
        st.error("Please enter a valid height greater than 0.")
