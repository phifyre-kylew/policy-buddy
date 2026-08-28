"""Stage 3 - semantic search over the indexed corpus.

Run:  python src/retrieve.py
"""
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="vectordb")
collection = client.get_collection("policies")


def search(question, n=5):
    """Embed the question, return the closest chunks with their source."""
    results = collection.query(
        query_embeddings=[model.encode(question).tolist()],
        n_results=n,
    )
    return list(zip(results["documents"][0], results["metadatas"][0]))


if __name__ == "__main__":
    print("Semantic search. Try: 'time off for a new baby'\n")
    while True:
        q = input("Question (or 'quit'): ").strip()
        if q.lower() in ("quit", "exit", ""):
            break
        for text, meta in search(q):
            print(f"\n--- {meta['source']} ---")
            print(text[:400], "...")
        print()
