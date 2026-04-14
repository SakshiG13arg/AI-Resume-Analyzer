import streamlit as st
import pdfplumber
import spacy

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

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# App title
st.title("AI Resume Analyzer 🚀")

# Role selection
role = st.selectbox("Select Job Role", list(roles.keys()))

# Function: Extract text
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Function: Clean text
def preprocess_text(text):
    doc = nlp(text.lower())
    clean_text = []

    for token in doc:
        if not token.is_stop and token.is_alpha:
            clean_text.append(token.lemma_)

    return " ".join(clean_text)

# Function: Extract skills
def extract_skills(text, role):
    skills = roles[role]
    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return found

# Function: Score
def calculate_score(skills, role):
    total_skills = len(roles[role])
    score = (len(skills) / total_skills) * 100
    return round(score, 2)

# Function: Keywords
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
    st.metric(label="Resume Score", value=f"{final_score}%")
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
    st.subheader("Processed Resume Text")
    st.write(clean_text)