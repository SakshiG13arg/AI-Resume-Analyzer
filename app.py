import streamlit as st
import pdfplumber
import re

from modules.interview_evaluator import evaluate_answer
from modules.roadmap import generate_roadmap
from modules.skill_gap import (
    analyze_skill_gap,
    get_learning_priority
)
from modules.chatbot import career_chat
from modules.recommender import recommend_jobs
from modules.jd_matcher import (
    calculate_match_score,
    find_missing_skills
)
from modules.interview import generate_question
from modules.cover_letter import generate_cover_letter

# ================= SIDEBAR =================

st.sidebar.title("AI Career Assistant 🚀")

st.sidebar.markdown("""
### Features

✅ Resume Analysis

✅ AI Career Chatbot

✅ Job Recommendations

✅ JD Matcher
                    
🎤 Mock Interview
                    
📄 Cover Letter Generator
""")

# ================= ROLE DATA =================

roles = {
    "Data Scientist": [
        "python",
        "machine learning",
        "pandas",
        "numpy",
        "deep learning",
        "statistics"
    ],

    "Software Engineer": [
        "java",
        "c++",
        "data structures",
        "algorithms",
        "sql",
        "system design"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "nodejs"
    ],

    "Data Analyst": [
        "excel",
        "sql",
        "power bi",
        "tableau",
        "data visualization"
    ],

    "AI Engineer": [
        "python",
        "deep learning",
        "nlp",
        "tensorflow",
        "pytorch"
    ]
}

keywords = [
    "project",
    "internship",
    "experience",
    "certification",
    "research",
    "development"
]

# ================= TITLE =================

st.title("🚀 AI Career Assistant")

st.markdown("""
Analyze resumes, get AI career guidance,
and discover best-fit job roles instantly.
""")

# ================= ROLE =================

role = st.selectbox(
    "Select Job Role",
    list(roles.keys())
)

# ================= FUNCTIONS =================

def extract_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            text += page.extract_text() or ""

    return text


def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-z\s]',
        '',
        text
    )

    return text


def extract_skills(text, role):

    skills = roles[role]

    found = []

    for skill in skills:

        if skill in text:

            found.append(skill)

    return found


def calculate_score(skills, role):

    total_skills = len(
        roles[role]
    )

    score = (
        len(skills) / total_skills
    ) * 100

    return round(score, 2)


def detect_keywords(text):

    found_keywords = []

    for word in keywords:

        if word in text:

            found_keywords.append(word)

    return found_keywords


def get_suggestions(found_skills, role):

    required_skills = roles[role]

    missing_skills = list(
        set(required_skills)
        - set(found_skills)
    )

    suggestions = []

    for skill in missing_skills:

        suggestions.append(
            f"Add {skill} to improve your resume"
        )

    return suggestions


