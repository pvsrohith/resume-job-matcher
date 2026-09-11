import re
from typing import List, Dict

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

WORD_RE = re.compile(r"[a-zA-Z]+")

def extract_keywords(text: str, top_n: int = 15) -> List[str]:
    words = [w.lower() for w in WORD_RE.findall(text) if len(w) > 2]
    seen = []
    for w in words:
        if w not in seen:
            seen.append(w)
    return seen[:top_n]

def rank_resumes(job_description: str, resumes: List[str]) -> List[Dict]:
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    job_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]
    scores = cosine_similarity(job_vector, resume_vectors)[0]

    job_keywords = set(extract_keywords(job_description, top_n=30))
    results = []
    for i, resume in enumerate(resumes):
        resume_keywords = set(extract_keywords(resume, top_n=30))
        overlap = sorted(job_keywords & resume_keywords)
        results.append({
            "index": i,
            "score": round(float(scores[i]), 4),
            "matched_keywords": overlap,
        })

    results.sort(key=lambda r: r["score"], reverse=True)
    return results
