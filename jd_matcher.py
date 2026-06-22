from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, jd_text):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [resume_text, jd_text]
    )

    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )

    return round(similarity[0][0] * 100, 2)


def find_missing_skills(resume_text, jd_text):

    important_skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "docker",
        "aws",
        "git",
        "flask",
        "tensorflow",
        "pytorch",
        "nlp",
        "pandas",
        "numpy",
        "power bi",
        "tableau",
        "react",
        "nodejs",
        "java",
        "c++"
    ]

    missing = []

    for skill in important_skills:

        if (
            skill.lower() in jd_text.lower()
            and
            skill.lower() not in resume_text.lower()
        ):
            missing.append(skill)

    return missing