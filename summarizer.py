from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def summarize_text(text, num_sentences=3):
    sentences = text.split('. ')

    if len(sentences) <= num_sentences:
        return text

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    scores = np.array(tfidf_matrix.sum(axis=1)).flatten()

    top_indices = scores.argsort()[-num_sentences:]
    top_indices.sort()

    summary = '. '.join([sentences[i] for i in top_indices])

    return summary