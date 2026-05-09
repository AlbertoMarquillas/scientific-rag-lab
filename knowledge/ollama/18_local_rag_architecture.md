# Local RAG Architecture

## Introduction

Retrieval-Augmented Generation (RAG) is one of the most important architectures in modern AI systems.

A local RAG system combines:

* local language models
* local embeddings
* local vector databases
* local document processing
* local APIs

The goal is to build an AI system that can answer questions using external knowledge without depending on cloud APIs.

---

# What Is RAG?

RAG stands for:

```text
Retrieval-Augmented Generation
```

It combines two processes:

| Stage      | Purpose                           |
| ---------- | --------------------------------- |
| Retrieval  | Find relevant information         |
| Generation | Produce a natural-language answer |

Instead of relying only on the model's internal knowledge, the system retrieves external context first.

---

# Core Idea

Without RAG:

```text
User Question
    ↓
LLM
    ↓
Answer from model memory
```

With RAG:

```text
User Question
    ↓
Retriever
    ↓
Relevant Context
    ↓
LLM
    ↓
Grounded Answer
```

The model becomes grounded in retrieved evidence.

---

# What Makes RAG Local?

A RAG system is local when the main components run on the user's machine or private infrastructure.

Local components may include:

* Ollama for LLM inference
* Ollama for embeddings
* Qdrant for vector storage
* LlamaIndex for orchestration
* FastAPI for backend APIs
* Streamlit for UI

No external AI provider is required.

---

# High-Level Local RAG Stack

Typical stack:

```text
Documents
    ↓
Ingestion Pipeline
    ↓
Chunking
    ↓
Local Embeddings
    ↓
Qdrant Vector DB
    ↓
Retriever
    ↓
Prompt Assembly
    ↓
Ollama LLM
    ↓
Generated Answer
```

This is the standard architecture for private AI assistants.

---

# Main Components

## 1. Data Sources

Possible data sources:

* Markdown files
* PDFs
* research papers
* experiment logs
* JSON files
* code repositories
* documentation
* notes

The system starts with raw knowledge.

---

## 2. Ingestion Pipeline

The ingestion pipeline loads and prepares documents.

Responsibilities:

* reading files
* extracting text
* cleaning content
* attaching metadata
* preparing chunks

Ingestion transforms raw files into structured knowledge units.

---

## 3. Chunking

Documents are split into smaller pieces.

Reason:

```text
LLMs and embedding models cannot efficiently process entire knowledge bases at once
```

Chunks become the units of retrieval.

---

## 4. Embeddings

Each chunk is converted into a vector.

Example:

```text
Text Chunk → Embedding Vector
```

Embeddings represent semantic meaning numerically.

---

## 5. Vector Database

The vector database stores:

* vectors
* text chunks
* metadata
* indexes

Qdrant is commonly used for this role.

---

## 6. Retriever

The retriever receives a user query and finds relevant chunks.

Workflow:

```text
Query → Query Embedding → Vector Search → Relevant Chunks
```

The retriever is the external memory access layer.

---

## 7. Prompt Assembly

Retrieved chunks are inserted into the LLM prompt.

Prompt may include:

* system instructions
* retrieved context
* user question
* conversation history
* formatting rules

Prompt assembly strongly affects answer quality.

---

## 8. Local LLM

The local LLM generates the final answer.

Example:

```text
Ollama + qwen2.5:7b
```

The model uses retrieved context to answer.

---

# Local RAG Architecture Diagram

```text
          ┌──────────────────┐
          │   User Interface │
          └────────┬─────────┘
                   │
                   ↓
          ┌──────────────────┐
          │   FastAPI Backend│
          └────────┬─────────┘
                   │
          ┌────────┴─────────┐
          │                  │
          ↓                  ↓
 ┌─────────────────┐  ┌─────────────────┐
 │    Retriever    │  │   Ollama LLM    │
 └────────┬────────┘  └─────────────────┘
          │
          ↓
 ┌─────────────────┐
 │   Qdrant DB     │
 └────────┬────────┘
          │
          ↓
 ┌─────────────────┐
 │  Vector Index   │
 └─────────────────┘
```

This separates retrieval from generation.

---

# Offline Indexing vs Online Querying

Local RAG systems usually have two separate workflows.

## Offline / Background Indexing

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Qdrant Storage
```

This happens before users ask questions.

---

## Online Querying

```text
User Question
    ↓
Retrieval
    ↓
Prompt Assembly
    ↓
