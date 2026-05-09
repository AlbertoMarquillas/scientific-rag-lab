# Vector Databases

---

# What is a Vector Database?

A vector database is a database designed to store, index, and search embeddings efficiently.

Unlike traditional databases that search using:

* exact values
* keywords
* relational queries

vector databases search using:

```text
semantic similarity
```

Their main purpose is to perform:

```text
nearest neighbor search
```

in high-dimensional vector spaces.

---

# Why Vector Databases Exist

Modern AI systems generate huge numbers of embeddings.

Examples:

* document embeddings
* image embeddings
* multimodal embeddings
* experiment embeddings
* user embeddings

Searching millions of vectors naively is computationally expensive.

Vector databases are optimized for:

* fast similarity search
* scalable vector indexing
* efficient retrieval
* metadata filtering

---

# Traditional Search vs Vector Search

## Traditional Search

Usually based on:

* keywords
* exact matching
* lexical similarity

Example:

```text
"beam wander"
```

matches documents containing:

```text
"beam wander"
```

---

## Vector Search

Based on semantic similarity.

Example:

```text
"beam wander"
```

may retrieve:

```text
"centroid instability"
```

because embeddings are semantically close.

---

# Core Idea

A vector database stores embeddings as points in vector space.

When a query arrives:

```text
query
   ↓
embedding
   ↓
similarity search
   ↓
nearest vectors
```

The system retrieves the vectors most similar to the query vector.

---

# High-Dimensional Spaces

Embeddings often contain:

* hundreds of dimensions
* thousands of dimensions

Examples:

* 384D
* 768D
* 1536D
* 3072D

Searching efficiently in high-dimensional spaces is difficult.

This is one of the main problems vector databases solve.

---

# Nearest Neighbor Search

Goal:

```text
find vectors closest to a query vector
```

This operation is called:

```text
nearest neighbor search
```

---

# Similarity Metrics

Vector databases compare vectors using similarity metrics.

Common metrics:

## Cosine Similarity

genui{"math_block_widget_always_prefetch_v2":{"content":"\cos(\theta)=\frac{\vec a \cdot \vec b}{\|a\|\|b\|}"}}

Most common in semantic search.

---

## Euclidean Distance

genui{"math_block_widget_always_prefetch_v2":{"content":"d(\vec a,\vec b)=\sqrt{\sum_{i=1}^{n}(a_i-b_i)^2}"}}

Measures geometric distance.

---

## Dot Product

genui{"math_block_widget_always_prefetch_v2":{"content":"\vec a \cdot \vec b=\sum_{i=1}^{n}a_ib_i"}}

Often used in embedding systems.

---

# Exact Search vs Approximate Search

## Exact Search

Compares the query against every vector.

Very accurate.

But extremely expensive at scale.

Complexity grows rapidly with dataset size.

---

## Approximate Nearest Neighbor (ANN)

Most modern vector databases use:

```text
ANN algorithms
```

Goal:

```text
find very good neighbors quickly
```

instead of:

```text
finding the mathematically perfect nearest neighbor
```

ANN dramatically improves scalability.

---

# Why ANN Matters

Without ANN:

```text
millions of vectors
→
slow retrieval
```

With ANN:

```text
millions of vectors
→
fast semantic search
```

This makes production-scale RAG systems possible.

---

# HNSW

One of the most common ANN algorithms is:

```text
HNSW
```

Meaning:

```text
Hierarchical Navigable Small World
```

HNSW creates graph-based structures allowing efficient navigation through vector space.

Many vector databases use HNSW internally.

Examples:

* Qdrant
* Weaviate
* Chroma

---

# Main Components of a Vector Database

## 1. Vectors

The embeddings themselves.

---

## 2. IDs

Unique identifiers associated with vectors.

---

## 3. Metadata / Payloads

Additional structured information.

Examples:

```json
{
  "experiment": "run_42",
  "heater_voltage": 16,
  "scintillation_index": 0.31,
  "regime": "strong"
}
```

---

## 4. Indexes

Data structures optimized for fast vector retrieval.

---

# Metadata Filtering

One of the most powerful features.

Retrieval can combine:

```text
semantic similarity
+
structured filters
```

Example:

```text
retrieve similar experiments
WHERE heater_voltage > 10
```

This is extremely important in scientific systems.

---

# Collections

Most vector databases organize data into:

```text
collections
```

A collection is similar to a table in relational databases.

Examples:

* papers collection
* experiment collection
* plots collection
* notes collection

---

# Typical RAG Workflow

## Offline Indexing Stage

```text
Documents
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database
```

---

## Online Query Stage

```text
User Query
      ↓
Query Embedding
      ↓
Vector Search
      ↓
Top-K Results
```

---

# Top-K Retrieval

Most searches retrieve:

```text
Top-K nearest vectors
```

Example:

```text
Top-5 most similar chunks
```

The value of K strongly affects:

* retrieval quality
* prompt size
* context noise

---

# Popular Vector Databases

## Qdrant

Modern open-source vector database.

Strong support for:

* filtering
* scalability
* production systems
* hybrid search

---

## Pinecone

Managed cloud vector database.

Widely used in production AI systems.

---

## Weaviate

Vector database with graph-oriented features.

---

## Chroma

Simple lightweight vector database.

Popular for experimentation.

---

## FAISS

Library created by Meta.

Very important historically.

Focused on fast similarity search.

---

# Hybrid Search

Modern systems often combine:

```text
vector search
+
keyword search
```

This is called:

```text
hybrid retrieval
```

Hybrid retrieval improves robustness.

---

# Reranking

Vector search may retrieve imperfect results.

Many systems perform:

```text
retrieve many
      ↓
rerank
      ↓
keep best results
```

Reranking improves retrieval precision.

---

# Scalability

Vector databases are designed for:

* millions of vectors
* billions of vectors
* distributed systems
* real-time retrieval

Scalability becomes critical in production AI systems.

---

# Latency

Retrieval speed matters.

RAG systems must often answer in:

```text
milliseconds
```

Vector databases optimize retrieval latency heavily.

---

# Vector Databases in Scientific Systems

Scientific applications are especially suitable because:

* experiments generate large datasets
* semantic relationships matter
* metadata filtering is important
* retrieval complexity grows rapidly

Examples:

* retrieving similar experiments
* searching papers semantically
* retrieving turbulence regimes
* comparing beam behavior

---

# Vector Databases in This Project

Potential collections:

```text
papers
experiments
analysis_results
comparison_results
notes
plots
```

Potential metadata:

```text
heater_voltage
fan_voltage
scintillation_index
fried_parameter
rytov_variance
beam_wander
regime
```

Potential retrieval tasks:

* similar turbulence regimes
* similar beam morphology
* experiment comparison
* semantic scientific search

---

# Important Limitations

Vector databases are powerful but imperfect.

Common issues:

* retrieval noise
* embedding errors
* ANN approximation errors
* storage costs
* scaling complexity
* metadata consistency

Good retrieval quality depends heavily on:

* embedding quality
* chunking quality
* indexing strategy
* filtering logic

---

# Key Insight

A vector database is fundamentally:

```text
semantic memory infrastructure
```

for AI systems.

It allows modern AI architectures to:

* search meaning mathematically
* retrieve relevant information efficiently
* scale external knowledge
* support RAG pipelines
* enable semantic retrieval over massive datasets
