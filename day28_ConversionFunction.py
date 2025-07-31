import streamlit as st

# Title
st.title("📏 Unit Conversion Tool")

# Sidebar - Unit selection
conversion_type = st.sidebar.selectbox(
    "Choose conversion type",
    ("Feet to Meters", "Meters to Feet",
     "Pounds to Kilograms", "Kilograms to Pounds",
     "Celsius to Fahrenheit", "Fahrenheit to Celsius")
)

# Input
value = st.number_input("Enter the value to convert", format="%.4f")

# Conversion Logic
def convert_units(value, conversion_type):
    if conversion_type == "Feet to Meters":
        return value * 0.3048
    elif conversion_type == "Meters to Feet":
        return value / 0.3048
    elif conversion_type == "Pounds to Kilograms":
        return value * 0.453592
    elif conversion_type == "Kilograms to Pounds":
        return value / 0.453592
    elif conversion_type == "Celsius to Fahrenheit":
        return (value * 9/5) + 32
    elif conversion_type == "Fahrenheit to Celsius":
        return (value - 32) * 5/9

# Output
if value:
    result = convert_units(value, conversion_type)
    st.success(f"{value} converted is: {result:.4f}")
