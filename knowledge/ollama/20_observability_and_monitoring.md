# Observability and Monitoring

## Introduction

Building a local AI system is not only about making the model answer questions.

A real system must also be observable.

Observability means understanding what the system is doing internally.

Monitoring means continuously tracking whether the system is healthy, fast, and reliable.

Together, observability and monitoring are essential for:

* debugging
* performance optimization
* reliability
* production readiness
* RAG evaluation
* scientific reproducibility

---

# What Is Observability?

Observability is the ability to answer questions such as:

```text
What happened inside the system?
```

```text
Why did this answer fail?
```

```text
Which chunks were retrieved?
```

```text
How much GPU memory was used?
```

```text
Where is the bottleneck?
```

Observability makes internal behavior inspectable.

---

# What Is Monitoring?

Monitoring is the continuous collection of system signals.

Examples:

* latency
* errors
* GPU usage
* VRAM usage
* token generation speed
* retrieval latency
* request volume

Monitoring helps detect problems before they become failures.

---

# Observability vs Monitoring

| Concept       | Purpose                       |
| ------------- | ----------------------------- |
| Observability | Understand internal behavior  |
| Monitoring    | Track system health over time |

Monitoring tells that something is wrong.

Observability helps explain why.

---

# Why This Matters in Local AI

Local AI systems involve many components:

* Ollama
* local LLMs
* embeddings models
* Qdrant
* LlamaIndex
* FastAPI
* Streamlit
* GPU hardware
* storage

A failure can happen at any layer.

Without observability, debugging becomes guesswork.

---

# Local AI System Signals

Important signals include:

* model name
* prompt size
* context size
* retrieved chunks
* similarity scores
* generation latency
* tokens per second
* VRAM usage
* GPU utilization
* Qdrant query time
* API errors

These signals explain system behavior.

---

# Observability in Ollama

For Ollama-based systems, useful observations include:

* which model was used
* whether the model was cold or warm
* generation latency
* time to first token
* total tokens generated
* context length
* error messages
* memory pressure

This helps diagnose inference problems.

---

# GPU Monitoring

GPU monitoring is essential for local AI.

Common tool:

```bash
nvidia-smi
```

Useful metrics:

* VRAM usage
* GPU utilization
* temperature
* power draw
* active processes

These metrics show whether the hardware is the bottleneck.

---

# VRAM Monitoring

VRAM is often the primary local AI constraint.

Monitor:

* total VRAM
* used VRAM
* free VRAM
* model memory footprint
* KV cache growth

VRAM exhaustion causes slowdowns or failures.

---

# Latency Monitoring

Latency should be measured across the full pipeline.

Typical components:

```text
User request
    ↓
Backend processing
    ↓
Retrieval
    ↓
Prompt assembly
    ↓
LLM inference
    ↓
Response streaming
```

Each stage should be measurable.

---

# Time To First Token

A key metric:

```text
TTFT = Time To First Token
```

High TTFT may indicate:

* cold model loading
* very large prompts
* slow retrieval
* GPU overload
* backend overhead

TTFT strongly affects user experience.

---

# Tokens Per Second

Another key metric:

```text
TPS = Tokens Per Second
```

Low TPS may indicate:

* oversized model
* CPU inference
* long context
* thermal throttling
* weak quantization choice

TPS measures generation throughput.

---

# Retrieval Observability

In RAG systems, retrieval must be observable.

Log:

* query text
* retrieved chunk IDs
* similarity scores
* metadata filters
* source documents
* final selected chunks

This is essential because many RAG failures are retrieval failures.

---

# Prompt Observability

Prompt assembly should be inspectable.

Useful information:

* system prompt version
* retrieved context length
* number of chunks
* total token count
* conversation history included
* final prompt structure

Prompt observability helps debug hallucinations and missing context.

---

# Generation Observability

Useful generation logs:

* model used
* temperature
* top_p
* top_k
* context size
* stop reason
* generated token count
* response latency

This helps reproduce model behavior.

---

# Qdrant Monitoring

For Qdrant, monitor:

* collection size
* vector count
* query latency
* payload size
* indexing status
* memory usage
* disk usage

A slow vector database slows the entire RAG system.

---

# Collection Health

Important checks:

* collection exists
* vector dimensions match embedding model
* payload fields exist
* indexes are built
* expected document count is present

Collection health prevents silent retrieval errors.

---

# Embeddings Monitoring

Monitor embeddings pipelines:

* embedding model used
* vector dimension
* embedding latency
* ingestion throughput
* failed documents
* skipped chunks

Changing embeddings models requires reindexing.

---

# Ingestion Observability

