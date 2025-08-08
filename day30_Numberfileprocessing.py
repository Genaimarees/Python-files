import streamlit as st

st.title("🔢 Number File Processing")

# File uploader
uploaded_file = st.file_uploader("Upload a file with numbers", type=["txt"])

if uploaded_file is not None:
    try:
        # Read and decode file
        content = uploaded_file.read().decode("utf-8")

        # Extract numbers (allow spaces, commas, or new lines)
        numbers = []
        for part in content.replace(",", " ").split():
            if part.strip().replace(".", "", 1).isdigit():  # Handles floats
                numbers.append(float(part))

        if numbers:
            total_sum = sum(numbers)
            average = total_sum / len(numbers)

            st.subheader("📊 Results")
            st.write(f"**Total Numbers:** {len(numbers)}")
            st.write(f"**Sum:** {total_sum}")
            st.write(f"**Average:** {average}")

            st.subheader("📄 Numbers in File")
            st.write(numbers)
        else:
            st.error("❌ No valid numbers found in the file.")
    except Exception as e:
        st.error(f"Error reading file: {e}")
