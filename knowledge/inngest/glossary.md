# Glossary

---

# Agent

An AI system capable of:

* reasoning
* planning
* calling tools
* executing workflows
* interacting with external systems

Agents are usually workflow-oriented systems.

---

# API

Application Programming Interface.

A mechanism allowing systems to communicate programmatically.

Example:

```text
workflow
→ calls embedding API
```

---

# Asynchronous Execution

Execution that does not block waiting for completion.

Example:

```text
trigger workflow
→ continue execution elsewhere
```

Important in distributed systems.

---

# Backoff

Retry strategy where wait time increases after failures.

Example:

```text
1s → 2s → 4s → 8s
```

Used to reduce overload.

---

# Backpressure

Mechanism slowing incoming work when downstream systems are overloaded.

Prevents:

* overload
* queue collapse
* cascading failures

---

# Chunk

A smaller piece of a document used for embeddings and retrieval.

RAG systems retrieve chunks rather than entire documents.

---

# Chunking

Process of splitting large content into smaller semantic units.

Critical for:

* retrieval quality
* embedding coherence
* context preservation

---

# Concurrency

Multiple workflows or tasks executing simultaneously.

Example:

```text
5 embedding workflows running at once
```

---

# Concurrency Limit

Restriction controlling how many tasks may execute simultaneously.

Used to protect:

* APIs
* GPUs
* databases
* infrastructure

---

# Context Window

Maximum amount of information an LLM can process at once.

Limited context windows motivate RAG systems.

---

# Durable Execution

Execution model where workflow state persists across failures.

Allows:

* retries
* recovery
* resuming execution

without restarting entire workflows.

---

# Embedding

Vector representation of data capturing semantic meaning.

Used for:

* semantic search
* retrieval
* similarity comparison

---

# Event

A record representing:

```text
something happened
```

Examples:

```text
paper.uploaded
experiment.completed
```

Events trigger workflows.

---

# Event-Driven System

A system where workflows react to emitted events.

Example:

```text
document uploaded
→ ingestion workflow triggered
```

---

# Function

An execution unit reacting to events or schedules.

Functions orchestrate workflow logic.

---

# Hallucination

When an AI model generates:

* incorrect information
* fabricated facts
* unsupported claims

RAG attempts to reduce hallucinations through retrieval grounding.

---

# Hybrid Search

Retrieval combining:

* dense retrieval (embeddings)
* sparse retrieval (keywords/BM25)

Improves retrieval robustness.

---

# Idempotency

Property where repeated execution does not corrupt state.

Important for:

* retries
* workflow replay
* distributed systems

---

# Ingestion

Process of transforming raw data into retrievable knowledge.

Typical stages:

```text
parse
→ chunk
→ embed
→ index
```

---

# LLM

Large Language Model.

Examples:

* GPT
* Claude
* Gemini
* Llama

LLMs generate language based on learned statistical patterns.

---

# Metadata

Structured information attached to data.

Examples:

```text
author
year
run_id
experiment_id
```

Metadata enables filtering and traceability.

---

# Multimodal

Systems capable of processing multiple modalities.

Examples:

* text
* images
* audio
* video
* plots

---

# Observability

Ability to understand internal system behavior through:

* logs
* metrics
* traces

Critical for production systems.

---

# Orchestration

Coordinating workflows, steps, retries, and execution logic.

Modern AI systems rely heavily on orchestration.

---

# Parsing

Extracting structured information from raw files.

Examples:

* PDF parsing
* OCR
* metadata extraction

---

# Prompt Injection

Security attack where malicious instructions are embedded into retrieved content.

Major risk in RAG and agentic systems.

---

# Queue

Structure temporarily storing pending work.

Queues stabilize distributed systems.

---

# RAG

Retrieval-Augmented Generation.

Architecture where LLMs retrieve external knowledge before generating responses.

Typical pipeline:

```text
retrieve
→ augment context
→ generate answer
```

---

# Rate Limit

Restriction controlling how frequently requests may occur.

Examples:

```text
100 requests/minute
```

Used to protect infrastructure.

---

# Reranking

Secondary ranking stage improving retrieval quality.

Rerankers reorder retrieved candidates using more advanced models.

---

# Retry

Attempting execution again after failure.

Retries improve reliability in distributed systems.

---

# Scheduling

Executing workflows automatically at specific times or intervals.

Examples:

```text
Every hour
Every day
```

---

# Semantic Search

Retrieval based on meaning rather than exact keywords.

Powered by embeddings.

---

# Sparse Retrieval

Keyword-based retrieval.

Examples:

* BM25
* TF-IDF

Often combined with vector search.

---

# Step

A smaller execution unit inside a workflow.

Steps enable:

* retries
* observability
* durable execution

---

# Trace

Representation of execution flow across workflows and systems.

Useful for debugging distributed systems.

---

# Vector

Numerical representation in high-dimensional space.

Embeddings are vectors.

---

# Vector Database

Database specialized for storing and searching embeddings.

Examples:

* Qdrant
* Pinecone
* Weaviate
* Chroma

---

# Vector Search

Retrieval based on vector similarity.

Core mechanism behind semantic search.

---

# Workflow

An orchestrated sequence of steps executed to achieve a goal.

Workflows often contain:

* retries
* observability
* concurrency control
* scheduling
* durable execution

---

# Workflow Replay

Re-executing workflows or events.

Useful for:

* debugging
* recovery
* rebuilding indexes
* regenerating embeddings

---

# Workflow Trace

Visual or logical representation of workflow execution.

Example:

```text
Event
→ Step 1
→ Retry Step 2
→ Step 3
```

---

# Key Insight

Modern AI systems increasingly combine:

```text
RAG
+
workflows
+
retrieval
+
observability
+
orchestration
+
agents
+
automation
```
