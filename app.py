import streamlit as st
import google.generativeai as genai

# local modules
from utils.pdf_reader import read_pdf
from nlp.skill_extractor import extract_skills
from rag.chatbot import ResumeChatbot



st.title("💼 Job Application Assistant Bot")


# -------------------------
# Inputs
# -------------------------
st.header("Upload Resume")
resume_file = st.file_uploader("Resume (PDF)", type=["pdf"])

st.header("Paste Job Description")
jd_text = st.text_area("Job Description")


# -------------------------
# Resume Processing
# -------------------------
if resume_file:
    st.session_state["resume_text"] = read_pdf(resume_file)

resume_text = st.session_state.get("resume_text", None)

# -------------------------
# Skill Analysis Section
# -------------------------
# -------------------------
# Skill Analysis Section
# -------------------------

st.subheader("📊 Resume Analysis")

st.write("DEBUG resume_text exists:", resume_text is not None)
st.write("DEBUG jd_text:", jd_text)

if st.button("Analyze Resume"):

    if resume_text is not None and jd_text.strip() != "":

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        missing = list(set(jd_skills) - set(resume_skills))

        match_score = int(
            len(set(resume_skills) & set(jd_skills)) / (len(jd_skills) + 1) * 100
        )

        st.success("Resume analyzed successfully!")
        st.write("✅ Resume Skills:", resume_skills)
        st.write("📋 Job Skills:", jd_skills)
        st.write("❌ Missing Skills:", missing)
        st.write(f"🎯 Match Score: {match_score}%")

    else:
        st.warning("⚠️ Please upload resume and paste job description first.")

# -------------------------
# AI Chatbot
# -------------------------

       # -------------------------
# AI Chatbot
# -------------------------
if resume_text:

    st.header("💬 Ask AI about your Resume")

    chatbot = ResumeChatbot(resume_text)

    question = st.text_input("Ask something about your resume")

    if question:
        answer = chatbot.ask(question)
        st.write("🤖", answer)

