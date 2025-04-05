import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompt import load_prompt
from dotenv import load_dotenv
import os 

load_dotenv()
auth_token = os.getenv("GOOGLE_API_KEY")

if not auth_token:
    st.error("API key is not present. Firslty see that")
    st.stop

model = ChatGoogleGenerativeAI(
      model = "gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    max_retries=3,
    api_key=auth_token,
    repetition_penalty = 1.03)

prompt = load_prompt("prompt.json",encoding='utf-8')  

st.header("ResearchExplainAI")
