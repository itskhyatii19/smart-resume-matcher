# src/ranker.py

from parser import load_resume
from matcher import rule_based_match
from scorer import semantic_similarity
import os

def rank_resumes(resume_dir, job_path):

    job_text = load_resume(job_path)
    results = []

    for file in os.listdir(resume_dir):

        path = os.path.join(resume_dir, file)

        # Skip folders & unsupported files
        if not os.path.isfile(path):
            continue

        if not file.endswith((".txt", ".pdf")):
            continue

        resume_text = load_resume(path)

        rule = rule_based_match(resume_text, job_text)
        ml = semantic_similarity(resume_text, job_text)

        final = round(
            (rule["weighted_score"] * 0.6) + (ml * 0.4),
            2
        )

        missing = list(
            set(rule["job_skills"]) - set(rule["matched_skills"])
        )

        results.append({
            "file": file,
            "rule_score": rule["weighted_score"],
            "ml_score": ml,
            "final_score": final,
            "matched_skills": rule["matched_skills"],
            "missing_skills": missing
        })

    return sorted(
        results,
        key=lambda x: x["final_score"],
        reverse=True
    )
