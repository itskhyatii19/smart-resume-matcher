from utils import extract_skills, SKILL_WEIGHTS

def rule_based_match(resume_text, job_text):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = set(resume_skills) & set(job_skills)

    total_weight = 0
    matched_weight = 0

    for skill in job_skills:
        weight = SKILL_WEIGHTS.get(skill, 1)   # default = 1
        total_weight += weight

        if skill in matched:
            matched_weight += weight

    if total_weight == 0:
        score = 0
    else:
        score = round((matched_weight / total_weight) * 100, 2)

    missing = list(set(job_skills) - matched)

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": list(matched),
        "missing_skills": missing,
        "weighted_score": score
    }
