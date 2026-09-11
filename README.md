# resume-job-matcher

A tool that ranks resumes against a job description using TF-IDF vectorization and cosine similarity, so recruiters can quickly see which candidates are the closest textual match.

## Features

- TF-IDF vectorization of resumes and job descriptions with scikit-learn
- Cosine similarity ranking of multiple resumes against one job description
- Keyword overlap highlighting between resume and job description
- Simple Flask API and command-line usage

## Tech Stack

Python, Flask, scikit-learn, NumPy

## Getting Started

```bash
pip install -r requirements.txt
python app.py
```

## API Overview

- `POST /match` - accepts a job description and a list of resumes, returns each resume ranked by similarity score
- `GET /` - health check
- 
