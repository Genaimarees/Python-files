import streamlit as st

# --- Helper Functions ---
def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_sum(numbers):
    return sum(numbers)

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# --- Streamlit UI ---
st.set_page_config(page_title="List Helper", page_icon="📋")

st.title("📋 List Helper Tool")
st.write("Enter a list of numbers and get Max, Min, Sum, and Average.")

# --- User Input ---
user_input = st.text_input("Enter numbers separated by commas (e.g. 1, 2, 3, 4)")

if st.button("Process List"):
    try:
        numbers = [float(num.strip()) for num in user_input.split(",") if num.strip() != ""]
        if numbers:
            st.subheader("Results:")
            st.write(f"🔼 Max: {find_max(numbers)}")
            st.write(f"🔽 Min: {find_min(numbers)}")
            st.write(f"➕ Sum: {find_sum(numbers)}")
            st.write(f"🧮 Average: {find_average(numbers)}")
        else:
            st.warning("⚠️ Please enter at least one number.")
    except ValueError:
        st.error("❌ Invalid input. Please enter only numbers separated by commas.")
