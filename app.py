import torch
import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text

st.title("📄 AI Research Paper Summarizer")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)

    if text:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)

        st.subheader("📌 Summary")
        st.write(summary)
        st.download_button("Download Summary", summary, file_name="summary.txt")
    else:
        st.error("No readable text found.")