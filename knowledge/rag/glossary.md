# RAG Glossary

---

# A

## Agent

An AI system capable of:

* reasoning
* planning
* using tools
* interacting with external systems
* executing multi-step workflows

---

## ANN (Approximate Nearest Neighbor)

A family of algorithms used to perform efficient similarity search in high-dimensional vector spaces.

Used heavily in scalable vector databases.

Examples:

* HNSW
* IVF
* PQ

---

# B

## Bi-Encoder

A retrieval architecture where:

* query
* document

are embedded independently.

Similarity is computed between embeddings.

Fast and scalable but less precise than cross-encoders.

---

## BM25

A classical sparse retrieval algorithm based on keyword relevance.

Widely used in search engines.

Good for:

* exact terms
* technical identifiers
* lexical matching

---

# C

## Caching

Storing previously computed results to reduce:

* latency
* computation
* API usage
* cost

---

## Chunk

A smaller unit of information extracted from a larger document.

Chunks are usually the units retrieved by a RAG system.

---

## Chunking

The process of dividing documents into chunks.

Chunking strongly affects retrieval quality.

---

## Context Window

The maximum amount of information an LLM can process at once.

Usually measured in tokens.

---

## Cosine Similarity

A common similarity metric used to compare embeddings.

Measures angular similarity between vectors.

Range:

```text
-1 → opposite
 0 → unrelated
 1 → identical direction
```

---

## Cross-Encoder

A reranking architecture where:

```text
query + document
```

are processed together.

More precise than bi-encoders but slower.

---

# D

## Dense Retrieval

Retrieval using embeddings and vector similarity.

Focuses on semantic similarity.

---

## Document Store

Storage system containing the original documents or chunks.

Usually separate from the vector database.

---

# E

## Embedding

A numerical vector representation of data.

Embeddings encode semantic information.

Used for:

* similarity search
* clustering
* retrieval
* recommendation systems

---

## Embedding Drift

A change in retrieval behavior caused by changes in:

* embedding models
* data distributions
* indexing strategies

---

## Evaluation

The process of measuring the quality and reliability of a RAG system.

---

# F

## Faithfulness

Measures whether a generated answer remains consistent with retrieved evidence.

---

## Fine-Tuning

Training or adapting a model on additional data.

Different from RAG.

RAG retrieves external knowledge dynamically.

Fine-tuning modifies model weights.

---

## Grounding

The process of connecting generated answers to retrieved evidence.

Grounded systems hallucinate less.

---

# H

## Hallucination

Generated content that:

* is false
* unsupported
* fabricated
* inconsistent with evidence

while sounding plausible.

---

## HNSW

Hierarchical Navigable Small World.

A widely used ANN algorithm for scalable vector search.

Used in:

* Qdrant
* Weaviate
* Chroma

---

## Hybrid Search

Retrieval combining:

* dense/vector search
* sparse/keyword search

Used to improve retrieval robustness.

---

# I

## Incremental Indexing

Updating only changed documents instead of rebuilding the entire index.

Important for scalable systems.

---

## Ingestion

The process of loading and preparing data for indexing.

Includes:

* parsing
* cleaning
* chunking
* metadata extraction

---

# K

## Keyword Search

Retrieval based on exact lexical matches.

Often implemented using:

* BM25
* TF-IDF

---

# L

## Latency

The time required for a system to produce a response.

Examples:

* retrieval latency
* generation latency
* total response time

---

## LLM (Large Language Model)

A neural network trained to predict and generate text.

Examples:

* GPT models
* Claude
* Gemini
* Llama

---

# M

## Metadata

Structured information describing data.

Examples:

* author
* year
* experiment ID
* timestamp
* turbulence regime
* metric values

---

## Metadata Filtering

Restricting retrieval using structured conditions.

Example:

```text
heater_voltage > 10
```

---

## MRR (Mean Reciprocal Rank)

A ranking metric measuring how early the first relevant result appears.

---

## Multimodal RAG

A RAG system capable of retrieving multiple data types.

Examples:

* text
* images
* plots
* tables
* time series

---

# N

## NDCG

Normalized Discounted Cumulative Gain.

A ranking quality metric.

Often used for retrieval evaluation.

---

## Nearest Neighbor Search

Searching for vectors that are closest to a query vector.

Core operation in vector retrieval.

---

# O

## Observability

The ability to inspect and understand internal system behavior.

Includes:

* logs
* traces
* metrics
* monitoring

---

# P

## Payload

Metadata attached to a vector inside a vector database.

Used for:

* filtering
* traceability
* retrieval constraints

---

## Precision@K

Measures the fraction of retrieved results that are relevant.

---

## Prompt

The input sent to an LLM.

Usually includes:

* system instructions
* retrieved context
* user query

---

## Prompt Injection

A security attack attempting to manipulate model behavior through malicious instructions.

---

## Prompt Engineering

The process of designing prompts that improve:

* grounding
* reasoning
* reliability
* answer quality

---

# Q

## Query Embedding

The embedding representation of a user query.

Used for vector retrieval.

---

# R

## RAG (Retrieval-Augmented Generation)

An AI architecture combining:

* retrieval
* external knowledge
* language generation

---

## Recall@K

Measures how much relevant information was retrieved.

---

## Replication

Duplicating data across multiple systems or nodes.

Used for:

* reliability
* availability
* fault tolerance

---

## Retrieval

The process of finding relevant information for a query.

---

## Retrieval Drift

A gradual change in retrieval quality over time.

---

## Retrieval Poisoning

Injecting malicious or misleading data into a retrieval system.

---

## Reranking

Reordering retrieved candidates using a more precise relevance model.

---

## ReAct

Reason + Act.

An agentic reasoning pattern combining:

* reasoning
* tool usage

---

# S

## Scaling

Designing systems that continue working efficiently as:

* data grows
* users increase
* workloads expand

---

## Semantic Search

Retrieval based on meaning rather than exact keywords.

Usually implemented using embeddings.

---

## Sharding

Partitioning data across multiple storage units or servers.

---

## Sparse Retrieval

Retrieval based on lexical matching.

Examples:

* BM25
* TF-IDF

---

## Streaming

Sending partial responses progressively instead of waiting for full completion.

---

# T

## Token

A basic text unit processed by an LLM.

Context windows and pricing are usually measured in tokens.

---

## Top-K Retrieval

Returning the K most relevant retrieval results.

Example:

```text
Top-5 chunks
```

---

## Traceability

The ability to connect outputs back to their original sources.

Important in scientific systems.

---

## Tracing

Tracking the flow of a request through a system.

---

# V

## Vector

A numerical representation of information.

Embeddings are vectors.

---

## Vector Database

A database optimized for storing and searching embeddings.

Examples:

* Qdrant
* Pinecone
* Weaviate
* Chroma

---

## Vector Search

Similarity search over embeddings.

Core operation in dense retrieval.

---

# W

## Workflow

A structured sequence of operations inside a system.

Workflows are usually more deterministic than autonomous agents.
