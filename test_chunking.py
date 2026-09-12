from services.document_loader import extract_text_from_pdf
from chunking import split_text


pdf_path = "uploads/Amina_AI Developer_Resume.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = split_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk)