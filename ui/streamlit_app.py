import streamlit as st
import requests

st.set_page_config(page_title="Document Extractor")

st.title("Intelligent Document Extraction Platform")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    with st.spinner("Processing document..."):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/extract",
                files={
                    "file": (
                        uploaded_file.name,
                        uploaded_file,
                        uploaded_file.type
                    )
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Extraction completed")

                st.json(data)

            else:
                st.error("Backend error")

        except Exception as e:

            st.error(f"Error: {e}")