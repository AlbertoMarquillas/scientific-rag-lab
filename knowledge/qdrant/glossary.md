# Glossary

---

# A

## ANN

Approximate Nearest Neighbor.

Technique used to perform scalable vector retrieval without exhaustive search.

Core idea:

```text
fast approximate similarity search
```

Widely used in:

* Qdrant
* Pinecone
* Milvus
* FAISS

---

# B

## BM25

Traditional keyword retrieval algorithm.

Uses:

* term frequency
* inverse document frequency
* document length normalization

Very important in:

```text
hybrid retrieval
```

---

# C

## Candidate Retrieval

Initial retrieval stage that generates:

```text
possible relevant results
```

Often followed by:

```text
reranking
```

---

## Chunk

A smaller semantic unit extracted from a larger document.

Chunks are embedded individually.

Chunk quality strongly affects retrieval quality.

---

## Chunking

Process of splitting information into chunks.

Important for:

* embeddings
* retrieval precision
* context management

---

## CLIP

Contrastive Language–Image Pretraining.

Multimodal model that aligns:

* text embeddings
* image embeddings

inside a shared semantic space.

---

## Collection

Primary organizational unit inside Qdrant.

A collection stores:

* vectors
* payloads
* indexes
* retrieval configuration

---

## Concurrency

Ability of a system to handle:

```text
multiple simultaneous operations
```

Important for:

* workflows
* retrieval
* ingestion
* APIs

---

## Context Window

Maximum amount of information an LLM can process at once.

RAG systems retrieve:

```text
most relevant context
```

to fit inside this limit.

---

## Cross-Modal Retrieval

Retrieval across modalities.

Example:

```text
text query
→ retrieve images
```

---

# D

## Dead-Letter Queue

Queue storing tasks that repeatedly fail.

Used in workflow systems to isolate failures.

---

## Distributed System

System operating across:

```text
multiple machines or nodes
```

Modern retrieval systems increasingly become distributed systems.

---

## Drift

Gradual change in system behavior over time.

Examples:

* embedding drift
* semantic drift
* retrieval drift

---

# E

## Embedding

Numerical vector representation of information.

Embeddings approximate:

```text
semantic meaning
```

---

## Embedding Drift

Change in embedding behavior caused by:

* model updates
* dataset evolution
* reindexing

May degrade retrieval quality.

---

## Embedding Model

Model generating embeddings.

Examples:

* OpenAI embeddings
* BGE
* E5
* sentence-transformers

---

## Event-Driven Architecture

Architecture based on:

```text
events triggering workflows
```

Widely used in:

* ingestion systems
* workflow orchestration
* AI pipelines

---

# F

## Failure Mode

Specific way a system may fail.

Examples:

* hallucinations
* weak retrieval
* workflow collapse
* metadata corruption

---

## Filtering

Restricting retrieval using:

```text
structured metadata conditions
```

---

# G

## Grounding

Using external retrieved information to support LLM outputs.

Grounded systems attempt to reduce hallucinations.

---

# H

## Hallucination

LLM-generated content unsupported by:

* retrieved context
* facts
* source material

RAG reduces hallucinations but does not eliminate them.

---

## HNSW

Hierarchical Navigable Small Worlds.

Graph-based ANN indexing algorithm widely used in vector databases.

Core idea:

```text
efficient graph navigation
for nearest-neighbor retrieval
```

---

## Hybrid Retrieval

Combining:

* vector search
* keyword retrieval
* metadata filtering
* reranking

inside one retrieval pipeline.

---

# I

## Idempotency

Property where repeating an operation:

```text
does not create inconsistent results
```

Important for:

* retries
* ingestion workflows
* distributed systems

---

## Index

Data structure enabling efficient retrieval.

Qdrant commonly uses:

```text
ANN indexes
```

---

## Ingestion Pipeline

Pipeline responsible for:

* parsing
* chunking
* embedding
* storing

information inside retrieval systems.

---

# K

## Keyword Search

Traditional retrieval based on:

```text
exact lexical matching
```

Examples:

* BM25
* TF-IDF

---

# L

## Latency

Time required to complete an operation.

Examples:

* retrieval latency
* embedding latency
* API latency

---

## LLM

Large Language Model.

Models capable of:

* generation
* reasoning
* summarization
* conversation

