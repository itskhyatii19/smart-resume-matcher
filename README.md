# 🧠 Smart Resume Matcher (ATS Engine)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)
![ML](https://img.shields.io/badge/ML-NLP-orange)
![GitHub stars](https://img.shields.io/github/stars/itskhyatii19/smart-resume-matcher?style=social)

> A **production-style Applicant Tracking System (ATS)** that ranks resumes against a job description using  
**rule-based skill matching + semantic ML similarity.**

---

## 🚀 Features

✔ Skill extraction from resumes  
✔ Weighted rule-based scoring  
✔ Semantic similarity using NLP  
✔ Batch resume ranking  
✔ PDF & TXT resume support  
✔ Explainable output (matched + missing skills)  
✔ CLI based execution  
✔ Modular clean architecture  

---

## 🏗 Project Structure

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
│ ├── parser.py # Resume loader (TXT / PDF)
│ ├── matcher.py # Rule based engine
│ ├── scorer.py # ML semantic similarity
│ ├── ranker.py # Resume ranking logic
│ └── utils.py # Skill extraction + weights
│
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy code

---

## ⚙ Tech Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| NLP | TF-IDF, Cosine Similarity |
| Parsing | pdfplumber |
| ML | Scikit-learn |
| Tooling | Git, CLI |

---

## 🔑 How It Works

### 1️⃣ Rule-Based Matching
- Extract skills from resume & job
- Apply **weighted scoring**
- Calculate % match

### 2️⃣ ML Semantic Matching
- Vectorize text
- Compute similarity score

### 3️⃣ Final Score
Final Score = (Rule Score * 0.6) + (ML Score * 0.4)

yaml
Copy code

---

## 🛠 Setup

```bash
git clone https://github.com/itskhyatii19/smart-resume-matcher.git
cd smart-resume-matcher
pip install -r requirements.txt
▶ Run (Single Resume)
bash
Copy code
python src/main.py --resume data/r.txt --job data/job_description.txt
▶ Run (Batch Ranking)
bash
Copy code
python src/main.py --resume data/resumes --job data/job_description.txt
📊 Sample Output
bash
Copy code
RANKED RESUMES

{'file': 'r.txt', 'final_score': 62.57, 'matched_skills': ['python','flask']}
{'file': 'Sarah_Chen_Senior_Developer.pdf', 'final_score': 38.1}
{'file': 'Maria_Rodriguez_Entry_Level.pdf', 'final_score': 0.0}
🎯 What This Project Demonstrates
✔ Real ATS system logic
✔ NLP text similarity
✔ Clean backend architecture
✔ File handling (PDF/TXT)
✔ Scoring algorithms
✔ Production-style design

🧠 Future Enhancements
Streamlit web interface

Skill synonym mapping

Resume improvement suggestions

Cloud deployment

Deep learning embeddings

Job role classification

📌 Resume Summary
Built an ATS-style Resume Ranking Engine using Python & NLP.
Implemented weighted skill matching + semantic similarity, batch ranking,
PDF parsing and explainable scoring system.

👩‍💻 Author
Khyati Sharma
🎓 B.Tech AI Student
💻 Backend & ML Developer

🔗 GitHub: @itskhyatii19

