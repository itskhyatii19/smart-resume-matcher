from parser import load_resume
from matcher import rule_based_match
from scorer import semantic_similarity
from ranker import rank_resumes
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

resume = load_resume(os.path.join(BASE_DIR, "..", "data", "sample_resumes.txt"))
job = load_resume(os.path.join(BASE_DIR, "..", "data", "job_description.txt"))

rule = rule_based_match(resume, job)
ml = semantic_similarity(resume, job)

print(rule)
print(f"ML Score: {ml}%")

results = rank_resumes("../data/resumes", "../data/job_description.txt")
print(results)
