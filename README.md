# Scientific RAG Lab

AI-powered scientific retrieval platform for optical turbulence research and free-space optical (FSO) communication experiments.

---

# Overview

Scientific RAG Lab is a modular Retrieval-Augmented Generation (RAG) system designed for scientific document ingestion, semantic retrieval, and AI-assisted exploration of optical turbulence research.

The project combines:

- local Large Language Models (LLMs)
- vector databases
- semantic embeddings
- scientific document ingestion
- asynchronous AI workflows
- retrieval pipelines

into a scalable architecture capable of transforming scientific PDFs and experimental artifacts into a searchable AI-ready knowledge system.

The current implementation focuses on local-first AI infrastructure using:

- Ollama
- Qdrant
- FastAPI
- LlamaIndex
- Inngest

---

# Features

Current capabilities include:

- PDF upload through a web interface
- automatic ingestion pipeline
- semantic chunking
- embedding generation
- vector storage with Qdrant
- semantic similarity search
- AI-generated answers using local LLMs
- asynchronous ingestion workflows with Inngest
- chat interface for querying scientific papers

---

# Architecture

```text
                ┌────────────────────┐
                │   Scientific PDFs  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Ingestion Pipeline │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │ Document Chunking  │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │ Semantic Embedding │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │ Qdrant Vector DB   │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │ Semantic Retrieval │
                └─────────┬──────────┘
                          │
                ┌─────────▼──────────┐
                │ Local LLM Reasoner │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Scientific Assistant│
                └────────────────────┘
```

---

# Technologies

## Core Stack

- Python
- FastAPI
- Ollama
- Qdrant
- Inngest
- LlamaIndex
- Pydantic
- Docker

## AI / Retrieval

- Retrieval-Augmented Generation (RAG)
- semantic embeddings
- vector similarity search
- local LLM inference
- scientific semantic retrieval

---

# Repository Structure

```text
scientific-rag-lab/
│
├── src/
│   ├── core/
│   │   └── config.py
│   │
│   ├── frontend/
│   │   ├── index.html
│   │   ├── styles.css
│   │   └── app.js
│   │
│   ├── ingestion/
│   │   ├── data_loader.py
│   │   ├── embedder.py
│   │   └── pipeline.py
│   │
│   ├── models/
│   │   ├── ingestion.py
│   │   ├── retrieval.py
│   │   └── vector_store.py
│   │
│   ├── vector_database/
│   │   └── vector_db.py
│   │
│   ├── workers/
│   │   ├── inngest_client.py
│   │   └── inngest_functions.py
│   │
│   └── main.py
│
├── documents_base/
├── vector_database/
├── requirements.txt
├── .env
└── README.md
```

---

# Setup

## 1. Clone the repository

```bash
git clone <repository-url>
cd scientific-rag-lab
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python -m venv env
source env/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file in the project root.

Example:

```env
# =========================================
# Ollama
# =========================================
OLLAMA_BASE_URL=http://localhost:11434

# =========================================
# Models
# =========================================
LLM_MODEL=qwen2.5:7b
EMBED_MODEL=bge-m3

# =========================================
# Qdrant
# =========================================
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=documents

# =========================================
# Chunking
# =========================================
CHUNK_SIZE=1024
CHUNK_OVERLAP=128

# =========================================
# Inngest
# =========================================
INNGEST_APP_ID=scientific-rag-lab
INNGEST_IS_PRODUCTION=false
INNGEST_LOGGER=uvicorn
```

---

# Running Qdrant

Make sure Docker Desktop is running.

## Linux / macOS

```bash
docker run -d \
  --name scientific-rag-qdrant \
  -p 6333:6333 \
  -v "$(pwd)/vector_database:/qdrant/storage" \
  qdrant/qdrant
```

## Windows PowerShell

```powershell
docker run -d `
  --name scientific-rag-qdrant `
  -p 6333:6333 `
  -v "${PWD}/vector_database:/qdrant/storage" `
  qdrant/qdrant
```

Qdrant dashboard:

```text
http://localhost:6333/dashboard
```

---

# Running Ollama

Start Ollama locally:

```bash
ollama serve
```

Pull required models:

```bash
ollama pull qwen2.5:7b
ollama pull bge-m3
```

---

# Running the Backend

Start FastAPI:

```bash
uvicorn src.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

---

# Running Inngest

```bash
npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
```

Inngest dashboard:

```text
http://127.0.0.1:8288
```

---

# Usage

## Upload a PDF

Open:

```text
http://127.0.0.1:8000
```

Upload a scientific paper through the web interface.

The system will automatically:

1. ingest the document
2. split it into chunks
3. generate embeddings
4. store vectors in Qdrant

---

## Query the document

Ask questions directly through the chat interface.

Example queries:

```text
What is this paper about?

Summarize the conclusions.

What turbulence metrics are analyzed?

Explain the experimental setup.

What is the role of the Fried parameter?
```

---

# Current Research Direction

This project is part of a broader research effort focused on:

- optical turbulence characterization
- free-space optical communications
- AI-assisted scientific analysis
- data-centric turbulence modeling
- semantic scientific retrieval
- multimodal scientific AI systems

The long-term objective is to investigate how modern AI systems can assist scientific experimentation by transforming raw experimental artifacts into searchable and semantically connected knowledge.

---

# Future Work

Planned future features include:

- multimodal retrieval
- image embeddings
- experiment similarity search
- scientific agents
- metadata filtering
- hybrid search
- reranking
- conversational memory
- streaming responses
- distributed vector storage
- evaluation pipelines
- observability and tracing
- scientific knowledge graphs

---

# Status

🚧 Active development

Current version includes a fully functional local scientific RAG pipeline with:

- PDF ingestion
- vector search
- local embeddings
- local LLM answering
- asynchronous workflows
- web chat interface