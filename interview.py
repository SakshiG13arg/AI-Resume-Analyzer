import random

questions = {
    "AI Engineer": [
        "What is overfitting?",
        "What is NLP?",
        "Explain TensorFlow.",
        "What is deep learning?"
    ],

    "Data Scientist": [
        "What is bias variance tradeoff?",
        "Explain linear regression.",
        "What is feature engineering?"
    ],

    "Software Engineer": [
        "What is OOP?",
        "Explain polymorphism.",
        "What is a hash table?"
    ]
}

def generate_question(role):

    return random.choice(
        questions.get(
            role,
            ["Tell me about yourself."]
        )
    )