# Smart Resume Matcher – ATS-Style Resume Ranking Engine

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20Cosine%20Similarity-orange)
![ML](https://img.shields.io/badge/Machine%20Learning-Applied-success)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Smart Resume Matcher is a **production-style Applicant Tracking System (ATS)** that ranks resumes against a job description using a **hybrid scoring approach** combining rule-based skill matching and semantic similarity using NLP.

The system is designed to simulate real-world resume screening pipelines used in recruitment platforms, focusing on **accuracy, explainability, and scalability**.

---

## Problem Statement

Recruiters often receive a large volume of resumes for a single job posting, making manual screening inefficient and subjective.

This project aims to:
- Automate resume screening
- Quantify resume–job relevance
- Rank candidates based on skill match and semantic alignment
- Provide interpretable and explainable scores

---

## Key Features

- Rule-based skill extraction and weighted matching  
- Semantic similarity using NLP techniques  
- Hybrid scoring system (rule-based + ML)  
- Batch resume ranking support  
- PDF and TXT resume parsing  
- Explainable output (matched and missing skills)  
- Command-line interface (CLI) execution  
- Modular, maintainable backend architecture  

---

## System Architecture
```
smart-resume-matcher/
│
├── data/
│ ├── resumes/
│ │ ├── r.txt
│ │ ├── Sarah_Chen_Senior_Developer.pdf
│ │ └── Maria_Rodriguez_Entry_Level.pdf
│ │
│ ├── job_description.txt
│ └── sample_resumes.txt
│
├── src/
│ ├── main.py # CLI entry point
│ ├── parser.py # Resume parsing (PDF / TXT)
│ ├── matcher.py # Rule-based skill matching
│ ├── scorer.py # NLP semantic similarity scoring
│ ├── ranker.py # Resume ranking logic
│ └── utils.py # Skill extraction and weighting
│
├── requirements.txt
├── README.md
└── .gitignore
``` 

---

## How It Works

### 1. Rule-Based Matching
- Extract skills from resumes and job description
- Apply weighted scoring to critical skills
- Compute a rule-based match score

### 2. ML Semantic Matching
- Vectorize text using **TF-IDF**
- Compute semantic similarity using **Cosine Similarity**

### 3. Final Scoring
The final resume score is calculated as:

Final Score = (Rule-Based Score × 0.6) + (ML Similarity Score × 0.4)


This ensures important skills are prioritized while still capturing semantic relevance.

---

## Design Decisions

- Combined rule-based and ML-based approaches to balance **explainability** and **semantic understanding**
- Assigned higher weight to rule-based scoring to ensure critical skills influence ranking
- Used TF-IDF instead of deep embeddings for efficiency and interpretability
- Implemented a CLI interface to support batch processing and automation
- Designed modular components to allow easy future extensions

---

## Tech Stack

| Layer        | Technology |
|-------------|------------|
| Language    | Python |
| NLP         | TF-IDF, Cosine Similarity |
| ML          | Scikit-learn |
| Parsing     | pdfplumber |
| Interface   | CLI |
| Tooling     | Git |

## Setup & Usage

### Installation

```bash
git clone https://github.com/itskhyatii19/smart-resume-matcher.git
cd smart-resume-matcher
pip install -r requirements.txt
Run (Single Resume)
python src/main.py --resume data/r.txt --job data/job_description.txt
Run (Batch Resume Ranking)
python src/main.py --resume data/resumes --job data/job_description.txt
Sample Output:
RANKED RESUMES

{'file': 'r.txt', 'final_score': 62.57, 'matched_skills': ['python', 'flask']}
{'file': 'Sarah_Chen_Senior_Developer.pdf', 'final_score': 38.10}
{'file': 'Maria_Rodriguez_Entry_Level.pdf', 'final_score': 0.00}
```
## Key Learnings
```bash
Designing ATS-style ranking systems

Applying NLP for semantic text similarity

Balancing rule-based logic with ML scoring

Building explainable ML systems

Structuring production-ready Python projects

Handling unstructured data (PDF / TXT)
```
## Future Enhancements
```bash
Web interface using Streamlit or FastAPI

Skill synonym and ontology mapping

Resume improvement suggestions

Cloud deployment

Future Enhancements

Web interface using Streamlit or FastAPI

Skill synonym and ontology mapping

Resume improvement suggestions

Cloud deployment

Transformer-based embeddings (BERT)

Job role classification

Transformer-based embeddings (BERT)

Job role classification
```
## Author

### Khyati Sharma
B.Tech in Artificial Intelligence
Aspiring Machine Learning & Backend Engineer

GitHub: https://github.com/itskhyatii19