Generation
```

This happens during user interaction.

Separating these workflows improves performance.

---

# Why RAG Is Not Just Chat with PDFs

A common misconception:

```text
RAG = chat with PDFs
```

Reality:

RAG is a general architecture for connecting language models to external knowledge.

Possible sources:

* papers
* code
* databases
* logs
* images
* experiment outputs
* documentation

PDFs are only one possible input type.

---

# Role of LlamaIndex

LlamaIndex can orchestrate:

* data loading
* document parsing
* node creation
* indexing
* retrieval
* query engines
* prompt assembly

It acts as a high-level framework for RAG systems.

---

# Role of Ollama

Ollama provides:

* local LLM inference
* local embeddings
* API access
* model management

It replaces cloud model APIs in the local stack.

---

# Role of Qdrant

Qdrant provides:

* vector storage
* similarity search
* metadata filtering
* scalable retrieval
* ANN indexing

It acts as the semantic memory layer.

---

# Role of FastAPI

FastAPI provides:

* HTTP routes
* backend orchestration
* API endpoints
* authentication layer
* service integration

Example routes:

```text
POST /ingest
POST /chat
POST /search
```

---

# Role of Streamlit

Streamlit can provide:

* chat interface
* debugging UI
* document upload
* retrieval visualization
* experiment dashboard

It is useful for prototypes and internal tools.

---

# Metadata in Local RAG

Metadata is essential.

Examples:

* source file
* topic
* creation date
* experiment ID
* document type
* page number
* run configuration

Metadata allows filtering and improves retrieval precision.

---

# Retrieval Quality

The most important part of RAG is often:

```text
Retrieval quality
```

If the wrong chunks are retrieved, the LLM will produce weak answers.

Good RAG depends on:

* good chunking
* good embeddings
* metadata filtering
* reranking
* context management

---

# Prompt Grounding

The LLM should be instructed to answer using retrieved context.

Typical behavior:

```text
Use the provided context.
If the answer is not in the context, say that it is not available.
```

This reduces hallucinations.

---

# Context Window Management

Retrieved chunks must fit into the model context window.

Trade-offs:

* too little context → missing information
* too much context → noise and latency

Context engineering is a core RAG problem.

---

# Reranking

Reranking improves retrieval results after initial vector search.

Pipeline:

```text
Top 20 retrieved chunks
    ↓
Reranker
    ↓
Top 5 final chunks
```

This improves prompt quality.

---

# Hybrid Search

Hybrid search combines:

* vector search
* keyword search
* metadata filtering

It often performs better than vector search alone.

---

# Local RAG Advantages

## Privacy

Documents remain local.

---

## Cost Control

No token-based API costs.

---

## Offline Operation

The system can work without internet.

---

## Reproducibility

Models, embeddings, prompts, and indexes can be versioned locally.

---

## Full Control

Developers control every layer.

---

# Local RAG Limitations

## Hardware Constraints

Local systems are limited by:

* VRAM
* RAM
* CPU
* storage

---

## Lower Model Quality

Local models may be weaker than frontier cloud models.

---

## Maintenance Burden

The developer manages:

* models
* indexes
* storage
* updates
* evaluation

---

## Scaling Difficulty

Serving many users locally is difficult.

---

# Evaluation

RAG systems require evaluation.

Important questions:

* Did retrieval find the correct chunks?
* Did the model use the context?
* Was the answer grounded?
* Was the answer complete?
* Did hallucination occur?

Evaluation is essential for production readiness.

---

# Observability

Useful logs:

* retrieved chunks
* similarity scores
* prompt length
* generation latency
* model used
* embedding model used
* metadata filters

Without observability, RAG debugging is difficult.

---

# Common Failure Modes

## Bad Chunking

Important information is split poorly.

---

## Weak Embeddings

Semantic retrieval fails.

---

## Missing Metadata

Filtering becomes impossible.

---

## Too Much Context

Prompt becomes noisy and slow.

---

## Too Little Context

Answer lacks evidence.

---

## Hallucinations

Model generates unsupported claims.

---

# Scientific Local RAG

Scientific local RAG systems can index:

* papers
* equations
* experiment metadata
* analysis outputs
* plots descriptions
* lab notes
* documentation

This enables assistants that understand project-specific scientific knowledge.

---

# Example Scientific Query

```text
Which experiments show high scintillation but low beam wander?
```

A local RAG system could retrieve:

* experiment metadata
* analysis results
* relevant plots
* previous notes

and generate a grounded answer.

---

# Recommended Minimal Local RAG Stack

A practical first stack:

| Layer         | Tool                  |
| ------------- | --------------------- |
| LLM           | Ollama                |
| Embeddings    | bge-m3 through Ollama |
| Vector DB     | Qdrant                |
| RAG framework | LlamaIndex            |
| Backend       | FastAPI               |
| UI            | Streamlit             |

This stack is powerful enough for serious experimentation.

---

# Mental Models

Useful mental models:

```text
RAG = External memory for LLMs
```

```text
Vector DB = Semantic memory store
```

```text
Embeddings = Meaning encoded as geometry
```

```text
Prompt assembly = Packing evidence into working memory
```

---

# Relationship with AI Systems Engineering

Local RAG architecture combines:

* machine learning
* databases
* backend engineering
* information retrieval
* prompt engineering
* GPU inference
* observability

It is one of the clearest examples of AI systems engineering.

---

# Reflection

Local RAG architecture is much more than connecting a chatbot to documents.

It is a complete AI system architecture involving:

* ingestion
* indexing
* retrieval
* grounding
* generation
* evaluation
* observability
* deployment

Understanding local RAG means understanding how modern AI systems use external memory to become more accurate, private, reproducible, and useful in real-world domains.
