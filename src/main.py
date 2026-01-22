# src/main.py

import argparse
import os

from parser import load_resume
from matcher import rule_based_match
from scorer import semantic_similarity
from ranker import rank_resumes


def single_resume_mode(resume_path, job_path):
    resume = load_resume(resume_path)
    job = load_resume(job_path)

    rule_result = rule_based_match(resume, job)
    ml_score = semantic_similarity(resume, job)

    print("\nRULE BASED MATCH")
    print(rule_result)

    print("\nML SEMANTIC SCORE")
    print(f"Similarity: {ml_score}%")

    final_score = round(
        (rule_result["match_score"] * 0.6) + (ml_score * 0.4), 2
    )

    print("\nFINAL SCORE")
    print(f"{final_score}%")


def batch_mode(resume_dir, job_path):
    results = rank_resumes(resume_dir, job_path)

    print("\nRANKED RESUMES")
    for r in results:
        print(r)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Smart Resume Matcher"
    )

    parser.add_argument(
        "--resume",
        help="Path to resume file OR folder of resumes"
    )

    parser.add_argument(
        "--job",
        required=True,
        help="Path to job description file"
    )

    args = parser.parse_args()

    if os.path.isdir(args.resume):
        batch_mode(args.resume, args.job)
    else:
        single_resume_mode(args.resume, args.job)
