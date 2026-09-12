import faiss
import numpy as np
import pickle
import os


def create_vector_store(chunks, embeddings):
    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])

    # Add embeddings to the index
    index.add(embeddings)

    # Create storage folder
    os.makedirs("vector_db", exist_ok=True)

    # Save FAISS index
    faiss.write_index(index, "vector_db/index.faiss")

    # Save chunks
    with open("vector_db/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    return index


def load_vector_store():
    index = faiss.read_index("vector_db/index.faiss")

    with open("vector_db/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks