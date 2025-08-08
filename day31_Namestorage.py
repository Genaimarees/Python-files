import streamlit as st
import os

st.title("📝 Name Storage App")

# File to store names
FILE_PATH = "names.txt"

# Input for name
name = st.text_input("Enter a name:")

# Save name button
if st.button("Save Name"):
    if name.strip():  # Avoid saving empty names
        with open(FILE_PATH, "a") as f:
            f.write(name.strip() + "\n")
        st.success(f"✅ Name '{name}' saved successfully!")
    else:
        st.warning("⚠ Please enter a valid name.")

# Display saved names
st.subheader("📋 Saved Names")
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        names_list = f.read().strip().split("\n")
    
    if names_list and names_list[0] != "":
        for idx, saved_name in enumerate(names_list, start=1):
            st.write(f"{idx}. {saved_name}")
    else:
        st.info("No names stored yet.")
else:
    st.info("No names stored yet.")
