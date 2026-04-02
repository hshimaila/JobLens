from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class JobMatcher:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")

    def match(self, resume_text: str, job_text: str) -> float:
        texts = [resume_text, job_text]
        tfidf_matrix = self.vectorizer.fit_transform(texts)

        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        return float(round(similarity[0][0] * 100, 2))
