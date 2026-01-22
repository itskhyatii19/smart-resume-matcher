from parser import load_resume
from matcher import rule_based_match
from scorer import semantic_similarity
import os

def rank_resumes(resume_dir, job_path):
    job_text = load_resume(job_path)
    results = []

    for file in os.listdir(resume_dir):
        path = os.path.join(resume_dir, file)
        resume_text = load_resume(path)

        rule = rule_based_match(resume_text, job_text)
        ml = semantic_similarity(resume_text, job_text)

        final = round(rule["match_score"] * 0.6 + ml * 0.4, 2)

        results.append({
            "file": file,
            "final_score": final
        })

    return sorted(results, key=lambda x: x["final_score"], reverse=True)
