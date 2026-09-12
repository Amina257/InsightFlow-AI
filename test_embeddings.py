from services. document_loader import extract_text_from_pdf
from chunking import split_text
from embeddings import create_embeddings


pdf_path = "uploads/Amina_AI Developer_Resume.pdf"

# 1. Extract text
text = extract_text_from_pdf(pdf_path)

# 2. Split text into chunks
chunks = split_text(text)

# 3. Create embeddings
embeddings = create_embeddings(chunks)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)