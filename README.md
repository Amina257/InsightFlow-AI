
# InsightFlow AI

## Multi-Agent Business Intelligence Analyst
InsightFlow AI is an AI-powered Business Intelligence application that combines Retrieval-Augmented Generation (RAG), semantic search, and a multi-agent workflow to analyze information from uploaded documents.

The system retrieves relevant information from documents and processes it through specialized AI agents to generate accurate answers, analytical findings, business insights, and structured reports.

## Key Features

- 📄 Upload and process documents
- 🔎 Retrieval-Augmented Generation (RAG)
- 🧠 Multi-agent AI workflow using LangGraph
- 💬 Question answering from uploaded documents
- 📊 Business data analysis and insight generation
- 📝 Automated business report generation
- 🗂️ FAISS vector database for semantic search
- 🤖 Local LLM inference using Ollama and Gemma
- ⚡ FastAPI REST API
- 🧪 Swagger API documentation and testing

## Supported File Formats

- PDF
- DOCX
- TXT
- CSV
- XLSX

## System Architecture

```text
User
  ↓
FastAPI API
  ↓
Document Upload
  ↓
Document Processing
  ↓
Text Chunking
  ↓
Embeddings
  ↓
FAISS Vector Database
  ↓
Semantic Retrieval
  ↓
LangGraph Multi-Agent Workflow
  ↓
BI Agent
  ↓
Analyst Agent
  ↓
Insight Agent
  ↓
Report Agent
  ↓
Ollama + Gemma
  ↓
Final Business Response

## Multi-Agent Workflow

InsightFlow AI uses a sequential multi-agent workflow built with LangGraph. Each agent performs a specific role in the business analysis process.

### 1. Business Intelligence Agent

The Business Intelligence Agent receives the user's question and the relevant context retrieved from the uploaded document. It generates a direct answer based only on the available document information.

### 2. Analyst Agent

The Analyst Agent analyzes the retrieved information and identifies important facts, patterns, and relevant findings related to the user's question.

### 3. Insight Agent

The Insight Agent reviews the analysis and identifies meaningful business insights, including relevant risks, opportunities, and patterns supported by the available information.

### 4. Report Agent

The Report Agent converts the generated insights into a structured business report containing:

- Executive Summary
- Key Findings
- Business Insights
- Recommendations

---

## Retrieval-Augmented Generation (RAG)

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents before generating an AI response.

The RAG pipeline consists of the following stages:

```text
Document Upload
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Text Embeddings
      ↓
FAISS Vector Database
      ↓
Semantic Retrieval
      ↓
Relevant Context
      ↓
Multi-Agent Workflow
      ↓
AI-Generated Response

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| FastAPI | REST API development |
| LangGraph | Multi-agent workflow orchestration |
| LangChain | Text processing and document utilities |
| Sentence Transformers | Text embedding generation |
| FAISS | Vector similarity search |
| Ollama | Local LLM inference |
| Gemma | Large Language Model |
| Pandas | CSV and Excel data processing |
| PyPDF | PDF text extraction |
| python-docx | DOCX text extraction |
| Swagger / OpenAPI | API documentation and testing |
| Git / GitHub | Version control |

## API Endpoints

### Health Check

GET /

Checks whether the InsightFlow AI API is running.

### Document Upload

POST /upload

Uploads a supported document, extracts its content, creates text chunks and embeddings, and stores them in the FAISS vector database.

### AI Chat

POST /chat

Accepts a user's question and executes the LangGraph multi-agent workflow.

The response provides:

- AI Answer
- Analysis
- Business Insights
- Generated Report

Example request:

```json
{
  "prompt": "What are the important insights from this document?"
}

Delete/Document

Deletes the currently uploaded document and clears the associated vector database.

## Project Structure

```text
InsightFlow-AI/
│
├── backend/
│   ├── agents/
│   │   ├── bi_agent.py
│   │   ├── analyst_agent.py
│   │   ├── insight_agent.py
│   │   └── report_agent.py
│   │
│   ├── services/
│   │   ├── document_loader.py
│   │   └── ollama_service.py
│   │
│   ├── main.py
│   ├── graph.py
│   ├── rag.py
│   ├── retriever.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── chunking.py
│   └── requirements.txt
│

└── README.md

## Local Setup

### Clone the Repository

```bash
git clone https://github.com/Amina257/InsightFlow-AI.git
cd InsightFlow-AI

Install Dependencies
cd backend
pip install -r requirements.txt

Start Ollama
ollama run  gemma3:1b

Start FastAPI
uvicorn main:app --reload

Open Swagger at
http://127.0.0.1:8000/docs

## Application Workflow

1. User uploads a document through the FastAPI /upload endpoint.
2. The document content is extracted based on its file type.
3. The extracted text is split into smaller chunks.
4. Sentence Transformers generates embeddings for the chunks.
5. FAISS stores the embeddings for similarity-based retrieval.
6. User submits a business question through the /chat endpoint.
7. The Retriever searches for the most relevant document chunks.
8. The LangGraph workflow passes the retrieved context through multiple AI agents:
   - Business Intelligence Agent
   - Analyst Agent
   - Business Insight Agent
   - Report Generation Agent
9. Ollama with Gemma generates the responses.
10. The API returns the answer, analysis, business insights, and generated report.

##Screenshots
Screenshots  demonstrating the InsightFlow AI application, document upload, Swagger API testing, and multi-agent analysis workflow will be added here.
<img width="1349" height="894" alt="Swagger1" src="https://github.com/user-attachments/assets/125deb49-e1d4-4434-adf8-6724bc714ac7" />
<img width="1405" height="847" alt="Swagger2" src="https://github.com/user-attachments/assets/1119699b-bb66-4612-9f45-4bfce7663b7f" />
<img width="1370" height="882" alt="Swagger3" src="https://github.com/user-attachments/assets/ef6fff84-38e9-4693-ac08-3b5f2428c038" />
<img width="1443" height="925" alt="Swagger4" src="https://github.com/user-attachments/assets/5b11734d-355a-4f4b-b1ac-9ea7923de26d" />
<img width="1404" height="893" alt="Swagger5" src="https://github.com/user-attachments/assets/2af91951-9c6a-4652-808d-33e73102a7ee" />

## Future Enhancements

- Advanced business KPI and statistical analysis
- Improved multi-document management
- Interactive dashboard integration
- Cloud deployment with a hosted LLM
- Enhanced agentic decision-making and tool calling
- Support for more advanced structured-data analysis

## Project Status

*Status:* Working Local Prototype

InsightFlow AI is currently running locally with FastAPI, LangGraph, FAISS, Sentence Transformers, and Ollama.

The project is functional and supports document upload, RAG-based question answering, multi-agent analysis, business insights, and report generation.

## Author

*Amina Aminu*

BTech Computer Science graduate with a focus on Artificial Intelligence, Machine Learning, Data Science, NLP, and Generative AI.

Interested in opportunities in:

- AI/ML Engineering
- Data Science
- AI Development
- Machine Learning
- Generative AI

GitHub: [Amina257](https://github.com/Amina257)
