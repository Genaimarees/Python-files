
import streamlit as st
import os

st.title("🏆 High Score Tracker")

FILE_PATH = "highscores.txt"

# Input for name and score
name = st.text_input("Enter player name:")
score = st.number_input("Enter score:", min_value=0, step=1)

# Save score button
if st.button("Save Score"):
    if name.strip():
        with open(FILE_PATH, "a") as f:
            f.write(f"{name.strip()},{score}\n")
        st.success(f"✅ Saved score for {name}!")
    else:
        st.warning("⚠ Please enter a valid name.")

# Load and display high scores
st.subheader("📋 High Scores")
if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r") as f:
        scores = [line.strip().split(",") for line in f if line.strip()]
    
    if scores:
        # Convert score to int and sort descending
        scores = [(n, int(s)) for n, s in scores]
        scores.sort(key=lambda x: x[1], reverse=True)

        # Display as a table
        st.table({"Player": [n for n, _ in scores], "Score": [s for _, s in scores]})
    else:
        st.info("No scores saved yet.")
else:
    st.info("No scores saved yet.")
