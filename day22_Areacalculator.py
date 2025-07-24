import streamlit as st
import math

# Set Streamlit page title
st.set_page_config(page_title="📏 Area Calculator", layout="centered")
st.title("📐 Area Calculator")

# Dropdown to choose shape
shape = st.selectbox("Choose a shape", ["Circle", "Rectangle", "Triangle"])

# Area calculation based on shape
if shape == "Circle":
    radius = st.number_input("Enter radius", min_value=0.0, format="%.2f")
    
    if st.button("Calculate Area"):
        area = math.pi * radius ** 2
        st.success(f"Area of the circle is: {area:.2f} square units")

elif shape == "Rectangle":
    length = st.number_input("Enter length", min_value=0.0, format="%.2f")
    width = st.number_input("Enter width", min_value=0.0, format="%.2f")

    if st.button("Calculate Area"):
        area = length * width
        st.success(f"Area of the rectangle is: {area:.2f} square units")

elif shape == "Triangle":
    base = st.number_input("Enter base", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height", min_value=0.0, format="%.2f")
