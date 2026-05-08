from google import genai

# Create Gemini client
client = genai.Client(api_key="AIzaSyCzUVtkPsHs1iWly0bV8W2qzwS6RyO2S68")

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