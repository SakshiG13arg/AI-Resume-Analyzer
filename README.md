# 🚀 AI Career Assistant

An AI-powered Career Guidance Platform that helps users analyze resumes, identify skill gaps, match resumes with job descriptions, generate personalized career roadmaps, practice interviews, and create AI-generated cover letters.

Built using Python, Streamlit, Machine Learning, NLP, and Gemini AI.

---

# 🌟 Features

## 📄 Resume Analysis

- Upload resumes in PDF format
- Automatic resume text extraction
- Technical skill detection
- Resume scoring system
- Resume improvement suggestions
- Keyword analysis

---

## 🤖 AI Career Chatbot

- Personalized career guidance
- Resume feedback
- Internship recommendations
- Project suggestions
- Career planning assistance
- AI-powered question answering

---

## 💼 Job Recommendation System

- Recommends suitable job roles
- Resume-to-job matching
- TF-IDF based similarity scoring
- Match percentage for each role

---

## 🎯 Job Description Matcher

Compare your resume against a Job Description.

Features:

- Resume-JD match score
- Missing skill detection
- ATS-style resume analysis
- Improvement suggestions

---

## 📚 Skill Gap Analyzer

Analyze the gap between your current skills and target role requirements.

Features:

- Missing skills identification
- Skill comparison
- Learning priority recommendations

---

## 🗺️ AI Career Roadmap Generator

Generate a personalized roadmap based on:

- Current skills
- Target career role

Outputs:

- Learning path
- Recommended technologies
- Suggested progression plan

---

## 🎤 AI Mock Interview

Practice interview preparation with AI-generated questions.

Features:

- Role-specific questions
- AI answer evaluation
- Interview feedback
- Downloadable feedback reports

Supported Roles:

- AI Engineer
- Data Scientist
- Software Engineer

---

## 📄 AI Cover Letter Generator

Generate professional cover letters using:

- Resume content
- Job description

Features:

- Personalized content
- ATS-friendly format
- Downloadable cover letters

---

# 🛠 Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## AI & Machine Learning

- Gemini AI
- Scikit-Learn
- NLP
- TF-IDF Vectorization
- Cosine Similarity

---

# 📚 Libraries Used

- streamlit
- pdfplumber
- scikit-learn
- google-genai
- numpy
- pandas

---

# 📂 Project Structure

```text
AI-Career-Assistant/
│
├── app.py
│
├── modules/
│   ├── chatbot.py
│   ├── recommender.py
│   ├── jd_matcher.py
│   ├── skill_gap.py
│   ├── roadmap.py
│   ├── interview.py
│   ├── interview_evaluator.py
│   └── cover_letter.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Career-Assistant.git
```

## 2. Open Project Directory

```bash
cd AI-Career-Assistant
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Add Gemini API Key

Create a local file:

```text
.streamlit/secrets.toml
```

Add the following:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

⚠️ Important:

- Do NOT upload `secrets.toml` to GitHub.
- Add it to `.gitignore`.
- Keep your API key private.

Example `.gitignore`:

```gitignore
.streamlit/secrets.toml
__pycache__/
*.pyc
.env
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧠 Machine Learning Concepts Used

- TF-IDF Vectorization
- Cosine Similarity
- Resume Matching
- Skill Extraction
- Recommendation Systems
- Prompt Engineering
- NLP-Based Text Processing

---

# 🎯 Learning Outcomes

This project demonstrates:

- Artificial Intelligence Integration
- Generative AI Applications
- Resume Parsing
- Recommendation Systems
- NLP Techniques
- Streamlit Development
- Modular Python Architecture
- Career Guidance Automation

---

# 🚀 Future Enhancements

- User Authentication
- Resume Ranking System
- Database Integration
- Vector Database Support
- LangChain Integration
- RAG-based Career Assistant
- Resume Builder
- Interview Analytics Dashboard
- Real-Time Job Listings

---

# 👨‍💻 Author

**Sakshi Garg**

B.Tech (Electronics & Communication Engineering)

Passionate about AI, Machine Learning, and Software Development.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
