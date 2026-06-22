from modules.chatbot import career_chat


def evaluate_answer(question, answer):

    prompt = f"""
    You are an interview evaluator.

    Interview Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and provide:

    1. Technical Accuracy score out of 10
    2. Communication score out of 10
    3. Strengths
    4. Weaknesses
    5. Improved Answer

    Format clearly.
    """

    return career_chat(prompt, "")