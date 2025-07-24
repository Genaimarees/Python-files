import streamlit as st

# Page settings
st.set_page_config(page_title="📞 Phone Number Formatter", layout="centered")

# App title
st.title("📞 Phone Number Formatter")

# User input
phone_input = st.text_input("Enter a 10-digit phone number (digits only):")

# Button to format
if st.button("Format Phone Number"):
    if phone_input.isdigit() and len(phone_input) == 10:
        formatted = f"{phone_input[:3]}-{phone_input[3:6]}-{phone_input[6:]}"
        st.success(f"✅ Formatted Number: {formatted}")
    else:
        st.error("❌ Please enter exactly 10 digits (only numbers).")
