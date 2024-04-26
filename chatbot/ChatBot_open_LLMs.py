from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant please respond to the use queries'),
        ('user','Question: {Question}')
    ]
)


st.title("ChatBot using LLAMA3 using langchain")
input_text = st.text_input("Search anything you want")

llm = Ollama(model='llama3')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"Question":input_text}))