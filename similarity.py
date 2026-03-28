from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(vectors):
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]