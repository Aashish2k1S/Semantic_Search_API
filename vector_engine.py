from sentence_transformers import SentenceTransformer
import faiss, numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "AI is transforming healthcare and diagnostics.",
    "Machine learning models are used in disease prediction.",
    "Python is a core language for data science.",
    "FastAPI enables rapid API development for AI apps.",
    "Deep learning assists in image-based medical analysis."
]

doc_embeddings = model.encode(documents, normalize_embeddings=True)
index = faiss.IndexFlatIP(doc_embeddings.shape[1])
index.add(doc_embeddings) #type: ignore

def retrieve_context(query, top_k=3):
    query_emb = model.encode([query], normalize_embeddings=True)
    D, I = index.search(query_emb, top_k) #type: ignore
    return [documents[i] for i in I[0]]

