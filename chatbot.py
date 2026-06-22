import streamlit as st
from google import genai

# Create Gemini client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Chat function
def career_chat(user_question, resume_text):

    prompt = f"""
    You are an AI Career Assistant.

    Resume:
    {resume_text}

    User Question:
    {user_question}

    Give professional career guidance.
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"