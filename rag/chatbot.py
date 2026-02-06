# rag/chatbot.py

import streamlit as st
import google.generativeai as genai


class ResumeChatbot:
    def __init__(self, resume_text: str):
        self.resume_text = resume_text

        # Configure Gemini API
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

        # Use stable model
        self.model = genai.GenerativeModel("gemini-1.0-pro")

    def ask(self, question: str) -> str:
        prompt = f"""
You are a helpful career assistant.

Answer ONLY using the resume below.
If the answer is not present, say:
"Not mentioned in the resume."

====================
RESUME:
{self.resume_text}
====================

Question:
{question}
"""

        response = self.model.generate_content(prompt)
        return response.text
