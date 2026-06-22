from modules.chatbot import career_chat

def generate_roadmap(current_skills, target_role):

    prompt = f"""
    Create a personalized learning roadmap.

    Current Skills:
    {current_skills}

    Target Role:
    {target_role}

    Give:
    1. Weekly learning plan
    2. Skills to learn
    3. Projects to build
    4. Resources to study
    5. Interview preparation tips

    Keep it practical and beginner friendly.
    """

    return career_chat(prompt, "")