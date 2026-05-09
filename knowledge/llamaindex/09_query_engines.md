# Query Engines

---

# What is a Query Engine?

A Query Engine is the component responsible for:

```text
coordinating retrieval
+
context assembly
+
LLM generation
```

inside a retrieval-augmented AI system.

Query Engines are one of the central orchestration layers in LlamaIndex.

---

# Core Idea

A retriever finds:

```text
relevant information
```

A Query Engine transforms that retrieval into:

```text
a grounded answer
```

Query Engines connect:

```text
retrieval
↔
LLM reasoning
```

---

# High-Level Mental Model

Typical flow:

```text
user query
      ↓
Query Engine
      ↓
Retriever
      ↓
relevant Nodes
      ↓
context assembly
      ↓
LLM
      ↓
grounded response
```

The Query Engine orchestrates the full retrieval-generation loop.

---

# Why Query Engines Exist

Retrieval alone is insufficient.

The system must also:

* retrieve information
* organize context
* manage token limits
* construct prompts
* interact with the LLM
* synthesize responses

Query Engines coordinate these stages.

---

# Relationship with Retrievers

Conceptually:

```text
Retriever
→ finds information

Query Engine
→ uses retrieved information
   to generate answers
```

Retrievers are retrieval components.

Query Engines are orchestration components.

---

# Query Engines in LlamaIndex

In LlamaIndex:

```text
Index
      ↓
.as_query_engine()
      ↓
Query Engine
```

This creates a high-level retrieval interface.

---

# Why Query Engines Matter

Modern RAG systems are not only:

```text
vector search systems
```

They are:

```text
retrieval + reasoning systems
```

Query Engines coordinate this interaction.

---

# Core Responsibilities

A Query Engine commonly handles:

* query interpretation
* retriever execution
* metadata filtering
* top-k selection
* context assembly
* prompt construction
* LLM calls
* response synthesis

It orchestrates the retrieval pipeline.

---

# Typical Query Pipeline

Conceptually:

```text
user query
      ↓
query embedding
      ↓
Retriever
      ↓
retrieve Nodes
      ↓
assemble context
      ↓
prompt construction
      ↓
LLM reasoning
      ↓
response synthesis
```

This is the core RAG query loop.

---

# Retrieval Stage

The Query Engine usually delegates retrieval to:

```text
retrievers
```

Possible retrieval strategies:

* vector retrieval
* keyword retrieval
* hybrid retrieval
* recursive retrieval
* metadata filtering
* reranking

The Query Engine coordinates retrieval behavior.

---

# Context Assembly

After retrieval:

```text
retrieved Nodes
```

must be assembled into:

```text
LLM context
```

This stage is extremely important.

---

# Why Context Assembly Matters

LLMs reason over:

```text
prompt context
```

not directly over the vector database.

Weak context assembly may produce:

* fragmented reasoning
* missing information
* hallucinations
* contradictory context

---

# Prompt Construction

The Query Engine typically builds prompts using:

* retrieved Nodes
* system instructions
* query text
* metadata
* synthesis templates

Prompt construction strongly affects answer quality.

---

# Query Engines and Grounding

The purpose of retrieval is:

```text
grounding
```

Meaning:

```text
answers should rely on retrieved context
```

instead of pure parametric memory.

Query Engines help enforce grounding.

---

# Response Synthesis

After retrieval:

the Query Engine synthesizes:

```text
multiple retrieved Nodes
```

into:

```text
a coherent answer
```

This process is called:

```text
response synthesis
```

---

# Query Engines vs Chat Engines

Important distinction.

## Query Engine

Typically:

```text
single query
→ retrieve
→ answer
```

---

## Chat Engine

Adds:

* conversation memory
* dialogue continuity
* chat history
* contextual accumulation

Chat Engines extend Query Engines.

---

# Stateless Nature

Most Query Engines are fundamentally:

```text
stateless
```

Meaning:

```text
each query is processed independently
```

Conversation memory usually belongs to Chat Engines.

---

# Query Understanding

Some Query Engines may perform:

* query rewriting
* query decomposition
* query expansion
* routing
* reformulation

before retrieval.

This improves retrieval quality.

---

# Multi-Step Querying

Advanced Query Engines may perform:

```text
retrieve
→ analyze
→ retrieve again
→ synthesize
```

This enables more complex reasoning.

---

# Recursive Querying

Some systems recursively retrieve:

```text
high-level summaries first
```

then:

```text
detailed Nodes
```

This improves scalability and context management.

---

# Query Decomposition

Complex questions may be decomposed into:

```text
smaller subqueries
```

Example:

```text
compare scintillation and beam wander
across strong turbulence experiments
```

may become:

```text
subquery 1 → scintillation
subquery 2 → beam wander
subquery 3 → experiment comparison
```

The Query Engine coordinates these retrievals.

---

# Metadata-Aware Querying

Query Engines may apply:

```text
metadata constraints
```

Example:

```text
retrieve experiments
WHERE:
module_name = optical_turbulence
```

Metadata-aware retrieval improves precision.

---

# Top-K Retrieval

Most Query Engines retrieve:

```text
top-k Nodes
```

Tradeoff:

```text
larger k
→ richer context

smaller k
→ cleaner context
```

Top-k strongly affects RAG behavior.

---

# Similarity Thresholding

Some systems discard Nodes below:

```text
minimum similarity thresholds
```

This helps reduce:

* noisy retrieval
* irrelevant context
* hallucination risk

---

# Query Engines and Context Windows

LLMs have limited:

```text
context windows
```

The Query Engine must decide:

```text
which information fits into context
```

This is fundamentally a:

```text
context selection problem
```

---

