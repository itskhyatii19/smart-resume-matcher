# src/matcher.py

from utils import extract_skills


def match_resume(resume_text: str, job_text: str):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = set(resume_skills) & set(job_skills)

    if len(job_skills) == 0:
        score = 0
    else:
        score = round(len(matched) / len(job_skills) * 100, 2)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": list(matched),
        "match_score": score
    }
