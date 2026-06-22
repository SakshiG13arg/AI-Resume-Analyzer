from modules.chatbot import career_chat

def generate_cover_letter(resume_text, jd_text):

    prompt = f"""
    Create a professional cover letter.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Requirements:
    - Professional tone
    - One page
    - Mention relevant skills
    - Tailor it to the job
    """

    return career_chat(prompt, "")