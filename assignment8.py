import zipfile
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = []
doc_names = []

with zipfile.ZipFile("/Users/user/Downloads/texts.zip", 'r') as zip_ref:
    for file in zip_ref.namelist():
        if file.endswith(".txt"):
            with zip_ref.open(file) as f:
                documents.append(f.read().decode("utf-8", errors="ignore"))
                doc_names.append(file)

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(documents)

query = "Speech emphasizing patriotism and media criticism and promises for a better future for America."
query_vector = vectorizer.transform([query])

similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]
ranked_indices = np.argsort(similarity_scores)[::-1]

print("Documents ranked by relevance:\n")

for idx in ranked_indices:
    print(doc_names[idx], similarity_scores[idx])