Ingestion should log:

* files loaded
* documents parsed
* chunks created
* chunks embedded
* vectors inserted
* errors
* metadata attached

Without this, it is hard to know whether the knowledge base is complete.

---

# Health Checks

A local AI system should expose health checks.

Examples:

```text
GET /health
```

Health checks may verify:

* FastAPI running
* Ollama reachable
* Qdrant reachable
* required models installed
* collection exists

---

# Error Logging

Log errors clearly.

Examples:

* Ollama connection refused
* model not found
* Qdrant unavailable
* collection missing
* vector dimension mismatch
* context overflow
* timeout

Good error messages reduce debugging time.

---

# Structured Logs

Structured logs are easier to analyze.

Example fields:

```text
request_id
model
latency_ms
retrieved_chunks
qdrant_latency_ms
tokens_generated
error_type
```

Structured logs are better than unstructured print statements.

---

# Request IDs

Each request should have an identifier.

Purpose:

```text
Trace one user query across the full system
```

This helps connect:

* frontend event
* backend request
* retrieval call
* Ollama generation
* final response

---

# Tracing

Tracing follows a request through multiple components.

Example trace:

```text
UI → FastAPI → Retriever → Qdrant → Prompt Assembly → Ollama → Stream
```

Tracing is very useful in multi-component AI systems.

---

# Metrics

Metrics are numerical measurements collected over time.

Examples:

* average latency
* p95 latency
* error rate
* GPU utilization
* requests per minute
* average retrieved chunks
* average prompt size

Metrics help detect trends.

---

# Dashboards

Dashboards visualize system health.

Useful panels:

* request latency
* retrieval latency
* GPU memory
* tokens per second
* error rate
* Qdrant query time
* collection size

Dashboards are especially useful during experiments.

---

# Alerts

Alerts notify when something goes wrong.

Examples:

* VRAM usage too high
* Qdrant unavailable
* error rate spike
* latency too high
* disk almost full

Alerts are important for production systems.

---

# Evaluation Logs

RAG systems need evaluation logs.

Track:

* question
* retrieved chunks
* expected answer
* generated answer
* correctness
* hallucination flags
* human feedback

This supports continuous improvement.

---

# Hallucination Debugging

When a model hallucinates, inspect:

* retrieved context
* prompt instructions
* model parameters
* temperature
* missing metadata
* chunk quality

Most hallucination debugging starts with retrieval inspection.

---

# Reproducibility Logging

For reproducible AI systems, log:

* model name and tag
* embedding model
* prompt version
* chunk size
* chunk overlap
* vector collection version
* generation parameters

This is especially important for scientific systems.

---

# Scientific AI Observability

Scientific systems require stronger traceability.

Important records:

* source documents
* experiment IDs
* retrieval evidence
* analysis version
* model version
* generated claims

This supports verification and auditability.

---

# Privacy Considerations

Logs may contain sensitive information.

Be careful logging:

* user prompts
* documents
* retrieved chunks
* personal data
* confidential research

Local AI systems still need data governance.

---

# Common Failure Modes

## No Retrieval Logs

Impossible to debug bad answers.

---

## No Model Version Tracking

Results cannot be reproduced.

---

## No GPU Monitoring

Performance bottlenecks are unclear.

---

## Silent Ingestion Failures

Documents appear indexed but are missing.

---

## Unstructured Logs

Debugging becomes slow and messy.

---

# Minimal Monitoring Checklist

A practical first checklist:

```text
Log model name
Log embedding model
Log retrieved chunks
Log similarity scores
Log prompt token count
Log generation latency
Log Qdrant latency
Monitor VRAM with nvidia-smi
Expose /health endpoint
Track ingestion success/failure
```

This is enough for a serious first local RAG system.

---

# Mental Models

Useful mental models:

```text
Observability = Seeing inside the AI system
```

```text
Monitoring = Watching system health over time
```

```text
RAG debugging = Retrieval debugging first
```

```text
Reproducibility = Logging every important configuration
```

---

# Relationship with AI Systems Engineering

Observability and monitoring connect:

* model inference
* retrieval systems
* databases
* APIs
* GPU hardware
* user experience
* reliability

They transform AI systems from demos into maintainable engineering systems.

---

# Reflection

An AI system that cannot be observed cannot be trusted.

For local RAG systems, observability is especially important because failures may happen in many places:

* bad chunking
* bad retrieval
* missing metadata
* model hallucination
* VRAM pressure
* slow Qdrant queries
* prompt overflow

Monitoring and observability make these failures visible.

They are therefore essential for building local AI systems that are reliable, debuggable, reproducible, and scientifically useful.
