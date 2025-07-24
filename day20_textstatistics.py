import streamlit as st
import re

# Page config
st.set_page_config(page_title="Text Statistics", layout="centered")

# Title
st.title("📊 Text Statistics App")

# Text input
paragraph = st.text_area("✍️ Enter your paragraph here:")

# When button is clicked
if st.button("Analyze Text"):
    if paragraph.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Count words
        word_count = len(paragraph.split())

        # Count sentences (using '.', '?', or '!')
        sentence_count = len(re.findall(r'[.!?]', paragraph))

        # Count characters (with spaces)
        char_count = len(paragraph)

        # Show results
        st.subheader("📈 Statistics:")
        st.markdown(f"**🔤 Words:** {word_count}")
        st.markdown(f"**📝 Sentences:** {sentence_count}")
        st.markdown(f"**🔡 Characters (with spaces):** {char_count}")
