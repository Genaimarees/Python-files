import streamlit as st
import math

# --- Helper Functions ---
def calculate_factorial(n):
    try:
        return math.factorial(n)
    except ValueError:
        return "❌ Invalid input (factorial only for non-negative integers)"

def calculate_power(base, exponent):
    return math.pow(base, exponent)

def calculate_sqrt(n):
    if n < 0:
        return "❌ Cannot find square root of negative number"
    return math.sqrt(n)

# --- Streamlit UI ---
st.set_page_config(page_title="Math Operation Helper", page_icon="🧮")

st.title("🧮 Math Operation Helper")
st.write("This app calculates Factorial, Power and Square Root.")

# --- Input Fields ---
operation = st.selectbox("Choose an operation", ["Factorial", "Power", "Square Root"])

if operation == "Factorial":
    num = st.number_input("Enter a number (non-negative integer)", step=1, min_value=0)
    if st.button("Calculate Factorial"):
        result = calculate_factorial(int(num))
        st.success(f"Factorial of {int(num)} is: {result}")

elif operation == "Power":
    base = st.number_input("Enter base")
    exponent = st.number_input("Enter exponent")
    if st.button("Calculate Power"):
        result = calculate_power(base, exponent)
        st.success(f"{base} raised to the power {exponent} is: {result}")

elif operation == "Square Root":
    num = st.number_input("Enter a number", step=1)
    if st.button("Calculate Square Root"):
        result = calculate_sqrt(num)
        st.success(f"Square root of {num} is: {result}")
