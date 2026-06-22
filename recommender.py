from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample job database
jobs = {
    "Data Scientist": "python machine learning pandas numpy statistics deep learning",
    
    "Software Engineer": "java c++ data structures algorithms sql system design",
    
    "Web Developer": "html css javascript react nodejs frontend backend",
    
    "Data Analyst": "excel sql tableau power bi analytics visualization",
    
    "AI Engineer": "python tensorflow pytorch deep learning nlp machine learning"
}

# Recommendation function
def recommend_jobs(resume_text):

    # Convert jobs to list
    job_titles = list(jobs.keys())
    job_descriptions = list(jobs.values())

    # Add resume text
    documents = job_descriptions + [resume_text]

    # TF-IDF
    tfidf = TfidfVectorizer()

    vectors = tfidf.fit_transform(documents)

    # Resume vector
    resume_vector = vectors[-1]

    # Job vectors
    job_vectors = vectors[:-1]

    # Similarity
    similarity = cosine_similarity(resume_vector, job_vectors)

    scores = similarity[0]

    # Sort jobs
    ranked_jobs = sorted(
        zip(job_titles, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_jobs