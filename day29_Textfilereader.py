import streamlit as st

# App title
st.title("📄 Text File Reader & Counter")

# File uploader
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    # Read file content
    content = uploaded_file.read().decode("utf-8")

    # Count lines and words
    lines = content.splitlines()
    total_lines = len(lines)
    total_words = len(content.split())

    # Display results
    st.subheader("📊 File Statistics")
    st.write(f"**Total Lines:** {total_lines}")
    st.write(f"**Total Words:** {total_words}")

    # Display file content
    st.subheader("📜 File Content")
    st.text(content)
