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

        # skip non-text files
        if not file.endswith(".txt"):
            continue

        resume_text = load_resume(path)

        # rule based score
        rule = rule_based_match(resume_text, job_text)

        # ml semantic score
        ml = semantic_similarity(resume_text, job_text)

        # final weighted score
        final = float(
            round((rule["match_score"] * 0.6) + (ml * 0.4), 2)
        )

        # missing skills (ATS feedback)
        missing = list(set(rule["job_skills"]) - set(rule["matched_skills"]))

        results.append({
            "file": file,
            "rule_score": rule["match_score"],
            "ml_score": ml,
            "final_score": final,
            "matched_skills": rule["matched_skills"],
            "missing_skills": missing
        })

    # sort by best match
    return sorted(results, key=lambda x: x["final_score"], reverse=True)
