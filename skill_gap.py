def analyze_skill_gap(user_skills, target_role, roles):

    required_skills = roles.get(
        target_role,
        []
    )

    user_skills = [
        skill.strip().lower()
        for skill in user_skills
    ]

    missing_skills = []

    for skill in required_skills:

        if skill.lower() not in user_skills:

            missing_skills.append(skill)

    return missing_skills


def get_learning_priority(missing_skills):

    priority_order = []

    for i, skill in enumerate(
        missing_skills,
        start=1
    ):

        priority_order.append(
            f"{i}. {skill}"
        )

    return priority_order