# src/utils.py

SKILL_WEIGHTS = {
    "python": 3,
    "machine learning": 3,
    "flask": 2,
    "sql": 2,
    "docker": 2,
    "git": 1,
    "html": 1,
    "css": 1,
    "javascript": 1
}

SKILLS = [
    "python", "java", "c++",
    "machine learning", "deep learning",
    "flask", "django", "fastapi",
    "sql", "mongodb",
    "pandas", "numpy", "scikit-learn",
    "docker", "git"
]
import re

def extract_skills(text: str):
    text = text.lower()
    found = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found.append(skill)

    return list(set(found))
