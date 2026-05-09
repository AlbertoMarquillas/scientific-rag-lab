# Serving and Deployment

## Introduction

Running a model locally is only the first step.

A real AI system also needs to expose the model to applications, users, services, and workflows.

This process is called:

```text
Serving and deployment
```

Serving and deployment define how an AI model becomes part of a usable software system.

---

# What Is Model Serving?

Model serving is:

```text
Making a model available for inference through an interface
```

Examples of interfaces:

* command line
* HTTP API
* WebSocket stream
* backend service
* internal microservice
* local desktop application

In Ollama, serving usually happens through its local API.

---

# What Is Deployment?

Deployment is:

```text
Running the AI system in an environment where it can be used reliably
```

Deployment includes:

* environment setup
* model installation
* API configuration
* hardware allocation
* monitoring
* security
* persistence
* update strategy

---

# Core Difference

| Concept    | Meaning                                               |
| ---------- | ----------------------------------------------------- |
| Running    | Executing a model manually                            |
| Serving    | Exposing the model through an interface               |
| Deployment | Operating the system reliably in a target environment |

Example:

```text
ollama run qwen2.5:7b
```

is running a model.

A FastAPI backend connected to Ollama is serving an AI application.

A monitored local RAG system with Qdrant, Ollama, and UI is a deployed system.

---

# Ollama as a Local Model Server

Ollama exposes a local server by default.

Default address:

```text
http://localhost:11434
```

This allows applications to send requests to local models.

Architecture:

```text
Application
    ↓
Ollama API
    ↓
Local Model
```

---

# Local Deployment Architecture

A simple local AI deployment may look like:

```text
Streamlit UI
    ↓
FastAPI Backend
    ↓
Ollama API
    ↓
Local LLM
```

For RAG:

```text
Streamlit UI
    ↓
FastAPI Backend
    ↓
Retriever
    ↓
Qdrant
    ↓
Ollama LLM
```

---

# Components in a Local RAG Deployment

| Component   | Role                   |
| ----------- | ---------------------- |
| Ollama      | Local inference server |
| Qdrant      | Vector database        |
| LlamaIndex  | RAG orchestration      |
| FastAPI     | Backend API            |
| Streamlit   | User interface         |
| .env        | Configuration          |
| Data folder | Persistent knowledge   |

Each component has a clear responsibility.

---

# Development vs Deployment

## Development

Focus:

* experimentation
* quick iteration
* debugging
* manual commands

Example:

```bash
ollama run qwen2.5:7b
```

---

## Deployment

Focus:

* reliability
* repeatability
* configuration
* monitoring
* user access

Example:

```text
Backend service + vector DB + local model runtime
```

---

# Localhost Deployment

The simplest deployment uses localhost.

Example:

```text
http://localhost:11434
```

Advantages:

* private
* simple
* safe for development
* no external exposure

Limitations:

* only usable from the same machine
* not suitable for multiple users

---

# LAN Deployment

A local AI system may be exposed to a local network.

Example:

```text
Other device → Local machine running Ollama
```

Useful for:

* lab networks
* internal demos
* local team tools

Requires additional security.

---

# Cloud Deployment

Ollama can also be deployed on a remote server.

Example:

```text
User → Web App → Remote GPU Server → Ollama
```

This requires:

* GPU server
* networking
* authentication
* monitoring
* security controls

Cloud deployment increases complexity.

---

# Containerized Deployment

AI systems are often deployed with containers.

Example components:

```text
Docker container: FastAPI
Docker container: Qdrant
Host service: Ollama
```

Containers improve:

* reproducibility
* portability
* environment control

GPU access must be configured carefully.

---

# Docker Compose Architecture

A local RAG system may use:

```text
Docker Compose
```

Conceptual services:

```text
fastapi
qdrant
streamlit
```

Ollama may run either:

* on the host machine
* inside a container

Host Ollama is often simpler on Windows.

---

# Environment Configuration

Deployment should avoid hardcoded values.

Typical `.env` values:

```env
OLLAMA_BASE_URL=http://localhost:11434
QDRANT_HOST=localhost
QDRANT_PORT=6333
LLM_MODEL=qwen2.5:7b
EMBED_MODEL=bge-m3
QDRANT_COLLECTION=documents
```

Configuration should be externalized.

---

# Model Availability

Before deployment, required models must be installed.

Example:

```bash
ollama pull qwen2.5:7b
ollama pull bge-m3
```

The application should fail clearly if required models are missing.

---

# Persistent Storage

Deployment requires persistent storage for:

* vector database data
* uploaded documents
* processed chunks
* logs
* configuration
* model cache

