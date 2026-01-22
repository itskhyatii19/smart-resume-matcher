from utils import extract_skills

def rule_based_match(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = set(resume_skills) & set(job_skills)
    score = round(len(matched) / len(job_skills) * 100, 2) if job_skills else 0

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": list(matched),
        "match_score": score
    }