# Token Budgeting

The Query Engine may manage:

* chunk counts
* prompt size
* retrieval limits
* compression
* summaries

This is necessary for scalable RAG.

---

# Query Engines and Hallucinations

Weak retrieval orchestration may cause:

* unsupported answers
* missing evidence
* contradictory context
* hallucinations

Grounding quality strongly depends on Query Engine behavior.

---

# Query Engines and Reranking

Modern Query Engines often combine:

```text
retrieval
+
reranking
```

Pipeline:

```text
retrieve candidates
      ↓
rerank candidates
      ↓
assemble final context
```

Reranking improves retrieval precision.

---

# Hybrid Query Engines

Modern systems increasingly combine:

* vector retrieval
* keyword retrieval
* metadata filtering
* reranking
* query rewriting

Pure vector retrieval is often insufficient.

---

# Router Query Engines

Some systems route queries dynamically.

Example:

```text
scientific query
→ scientific retriever

image query
→ multimodal retriever
```

Routing improves specialization.

---

# Multi-Index Querying

Large systems may query across:

* papers
* experiments
* notes
* reports
* plots

The Query Engine may merge results from multiple indexes.

---

# Federated Retrieval

Advanced systems may retrieve from:

```text
multiple independent knowledge sources
```

Examples:

* local vector database
* APIs
* cloud retrieval systems
* scientific repositories

Query Engines increasingly orchestrate distributed retrieval.

---

# Streaming Responses

Some Query Engines support:

```text
streaming generation
```

Meaning:

```text
tokens are returned progressively
```

instead of waiting for the full answer.

Streaming improves perceived latency.

---

# Query Engines and Agents

Agents often use Query Engines as:

```text
retrieval tools
```

Example:

```text
Agent
→ asks Query Engine
→ receives grounded context
→ reasons further
```

Query Engines become part of agent cognition.

---

# Scientific Query Engines

Scientific systems may retrieve:

* experiment summaries
* turbulence analyses
* comparison reports
* morphology observations
* statistical analyses
* scientific notes

Scientific querying is often metadata-heavy.

---

# Example Scientific Query

Example:

```text
Find experiments showing:
strong scintillation
with centroid instability
```

Possible pipeline:

```text
query
      ↓
metadata-aware retrieval
      ↓
reranking
      ↓
scientific context assembly
      ↓
LLM-assisted interpretation
```

---

# Your Project as a Query System

Your project naturally generates:

```text
analysis.json
comparison reports
scientific summaries
module outputs
metadata-rich analyses
```

These become ideal retrieval objects for Query Engines.

---

# Example Future Architecture

Possible future pipeline:

```text
scientific query
      ↓
LlamaIndex Query Engine
      ↓
Qdrant retrieval
      ↓
retrieve experiment Nodes
      ↓
LLM scientific reasoning
      ↓
grounded scientific answer
```

This creates semantic scientific exploration.

---

# Query Engines and Observability

Production systems should monitor:

* retrieval latency
* prompt size
* token usage
* retrieval quality
* hallucination frequency
* failed retrievals

Query Engines require observability.

---

# Query Evaluation

Query systems should be evaluated.

Possible metrics:

* grounding quality
* relevance
* faithfulness
* latency
* hallucination rate
* retrieval precision

Evaluation is essential.

---

# Scalability

Large Query Engine systems may involve:

* millions of Nodes
* distributed retrieval
* multimodal context
* agent orchestration
* continuous ingestion

Query orchestration becomes infrastructure.

---

# Failure Modes

Common failures:

* weak retrieval
* poor prompt assembly
* context overflow
* noisy context
* weak reranking
* metadata mismatch
* hallucination-inducing retrieval

Query quality depends on the entire pipeline.

---

# Security

Query systems may expose:

* private documents
* scientific experiments
* sensitive metadata
* proprietary analyses

Query infrastructure requires:

* access control
* filtering
* tenant isolation
* validation

---

# Why Query Engines Became Important

Modern AI systems increasingly require:

* retrieval orchestration
* grounded reasoning
* semantic memory access
* scalable context management
* retrieval-assisted generation

Query Engines became foundational AI infrastructure.

---

# Common Misconceptions

## “A Query Engine is Just Vector Search”

Modern Query Engines coordinate:

* retrieval
* reranking
* synthesis
* prompting
* orchestration

---

## “The Retriever Alone Solves RAG”

Retrieval alone does not generate grounded answers.

Context orchestration also matters.

---

## “The LLM Understands the Database Directly”

The LLM only sees:

```text
assembled prompt context
```

The Query Engine controls that context.

---

# Common Mistakes

## Weak Context Assembly

Reasoning quality degrades.

---

## Oversized Retrieval Context

Prompts become noisy and expensive.

---

## Ignoring Metadata Filtering

Retrieval precision suffers.

---

## No Reranking

Irrelevant Nodes may dominate context.

---

## Treating Querying as Simple Search

Modern querying is sophisticated orchestration infrastructure.

---

# Recommended Mental Model

Useful perspective:

```text
Retrievers find memories

Query Engines transform memories
into grounded reasoning context
```

Query Engines are effectively:

```text
retrieval orchestration systems
```

for LLMs.

---

# Important Insight

In modern RAG systems:

```text
retrieval quality
+
context orchestration quality
≈
answer quality
```

Query Engines sit at the center of this orchestration layer.

---

# Key Insight

Modern Query Engines fundamentally combine:

```text
retrievers
+
metadata filtering
+
reranking
+
context assembly
+
prompt construction
+
LLM reasoning
+
response synthesis
```

Query Engines are one of the foundational orchestration abstractions enabling scalable retrieval-augmented AI systems.