Without persistence, the system may lose indexed knowledge.

---

# Qdrant Persistence

Qdrant should store collections persistently.

Important data:

* vectors
* payloads
* indexes
* metadata

In production-like systems, Qdrant data should not be ephemeral.

---

# API Serving Layer

FastAPI often acts as the serving layer.

Example endpoints:

```text
POST /chat
POST /ingest
POST /search
GET /health
```

The API layer hides internal complexity from the UI.

---

# Health Checks

Useful health checks:

* Ollama reachable
* Qdrant reachable
* required model installed
* vector collection exists
* backend alive

Health checks improve reliability.

---

# Streaming Deployment

For chat systems, streaming responses improve usability.

Possible mechanisms:

* HTTP streaming
* Server-Sent Events
* WebSockets

Streaming requires backend support.

---

# Concurrency

Multiple simultaneous users increase complexity.

Challenges:

* GPU contention
* VRAM pressure
* request queuing
* latency spikes
* timeout handling

Local deployments usually support limited concurrency.

---

# Request Queues

For heavier systems, requests may be queued.

Benefits:

* prevents overload
* stabilizes GPU usage
* improves fairness

Trade-off:

```text
Queueing increases waiting time
```

---

# Security Considerations

If the system is exposed beyond localhost, security matters.

Important concerns:

* authentication
* authorization
* rate limiting
* input validation
* prompt injection
* API abuse
* data leakage

Local AI does not automatically mean secure AI.

---

# Access Control

Production systems should define who can:

* upload documents
* query documents
* delete indexes
* change models
* access logs

Access control becomes essential in multi-user systems.

---

# Observability

Deployment requires observability.

Useful logs:

* request latency
* retrieved chunks
* model used
* token count
* errors
* GPU utilization
* Qdrant query time

Without observability, debugging is difficult.

---

# Monitoring

Important metrics:

* VRAM usage
* GPU utilization
* tokens per second
* time to first token
* retrieval latency
* API error rate
* concurrent requests

Monitoring reveals bottlenecks.

---

# Versioning

Deployment should track:

* model name
* model tag
* embeddings model
* prompt version
* chunking configuration
* Qdrant collection version
* code version

This is critical for reproducibility.

---

# Model Updates

Updating models may change system behavior.

Possible effects:

* different answers
* different embeddings
* changed latency
* changed memory usage

Model updates should be tested before deployment.

---

# Embedding Model Changes

Changing the embedding model usually requires reindexing.

Reason:

```text
Vectors from different embedding models are not directly compatible
```

This is a critical deployment concern.

---

# Scaling Limits

Local deployment is limited by:

* GPU VRAM
* CPU performance
* RAM
* disk speed
* concurrency

Scaling beyond one machine requires more infrastructure.

---

# Production Deployment Challenges

Production AI systems require:

* reliability
* monitoring
* rollback strategies
* authentication
* data governance
* evaluation
* performance tuning

A working demo is not automatically production-ready.

---

# Deployment Failure Modes

## Ollama Not Running

The backend cannot reach the model server.

---

## Model Missing

The configured model has not been pulled.

---

## Qdrant Not Available

Retrieval fails.

---

## Collection Missing

The vector index has not been created.

---

## VRAM Exhaustion

The selected model is too large.

---

## Timeout Errors

Inference takes too long.

---

# Minimal Local Deployment Checklist

A practical checklist:

```text
Ollama installed
Required models pulled
Qdrant running
.env configured
FastAPI backend running
Streamlit UI running
Health checks passing
Test document ingested
Test query answered
```

This is a good first deployment target.

---

# Deployment Mindset

Deployment is not only about making code run.

It is about making the system:

* reliable
* reproducible
* observable
* maintainable
* secure
* usable

This is where AI projects become real software systems.

---

# Mental Models

Useful mental models:

```text
Ollama = Local inference server
```

```text
FastAPI = Application serving layer
```

```text
Qdrant = Persistent semantic memory
```

```text
Deployment = Turning an experiment into a usable system
```

---

# Relationship with AI Systems Engineering

Serving and deployment connect:

* model inference
* backend APIs
* vector databases
* user interfaces
* monitoring
* security
* configuration management

This is one of the clearest areas where AI becomes systems engineering.

---

# Reflection

Serving and deployment are what transform local AI from a personal experiment into a usable system.

A model running in a terminal is useful.

But a deployed AI system requires:

* stable APIs
* persistent storage
* configuration
* health checks
* observability
* security
* reproducibility

Understanding serving and deployment is therefore essential for building local AI systems that are not only impressive demos, but reliable tools.
