# 📘 Job Application Assistant Bot – Project Documentation

## 1. Problem Statement
Students often apply to multiple jobs but struggle to customize their resumes according to each job description. This leads to low match rates and missed opportunities.

## 2. Solution
We built an AI-powered chatbot that analyzes resumes and job descriptions using NLP and Retrieval-Augmented Generation (RAG).  
The system identifies missing skills, compares profiles, and provides personalized improvement suggestions.

---

## 3. System Architecture

User → Streamlit UI → Resume Processing → Skill Extraction → Embeddings → Vector DB → LLM → Response

---

## 4. Workflow

1. User uploads resume (PDF)
2. Text is extracted
3. Skills are identified using NLP
4. Job description is processed
5. Resume & JD are compared
6. Embeddings are stored in ChromaDB
7. LangChain retrieves relevant chunks
8. OpenAI generates personalized suggestions

---

## 5. Modules

### Frontend
- Streamlit interface
- File upload
- Chat interface

### Backend
- Resume text extraction (PyPDF)
- Skill extraction (spaCy / NLP)
- Matching logic (scikit-learn)

### RAG Pipeline
- LangChain for document chaining
- ChromaDB for vector storage
- OpenAI API for answer generation

---

## 6. Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- OpenAI API
- spaCy / scikit-learn

---

## 7. Features

- Resume upload
- Job description summarization
- Skill extraction
- Missing skills detection
- Match score calculation
- Context-aware AI chatbot

---

## 8. Folder Structure

