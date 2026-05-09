# Glossary

---

# Agent

AI system capable of:

```text
reasoning
planning
using tools
retrieving information
and executing actions
```

through iterative workflows.

---

# ANN (Approximate Nearest Neighbor)

Retrieval technique designed to:

```text
find approximately similar vectors efficiently
```

without exhaustive comparison.

Foundational for scalable vector retrieval.

---

# API

Application Programming Interface.

Mechanism allowing systems to:

```text
communicate programmatically
```

with other systems.

---

# Bi-Encoder

Embedding architecture where:

```text
query
and
document
```

are encoded independently into vectors.

Used heavily in scalable vector retrieval.

---

# Candidate Retrieval

Initial retrieval stage where:

```text
potentially relevant Nodes
```

are selected before reranking.

---

# Chat Engine

Conversational retrieval system combining:

```text
memory
retrieval
and LLM reasoning
```

for multi-turn interactions.

---

# Chunk

Small segment of a larger document.

Chunking improves:

* retrieval
* embedding quality
* context management

---

# Chunking

Process of splitting:

```text
Documents
```

into:

```text
smaller retrievable units
```

called:

```text
Nodes or chunks
```

---

# Collection

Logical grouping of vectors inside a vector database.

Examples:

```text
papers
experiments
notes
```

---

# Condense Question

Conversational retrieval technique where:

```text
conversation history
+
latest message
```

are rewritten into:

```text
standalone retrieval query
```

---

# Context Window

Maximum amount of information an LLM can process at once.

Measured in:

```text
tokens
```

---

# Cross-Encoder

Reranking architecture where:

```text
query + document
```

are processed jointly to estimate relevance.

Usually more accurate but slower than bi-encoders.

---

# Embedding

High-dimensional vector representation encoding:

```text
semantic meaning
```

of text, images, or other modalities.

---

# Embedding Drift

Changes in embedding behavior over time caused by:

* model updates
* ingestion changes
* chunking redesign

May silently degrade retrieval quality.

---

# Evaluation

Process of measuring:

```text
quality
reliability
and correctness
```

inside AI systems.

---

# Faithfulness

Measure of whether a generated response:

```text
accurately reflects retrieved evidence
```

without unsupported claims.

---

# Function Calling

Structured mechanism allowing LLMs to:

```text
invoke tools or APIs
```

reliably.

---

# Grounding

Property where generated outputs are:

```text
supported by retrieved evidence
```

instead of hallucinated.

---

# Hallucination

Generated content that is:

```text
fabricated
unsupported
or factually incorrect
```

relative to available evidence.

---

# HNSW

Hierarchical Navigable Small Worlds.

Graph-based ANN algorithm heavily used in:

* Qdrant
* Weaviate
* FAISS

for scalable vector retrieval.

---

# Hybrid Retrieval

Retrieval architecture combining:

```text
semantic retrieval
+
keyword retrieval
+
metadata filtering
```

for improved retrieval quality.

---

# Idempotency

Property where:

```text
repeating the same operation
```

does not corrupt system state.

Critical for workflows and retries.

---

# Ingestion Pipeline

Pipeline responsible for:

* loading data
* chunking
* embedding generation
* indexing
* metadata propagation

---

# LLM

Large Language Model.

Neural network trained to:

```text
predict and generate language
```

using large-scale datasets.

---

# Memory

Stored information accessible to an AI system.

Examples:

* conversational memory
* vector databases
* retrieval memory
* workflow state

---

# Metadata

Structured information describing content.

Examples:

```text
run_id
module_name
fps
experiment_date
```

Metadata enables:

* filtering
* routing
* traceability

---

# Metadata Filtering

Retrieval constrained using:

```text
structured metadata conditions
```

in addition to semantic similarity.

---

# Multimodal Retrieval

Retrieval involving multiple modalities.

Examples:

* text
* images
* plots
* audio
* video

---

# Node

Fundamental retrievable unit inside LlamaIndex.

Usually created from:

```text
chunked document segments
```

plus metadata.

---

# Observability

Ability to:

```text
monitor
trace
inspect
and debug
```

AI system behavior.

---

# Payload

Metadata stored alongside vectors inside vector databases.

Especially important in:

```text
Qdrant
```

---

# Persistence

Property where data survives:

```text
restarts
sessions
or crashes
```

---

# Prompt Injection

Malicious attempt to manipulate:

```text
LLM instructions
or retrieval behavior
```

through crafted inputs.

---

# Query Engine

LlamaIndex abstraction responsible for:

```text
retrieval
context assembly
and response generation
```

for user queries.

---

# Query Rewriting

Process of transforming a query into:

```text
better retrieval-oriented form
```

using:

* conversation context
* metadata
* retrieval goals

---

# Qdrant

Vector database optimized for:

* semantic retrieval
* metadata filtering
* ANN search
* scalable vector storage

---

# RAG (Retrieval-Augmented Generation)

Architecture combining:

```text
retrieval
+
LLM generation
```

so answers are grounded in external information.

---

# Recall

Retrieval metric measuring:

```text
whether relevant information was retrieved
```

---

# ReAct

Agent pattern combining:

```text
Reasoning
+
Acting
```

through iterative execution loops.

---

# Reranking

Process of:

```text
reordering retrieved results
```

using stronger relevance estimation.

---

# Response Synthesis

Process of generating:

```text
final coherent response
```

from retrieved Nodes.

---

# Retrieval

Process of locating:

```text
relevant information
```

for a query.

---

# Retrieval Precision

Measure of:

```text
how many retrieved results
are actually relevant
```

---

# Scientific RAG

Application of:

```text
retrieval-augmented generation
```

to:

```text
scientific knowledge
and experimental systems
```

---

# Semantic Retrieval

Retrieval based on:

```text
semantic similarity
```

instead of exact keyword matching.

---

# Similarity Search

Search mechanism identifying:

```text
vectors close in embedding space
```

---

# Streaming

Technique where responses are:

```text
generated progressively
```

instead of waiting for full completion.

---

# Tool

External capability accessible to agents.

Examples:

* retrievers
* APIs
* calculators
* databases
* workflows

---

# Trace

Execution path followed through:

```text
multiple system components
```

Useful for debugging and observability.

---

# Vector

Numerical representation inside embedding space.

Embeddings are vectors.

---

# Vector Database

Database specialized in:

```text
storing
indexing
and retrieving
vectors
```

Examples:

* Qdrant
* Pinecone
* Weaviate

---

# Vector Store

Infrastructure layer responsible for:

```text
semantic vector storage
and retrieval
```

Often implemented using vector databases.

---

# Workflow

Structured orchestration pipeline coordinating:

* execution
* retries
* state
* events
* AI operations

---

# Workflow Orchestration

Coordination of:

```text
multi-step execution pipelines
```

across distributed systems.

---

# Key Insight

Modern LlamaIndex ecosystems fundamentally combine:

```text
Documents
+
Nodes
+
embeddings
+
vector databases
+
retrieval
+
reranking
+
metadata filtering
+
workflows
+
agents
+
observability
+
LLM reasoning
```

to create scalable retrieval-augmented AI systems.
