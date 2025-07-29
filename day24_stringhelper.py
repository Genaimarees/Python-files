import streamlit as st

# --- Helper Functions ---
def capitalize_text(text):
    return text.upper()

def reverse_text(text):
    return text[::-1]

def count_characters(text):
    return len(text.replace(" ", ""))

# --- Streamlit UI ---
st.set_page_config(page_title="String Helper", page_icon="🔤")

st.title("🔤 String Helper Tool")
st.write("This tool helps you with string operations like capitalization, reversing, and character counting.")

# --- User Input ---
user_input = st.text_input("Enter a string")

if st.button("Process"):
    st.subheader("Results:")
    
    st.write(f"🔠 Capitalized: `{capitalize_text(user_input)}`")
    st.write(f"🔁 Reversed: `{reverse_text(user_input)}`")
    st.write(f"🔢 Character Count (no spaces): `{count_characters(user_input)}`")
