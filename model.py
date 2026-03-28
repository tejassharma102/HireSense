from preprocess import clean_text
from vectorizer import get_vectors
from similarity import calculate_similarity
from suggestions import give_suggestions

def analyze_resume(resume, job_desc):
    clean_resume = clean_text(resume)
    clean_job = clean_text(job_desc)

    vectors = get_vectors([clean_resume, clean_job])
    score = calculate_similarity(vectors)

    suggestions = give_suggestions(resume, job_desc)

    return score, suggestions