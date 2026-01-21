from parser import load_resume
from matcher import match_resume
from scorer import semantic_similarity
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

resume_path = os.path.join(BASE_DIR, "..", "data", "sample_resumes.txt")
job_path = os.path.join(BASE_DIR, "..", "data", "job_description.txt")

resume = load_resume(resume_path)
job = load_resume(job_path)

rule_result = match_resume(resume, job)
ml_score = semantic_similarity(resume, job)

print("\nRULE BASED MATCH")
print(rule_result)

print("\nML SEMANTIC SCORE")
print(f"Similarity: {ml_score}%")
