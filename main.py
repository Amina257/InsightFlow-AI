from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os
import shutil

from services.document_loader import extract_text
from chunking import split_text
from embeddings import create_embeddings
from vector_store import create_vector_store
from graph import bi_graph


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="InsightFlow AI",
    description="Multi-Agent Business Intelligence API",
    version="1.0.0"
)


# ============================================================
# CHAT REQUEST
# ============================================================

class ChatRequest(BaseModel):
    prompt: str


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "InsightFlow AI API is running"
    }


# ============================================================
# UPLOAD DOCUMENT
# ============================================================

@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text
    text = extract_text(file_path)

    # Split text into chunks
    chunks = split_text(text)

    # Create embeddings
    embeddings = create_embeddings(chunks)

    # Create FAISS vector database
    create_vector_store(
        chunks,
        embeddings
    )

    return {
        "message": "Document uploaded and indexed successfully",
        "filename": file.filename,
        "chunks": len(chunks)
    }


# ============================================================
# CHAT
# ============================================================

@app.post("/chat")
def chat(request: ChatRequest):

    # Check whether a document has been uploaded
    if not os.path.exists("vector_db/index.faiss"):

        return {
            "question": request.prompt,
            "answer": "No document is currently uploaded. Please upload a document before asking a question.",
            "analysis": "",
            "insights": "",
            "report": ""
        }

    # Run the LangGraph multi-agent workflow
    result = bi_graph.invoke(
        {
            "question": request.prompt
        }
    )

    return {
        "question": request.prompt,
        "answer": result["answer"],
        "analysis": result["analysis"],
        "insights": result["insights"],
        "report": result["report"]
    }


# ============================================================
# DELETE DOCUMENT
# ============================================================

@app.delete("/document")
def clear_document():

    # Remove uploaded documents
    if os.path.exists("uploads"):
        shutil.rmtree("uploads")

    os.makedirs("uploads", exist_ok=True)

    # Remove vector database
    if os.path.exists("vector_db"):
        shutil.rmtree("vector_db")

    return {
        "message": "Document and vector database cleared successfully"
    }