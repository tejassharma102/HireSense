from sklearn.feature_extraction.text import TfidfVectorizer

def get_vectors(texts):
    tfidf = TfidfVectorizer()
    return tfidf.fit_transform(texts)