from services.document_loader import extract_text_from_pdf

pdf_path = "uploads/Amina_AI Developer_Resume.pdf"

text = extract_text_from_pdf(pdf_path)

print("\n--- EXTRACTED TEXT ---\n")
print(text[:3000])