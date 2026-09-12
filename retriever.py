from embeddings import create_embeddings
from vector_store import load_vector_store


def search_documents(query, k=3):
    # Load FAISS index and chunks
    index, chunks = load_vector_store()

    # Create embedding for the query
    query_embedding = create_embeddings([query])

    # Search for similar chunks
    distances, indices = index.search(query_embedding, k)

    results = []

    for i in indices[0]:
        if i != -1:
            results.append(chunks[i])

    return results