Examples:

* GPT
* Claude
* Gemini

---

## Logs

Structured records of system events.

Important for:

* debugging
* observability
* auditing

---

# M

## Metadata

Structured information attached to retrievable objects.

Examples:

```text
run_id
fps
module_name
heater_voltage
```

Metadata enables:

* filtering
* traceability
* reproducibility

---

## Metrics

Numerical measurements describing system behavior.

Examples:

* latency
* throughput
* recall
* precision

---

## Multimodal Retrieval

Retrieval across multiple modalities.

Examples:

* text
* images
* plots
* audio

---

# N

## Nearest Neighbor Search

Finding vectors closest to a query vector.

Core operation behind semantic retrieval.

---

# O

## Observability

Ability to understand system behavior through:

* logs
* metrics
* traces

Essential for production systems.

---

# P

## Payload

Metadata attached to a Qdrant point.

Payloads support:

* filtering
* retrieval control
* traceability

---

## Point

Basic retrievable object inside Qdrant.

Usually contains:

```text
ID
+
vector
+
payload
```

---

## Precision

Retrieval metric describing:

```text
how many retrieved results are relevant
```

---

## Prompt Injection

Attack where retrieved or user-provided content attempts to manipulate LLM behavior.

Important security concern in RAG systems.

---

# Q

## Qdrant

Vector database specialized for:

* semantic retrieval
* ANN search
* metadata filtering
* scalable vector infrastructure

Widely used in modern RAG systems.

---

## Query Embedding

Embedding generated from a user query.

Used for semantic retrieval.

---

# R

## RAG

Retrieval-Augmented Generation.

Architecture combining:

```text
retrieval
+
LLM generation
```

---

## Recall

Retrieval metric describing:

```text
how many relevant results are retrieved
```

---

## Reindexing

Regenerating retrieval infrastructure.

Reasons:

* new embeddings
* better chunking
* metadata redesign

---

## Reranking

Secondary ranking stage applied after retrieval.

Goal:

```text
improve retrieval quality
```

---

## Retrieval

Finding relevant information for a query.

Modern retrieval often combines:

* embeddings
* metadata
* hybrid search

---

## Retrieval Drift

Gradual degradation of retrieval behavior over time.

Causes:

* evolving datasets
* embedding changes
* metadata inconsistency

---

# S

## Scalability

Ability of a system to handle growing workload efficiently.

Important dimensions:

* latency
* throughput
* storage
* concurrency

---

## Scientific Retrieval

Semantic retrieval specialized for:

* experiments
* scientific observations
* multimodal scientific data

---

## Semantic Memory

Retrieval infrastructure acting as:

```text
persistent semantic knowledge storage
```

for AI systems.

---

## Semantic Retrieval

Retrieval based on:

```text
semantic similarity
```

rather than exact keywords.

---

## Semantic Search

Another term for semantic retrieval.

---

## Sharding

Distributing data across multiple machines.

Used for:

* scalability
* distributed retrieval
* workload balancing

---

## Similarity Search

Finding semantically close vectors.

Core mechanism behind vector databases.

---

## Structured Logging

Logs organized into machine-readable fields.

Improves:

* observability
* debugging
* analysis

---

# T

## Throughput

Amount of work completed per unit of time.

Examples:

* queries per second
* ingestion throughput

---

## Tracing

Tracking request flow through distributed systems.

Important for:

* debugging
* observability
* latency analysis

---

# V

## Vector

High-dimensional numerical representation of information.

Vectors approximate semantic meaning.

---

## Vector Database

Database specialized for:

* vector storage
* nearest-neighbor retrieval
* semantic search
* metadata filtering

---

## Vector Search

Retrieval based on vector similarity.

Core operation behind semantic retrieval.

---

# W

## Workflow

Coordinated sequence of operations.

Examples:

* ingestion
* embedding generation
* reindexing
* retrieval pipelines

---

## Workflow Orchestration

Managing distributed workflows.

Examples:

* retries
* scheduling
* concurrency
* event handling

---

# Final Perspective

This glossary describes the conceptual foundations behind:

```text
modern retrieval systems
semantic memory
RAG infrastructure
multimodal AI systems
scientific retrieval
production AI engineering
```

Understanding these concepts together provides a strong mental model for modern AI systems engineering.
