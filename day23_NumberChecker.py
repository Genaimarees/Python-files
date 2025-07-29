import streamlit as st

# --- Utility functions ---
def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# --- Streamlit UI ---
st.set_page_config(page_title="Number Checker", page_icon="🔢")

st.title("🔢 Number Checker")
st.write("Check if a number is positive, even, or prime.")

# --- User Input ---
number = st.number_input("Enter a number", step=1)

if st.button("Check Number"):
    st.subheader("Results:")
    st.write(f"✅ Positive: {'Yes' if is_positive(number) else 'No'}")
    st.write(f"🔁 Even: {'Yes' if is_even(number) else 'No'}")
    st.write(f"🧮 Prime: {'Yes' if is_prime(int(number)) else 'No'}")
