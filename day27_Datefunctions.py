import streamlit as st
from datetime import datetime

# --- Helper Functions ---
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(dob):
    today = datetime.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

# --- Streamlit UI ---
st.set_page_config(page_title="Date Functions", page_icon="📅")

st.title("📅 Date Functions Tool")
st.write("Check if a year is a leap year and calculate your age from date of birth.")

# --- Leap Year Checker ---
st.subheader("🔄 Leap Year Checker")
year = st.number_input("Enter a year", min_value=1, step=1)

if st.button("Check Leap Year"):
    if is_leap_year(int(year)):
        st.success(f"✅ {int(year)} is a Leap Year!")
    else:
        st.warning(f"❌ {int(year)} is NOT a Leap Year.")

# --- Age Calculator ---
st.subheader("🎂 Age Calculator")
dob = st.date_input("Select your Date of Birth")

if st.button("Calculate Age"):
    age = calculate_age(dob)
    st.success(f"🎉 Your age is: {age} years")
