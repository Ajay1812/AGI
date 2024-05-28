import streamlit as st

st.set_page_config(page_title="RAG Chat Application using local LLM ")

st.title("RAG Chat Application using local LLM")

st.file_uploader("Upload your file here ",type='.pdf')