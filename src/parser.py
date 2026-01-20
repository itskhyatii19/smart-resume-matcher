# src/parser.py

import re
import os

def clean_text(text: str) -> str:
    """
    Clean resume text:
    - Lowercase
    - Remove special characters
    - Remove extra spaces
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_resume(file_path: str) -> str:
    """
    Load resume from text file
    (Later we will support PDF/DOCX)
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return clean_text(text)


from matcher import match_resume

if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    resume_path = os.path.join(BASE_DIR, "..", "data", "sample_resumes.txt")
    job_path = os.path.join(BASE_DIR, "..", "data", "job_description.txt")

    resume = load_resume(resume_path)
    job = load_resume(job_path)

    result = match_resume(resume, job)

    print("\nMATCH RESULT")
    print(result)
