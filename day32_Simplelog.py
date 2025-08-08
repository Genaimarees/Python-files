import streamlit as st
from datetime import datetime
import os

st.title("📝 Simple Daily Log")

LOG_FILE = "daily_log.txt"

# Activity input
activity = st.text_area("Enter your daily activity:")

# Save button
if st.button("Save Activity"):
    if activity.strip():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {activity.strip()}\n")
        st.success("✅ Activity saved successfully!")
    else:
        st.warning("⚠ Please enter some activity before saving.")

# Display log history
st.subheader("📜 Activity Log History")
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = f.read().strip()

    if logs:
        st.text(logs)
    else:
        st.info("No activities logged yet.")
else:
    st.info("No activities logged yet.")
