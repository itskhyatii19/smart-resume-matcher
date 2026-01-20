# src/utils.py

SKILLS = [
    "python", "java", "c++",
    "machine learning", "deep learning",
    "flask", "django", "fastapi",
    "sql", "mongodb",
    "pandas", "numpy", "scikit-learn",
    "docker", "git"
]
def extract_skills(text: str):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return list(set(found))
