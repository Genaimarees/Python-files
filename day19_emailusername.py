import streamlit as st

# Streamlit page settings
st.set_page_config(page_title="Email Username Extractor", layout="centered")

# App Title
st.title("📧 Email Username Extractor")

# User Input
email = st.text_input("Enter your email address:")

# Button to extract username
if st.button("Extract Username"):
    if "@" in email:
        username = email.split('@')[0]
        st.success(f"✅ Username extracted: **{username}**")
    else:
        st.error("❌ Please enter a valid email address (with '@').")
