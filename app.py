import streamlit as st
import pdfplumber
import re
from modules.chatbot import career_chat
from modules.recommender import recommend_jobs
st.sidebar.title("AI Career Assistant 🚀")

st.sidebar.markdown("""
### Features
✅ Resume Analysis  
✅ AI Career Chatbot  
✅ Job Recommendations  
""")

# Role-based skills
roles = {
    "Data Scientist": ["python", "machine learning", "pandas", "numpy", "deep learning", "statistics"],
    "Software Engineer": ["java", "c++", "data structures", "algorithms", "sql", "system design"],
    "Web Developer": ["html", "css", "javascript", "react", "nodejs"],
    "Data Analyst": ["excel", "sql", "power bi", "tableau", "data visualization"],
    "AI Engineer": ["python", "deep learning", "nlp", "tensorflow", "pytorch"]
}

# Keywords
keywords = ["project", "internship", "experience", "certification", "research", "development"]

# App title
st.title("🚀 AI Career Assistant")

st.markdown("""
Analyze resumes, get AI career guidance,
and discover best-fit job roles instantly.
""")

# Role selection
role = st.selectbox("Select Job Role", list(roles.keys()))

# Function: Extract text from PDF
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Function: Clean text (no spaCy)
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove special characters
    return text

# Function: Extract skills
def extract_skills(text, role):
    skills = roles[role]
    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return found

# Function: Calculate score
def calculate_score(skills, role):
    total_skills = len(roles[role])
    score = (len(skills) / total_skills) * 100
    return round(score, 2)

# Function: Detect keywords
def detect_keywords(text):
    found_keywords = []

    for word in keywords:
        if word in text:
            found_keywords.append(word)

    return found_keywords

# Function: Suggestions
def get_suggestions(found_skills, role):
    required_skills = roles[role]
    missing_skills = list(set(required_skills) - set(found_skills))

    suggestions = []
    for skill in missing_skills:
        suggestions.append(f"Add {skill} to improve your resume")

    return suggestions

# Upload file
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume Uploaded Successfully!")

    # Extract & process
    text = extract_text(uploaded_file)
    clean_text = preprocess_text(text)

    # Skills & keywords
    skills = extract_skills(clean_text, role)
    found_keywords = detect_keywords(clean_text)

    # Score
    skill_score = calculate_score(skills, role)
    keyword_score = len(found_keywords) * 5
    final_score = min(skill_score + keyword_score, 100)

    # Suggestions
    suggestions = get_suggestions(skills, role)

    # ===== DISPLAY =====
    st.markdown("## 📊 Analysis Result")

    # Skills
    st.subheader("📌 Skills Detected")
    if skills:
        for skill in skills:
            st.write(f"✅ {skill}")
    else:
        st.write("No relevant skills found")

    # Score
    st.subheader("📊 Resume Score")
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Resume Score", f"{final_score}%")

    with col2:
        st.metric("Skills Found", len(skills))
        st.progress(int(final_score))

    # Feedback
    if final_score > 80:
        st.success("Excellent Resume!")
    elif final_score > 50:
        st.warning("Good, but can improve.")
    else:
        st.error("Needs improvement.")

    # Keywords
    st.subheader("🔍 Keywords Found")
    st.write(found_keywords if found_keywords else "No important keywords found")

    # Suggestions
    st.subheader("💡 Suggestions")
    if suggestions:
        for s in suggestions:
            st.write(f"🔹 {s}")
    else:
        st.write("Great! Your resume matches the role well.")

    # Raw text
    with st.expander("Show Raw Text"):
        st.write(text)

    # Cleaned text
    with st.expander("Processed Resume Text"):
        st.write(clean_text)
    # ================= CHATBOT =================

    st.markdown("## 🤖 AI Career Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_input(
        "Ask career-related questions:"
    )

    if st.button("Ask AI"):

        if user_question:

            with st.spinner("AI is thinking..."):

                answer = career_chat(user_question, text)

            st.session_state.chat_history.append(
                ("You", user_question)
            )

            st.session_state.chat_history.append(
                ("AI", answer)
            )

    # Display chat history
    for sender, message in st.session_state.chat_history:

        st.write(f"**{sender}:** {message}")
    # ================= JOB RECOMMENDATION =================

    st.markdown("## 💼 Recommended Jobs")

    recommended_jobs = recommend_jobs(clean_text)

    for job, score in recommended_jobs:

        match_percent = round(score * 100, 2)

        st.write(
            f"✅ {job} — Match Score: {match_percent}%"
    )

        st.progress(min(score, 1.0))