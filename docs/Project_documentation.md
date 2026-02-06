# 📘 Job Application Assistant Bot – Project Documentation

## 1. Problem Statement
Students and fresh graduates often apply to multiple jobs without tailoring their resumes to specific job descriptions. This results in low resume–job match scores and reduced chances of shortlisting.

## 2. Solution
This project implements an AI-powered Job Application Assistant Bot that analyzes resumes and job descriptions using Natural Language Processing (NLP) and Retrieval-Augmented Generation (RAG).  
The system identifies skill gaps, compares profiles, and provides personalized improvement suggestions through an interactive chatbot.

---

## 3. System Architecture

User → Streamlit UI → Resume Processing → Skill Extraction → Embeddings → FAISS Vector Store → LLM (Gemini) → Response

---

## 4. Workflow

1. User uploads a resume in PDF format
2. Resume text is extracted and cleaned
3. Skills are identified using NLP techniques
4. Job description is processed similarly
5. Resume and job description are compared
6. Text embeddings are generated
7. Embeddings are stored in FAISS
8. Relevant context is retrieved using RAG
9. LLM generates personalized suggestions and chatbot responses

---

## 5. Modules

### Frontend
- Streamlit-based web interface
- Resume upload functionality
- Interactive chatbot UI

### Backend
- PDF text extraction
- Skill extraction using NLP
- Resume–job matching logic

### RAG Pipeline
- Embedding generation
- FAISS for vector storage and similarity search
- LLM (Google Gemini) for response generation

---

## 6. Tech Stack

- Python
- Streamlit
- NLP
- RAG
- FAISS (Vector Search)
- Google Gemini / LLM APIs

---

## 7. Features

- Resume upload (PDF)
- Job description analysis
- Skill extraction and comparison
- Missing skill recommendations
- Resume–job match insights
- Context-aware AI chatbot

---
## 8. Folder Structure

Job-Application-Assistant-Bot/
│
├── app.py                  
├── utils/
│   ├── pdf_reader.py           
│        
├── nlp/
│   ├── skill_extractor.py    
│   
├── rag/
│   └── chatbot.py              

├── requirements.txt           
├── README.md                   
├── PROJECT_DOCUMENTATION.md    
└── .gitignore                

