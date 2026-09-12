
from pathlib import Path
from pypdf import PdfReader
from docx import Document
import pandas as pd


def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_text_from_docx(file_path: str) -> str:
    document = Document(file_path)
    text = ""

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text


def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_text_from_csv(file_path: str) -> str:
    dataframe = pd.read_csv(file_path)
    return dataframe.to_string(index=False)


def extract_text_from_excel(file_path: str) -> str:
    dataframe = pd.read_excel(file_path)
    return dataframe.to_string(index=False)


def extract_text(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    elif extension == ".txt":
        return extract_text_from_txt(file_path)

    elif extension == ".csv":
        return extract_text_from_csv(file_path)

    elif extension == ".xlsx":
        return extract_text_from_excel(file_path)

    else:
        raise ValueError(
            "Unsupported file type. Supported formats: "
            "PDF, DOCX, TXT, CSV, XLSX"
        )