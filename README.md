# Job Application Assistant Bot 🚀

An AI-powered chatbot that helps students and job seekers improve their resumes and job applications using NLP and Retrieval-Augmented Generation (RAG).

## Features
- Resume upload (PDF format)
- Job description summarization
- Resume–job skill matching
- Missing skill recommendations
- Interactive chatbot assistant
- Streamlit-based web interface

## Tech Stack
- Python
- Streamlit (Web UI)
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG)
- Google Gemini / LLM APIs
- Vector Search (FAISS)

## How It Works
1. User uploads a resume (PDF)
2. Job description is analyzed using NLP
3. Skills are extracted and compared
4. Missing or weak skills are suggested
5. Chatbot answers job-related queries using RAG

**Flow:** Streamlit UI → Resume Parser → NLP & Skill Extraction → FAISS Vector Store → RAG Engine → LLM → User Output

## Run Locally
```bash
# Activate virtual environment
venv\Scripts\activate

# Run the application
streamlit run app.py