# ================= FILE UPLOAD =================

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success(
        "Resume Uploaded Successfully!"
    )

    text = extract_text(
        uploaded_file
    )

    st.session_state[
        "resume_text"
    ] = text

    clean_text = preprocess_text(
        text
    )

    skills = extract_skills(
        clean_text,
        role
    )

    found_keywords = detect_keywords(
        clean_text
    )

    skill_score = calculate_score(
        skills,
        role
    )

    keyword_score = (
        len(found_keywords) * 5
    )

    final_score = min(
        skill_score + keyword_score,
        100
    )

    suggestions = get_suggestions(
        skills,
        role
    )

    # ================= ANALYSIS =================

    st.divider()
    st.markdown(
        "## 📊 Analysis Result"
    )

    st.subheader(
        "📌 Skills Detected"
    )

    if skills:

        for skill in skills:

            st.write(
                f"✅ {skill}"
            )

    else:

        st.write(
            "No relevant skills found"
        )

    st.subheader(
        "📊 Resume Score"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Resume Score",
            f"{final_score}%"
        )

    with col2:

        st.metric(
            "Skills Found",
            len(skills)
        )

        st.progress(
            int(final_score)
        )

    if final_score > 80:

        st.success(
            "Excellent Resume!"
        )

    elif final_score > 50:

        st.warning(
            "Good, but can improve."
        )

    else:

        st.error(
            "Needs improvement."
        )

    st.subheader(
        "🔍 Keywords Found"
    )

    st.write(
        found_keywords
        if found_keywords
        else "No important keywords found"
    )

    st.subheader(
        "💡 Suggestions"
    )

    if suggestions:

        for s in suggestions:

            st.write(
                f"🔹 {s}"
            )

    else:

        st.write(
            "Great! Your resume matches the role well."
        )

    # ================= CHATBOT =================

    st.divider()
    st.markdown(
        "## 🤖 AI Career Chatbot"
    )

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    user_question = st.text_input(
        "Ask career-related questions:"
    )

    if st.button(
        "Ask AI"
    ):

        if user_question:

            with st.spinner(
                "AI is thinking..."
            ):

                answer = career_chat(
                    user_question,
                    text
                )

            st.session_state.chat_history.append(
                ("You", user_question)
            )

            st.session_state.chat_history.append(
                ("AI", answer)
            )

    for sender, message in st.session_state.chat_history:

        st.write(
            f"**{sender}:** {message}"
        )

    # ================= JOB RECOMMENDER =================

    st.divider()
    st.markdown(
        "## 💼 Recommended Jobs"
    )

    recommended_jobs = recommend_jobs(
        clean_text
    )

    for job, score in recommended_jobs:

        match_percent = round(
            score * 100,
            2
        )

        st.write(
            f"✅ {job} — Match Score: {match_percent}%"
        )

        st.progress(
            min(score, 1.0)
        )

    # ================= JD MATCHER =================

    st.divider()
    st.markdown(
        "## 🎯 Job Description Matcher"
    )

    jd_text = st.text_area(
        "Paste Job Description Here"
    )

    if st.button(
        "Analyze Job Match"
    ):

        if jd_text:

            score = calculate_match_score(
                text,
                jd_text
            )

            missing_skills = find_missing_skills(
                text,
                jd_text
            )

            st.subheader(
                "📊 Match Score"
            )

            st.metric(
                "Resume Match %",
                f"{score}%"
            )

            st.progress(
                min(int(score), 100)
            )

            st.subheader(
                "❌ Missing Skills"
            )

            if missing_skills:

                for skill in missing_skills:

                    st.write(
                        f"🔹 {skill}"
                    )

            else:

                st.success(
                    "No major skills missing!"
                )
    
    # ================= SKILL GAP ANALYZER =================

    st.divider()
    st.markdown("## 📚 Skill Gap Analyzer")

    target_role = st.selectbox(
        "Choose Target Role",
        list(roles.keys()),
        key="skill_gap_role"
    )

    if st.button("Analyze Skill Gap"):

        user_skills = skills if skills else []

        missing_skills = analyze_skill_gap(
            user_skills,
            target_role,
            roles
        )

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.write(f"🔹 {skill}")

        else:
            st.success(
                "You already have all required skills!"
            )

        # ================= CAREER ROADMAP =================

    st.divider()
    st.markdown(
        "## 🗺️ AI Career Roadmap"
    )

    roadmap_skills = st.text_input(
        "Current Skills",
        placeholder="Python, SQL"
    )

    roadmap_role = st.selectbox(
        "Target Career Role",
        list(roles.keys()),
        key="roadmap_role"
    )

    if st.button("Generate Roadmap"):

        roadmap = generate_roadmap(
            roadmap_skills,
            roadmap_role
        )

        st.session_state["roadmap"] = roadmap

    if "roadmap" in st.session_state:

        st.markdown(
            st.session_state["roadmap"]
        )

        st.download_button(
            "⬇ Download Roadmap",
            st.session_state["roadmap"],
            file_name="career_roadmap.txt"
        )

    # ================= MOCK INTERVIEW =================

    st.divider()
    st.markdown("## 🎤 AI Mock Interview")

    interview_role = st.selectbox(
        "Interview Role",
        [
            "AI Engineer",
            "Data Scientist",
            "Software Engineer"
        ],
        key="interview_role"
    )

    if st.button("Generate Question"):

        question = generate_question(
            interview_role
        )

        st.session_state["question"] = question

    if "question" in st.session_state:

        st.subheader("Interview Question")

        st.write(
            st.session_state["question"]
        )

        user_answer = st.text_area(
            "Your Answer"
        )

        if st.button("Evaluate Answer"):

            feedback = evaluate_answer(
            st.session_state["question"],
            user_answer
        )

            st.markdown(feedback)

            st.download_button(
                "⬇ Download Feedback",
                feedback,
                file_name="interview_feedback.txt"
        )

        # ================= COVER LETTER =================

    st.divider()
    st.markdown(
        "## 📄 Cover Letter Generator"
    )

    cover_jd = st.text_area(
        "Paste Job Description",
        key="cover_letter_jd"
    )

    if st.button(
    "Generate Cover Letter"
):

        if cover_jd:

            with st.spinner(
                "Generating Cover Letter..."
            ):

                letter = generate_cover_letter(
                    text,
                    cover_jd
                )

                st.markdown(letter)

                st.download_button(
                    "⬇ Download Cover Letter",
                    letter,
                    file_name="cover_letter.txt"
                )

    # ================= RAW TEXT =================

    with st.expander(
        "Show Raw Text"
    ):
        st.write(text)

    with st.expander(
        "Processed Resume Text"
    ):
        st.write(clean_text)