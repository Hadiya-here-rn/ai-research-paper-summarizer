print("✅ App started loading")

import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text

# Set Streamlit page config
st.set_page_config(
    page_title="AI Research Paper Summarizer",
    page_icon="🧠",
    layout="centered"
)

# Sidebar for credits or instructions
with st.sidebar:
    st.markdown("## ℹ️ How to Use")
    st.markdown(
        """
        1. Upload a research paper in PDF format  
        2. The app will extract the text  
        3. Click to generate a summary  
        4. Download the summary if desired  
        """
    )
    st.markdown("---")
    st.markdown("Built with ❤️ using GPT-4, LangChain, and PyMuPDF")

# App Title
st.title("📄 AI Research Paper Summarizer")

# File uploader
uploaded_file = st.file_uploader("📤 Upload a PDF", type=["pdf"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    with st.spinner("🔍 Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    if text:
        st.info(f"📃 Extracted approximately {len(text.split())} words.")
        st.text_area("🔎 Preview Extracted Text", value=text[:1000] + "...", height=200)

        if st.button("🧠 Generate Summary"):
            with st.spinner("✍️ Summarizing..."):
                summary = summarize_text(text)

            st.success("✅ Summary generated!")
            st.subheader("📌 Summary")
            st.write(summary)

            st.download_button(
                label="💾 Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )
    else:
        st.error("❌ No readable text found in the PDF.")
else:
    st.markdown("👆 Please upload a PDF file to begin.")

# Optional footer
st.markdown("---")
st.markdown(
    "<center><small>© 2025 AI Research Tools</small></center>",
    unsafe_allow_html=True
)
