# Indexing

---

# Why Indexing Exists

Modern vector databases may contain:

* millions of vectors
* billions of embeddings
* multimodal datasets
* long-term AI memory

Searching every vector sequentially would be too expensive.

Indexing exists to make retrieval:

```text
fast
and
scalable
```

---

# Core Idea

Indexing means:

```text
organizing data
for efficient retrieval
```

Instead of scanning everything:

```text
smart structures accelerate search
```

This is fundamental in databases and retrieval systems.

---

# Traditional Database Indexes

Traditional databases use indexes for:

* exact matching
* sorted lookups
* structured queries

Example:

```sql
SELECT *
WHERE run_id = 123
```

Indexes accelerate these operations.

---

# Why Vector Indexing is Different

Vector search is not:

```text
exact matching
```

It is:

```text
nearest-neighbor search
```

Meaning:

```text
find vectors geometrically close
```

This requires specialized indexing algorithms.

---

# The Retrieval Problem

Suppose:

```text
100 million embeddings
```

Naive search:

```text
compare query vector
against every stored vector
```

This becomes computationally expensive.

Vector indexes solve this problem.

---

# Nearest Neighbor Search

Core retrieval objective:

```text
find nearest vectors efficiently
```

Indexing structures help avoid:

```text
full exhaustive search
```

---

# Exact Search

Exact search means:

```text
compute similarity with every vector
```

Advantages:

* perfectly accurate

Disadvantages:

* extremely slow at scale
* computationally expensive
* poor scalability

Exact search rarely scales well.

---

# Approximate Search

Modern vector databases often use:

```text
Approximate Nearest Neighbor (ANN)
```

search.

ANN trades:

```text
small accuracy loss
```

for:

```text
massive speed improvements
```

This is critical in production systems.

---

# Why ANN Matters

Production systems require:

* low latency
* scalable retrieval
* large vector collections
* fast semantic search

ANN enables practical semantic retrieval.

---

# Core ANN Idea

Instead of:

```text
search everything
```

ANN attempts to:

```text
search only promising regions
```

inside vector space.

This dramatically reduces computation.

---

# Semantic Geometry

Embeddings create:

```text
semantic geometric spaces
```

Similar vectors cluster together.

Indexes exploit this geometric structure.

---

# HNSW

One of the most important ANN algorithms:

```text
HNSW
```

Hierarchical Navigable Small Worlds.

Qdrant heavily relies on HNSW indexing.

---

# Intuition Behind HNSW

Conceptually:

```text
vectors form neighborhoods
```

HNSW builds:

```text
navigable graph structures
```

allowing fast traversal toward similar vectors.

---

# Graph-Based Search

HNSW organizes vectors as:

```text
connected graph nodes
```

Search navigates through nearby neighbors.

Instead of searching all vectors:

```text
follow promising paths
```

through the graph.

---

# Why HNSW is Powerful

HNSW provides:

* high retrieval speed
* strong scalability
* excellent recall
* efficient nearest-neighbor search

It is one of the dominant ANN approaches.

---

# ANN Tradeoff

ANN always involves a tradeoff:

```text
speed
vs
retrieval accuracy
```

Production systems optimize this balance.

---

# Recall

Important ANN concept:

```text
recall
```

Meaning:

```text
how often the correct neighbors are retrieved
```

Higher recall:

* better retrieval quality
* slower search

Lower recall:

* faster retrieval
* weaker search quality

---

# Latency

Another important metric:

```text
retrieval latency
```

Meaning:

```text
how fast retrieval occurs
```

Production systems require low latency.

---

# Throughput

Indexing systems also care about:

```text
throughput
```

Meaning:

```text
how many searches per second
```

can be processed.

---

# Index Construction

Indexes must first be built.

Process:

```text
vectors inserted
      ↓
index structure updated
      ↓
retrieval optimized
```

Index building itself may be expensive.

---

# Dynamic Indexing

Modern systems continuously ingest new data.

Indexes must support:

* insertions
* updates
* deletions
* reindexing

without full reconstruction.

---

# Reindexing

Sometimes indexes require rebuilding.

Reasons:

* new embeddings
* new configurations
* performance optimization
* corrupted indexes

Reindexing may be expensive.

---

# Memory vs Speed Tradeoff

Indexes consume memory.

Tradeoff:

```text
larger indexes
→ faster retrieval
```

but:

```text
higher memory usage
```

Infrastructure design balances these constraints.

---

# Payload Indexing

Metadata fields may also be indexed.

Examples:

```text
run_id
experiment_date
module_name
```

Payload indexes accelerate filtering.

---

# Hybrid Retrieval

Modern systems combine:

* vector indexes
* keyword indexes
* metadata indexes

This enables:

```text
hybrid retrieval
```

---

# Why Hybrid Retrieval Matters

Semantic retrieval alone may retrieve noisy results.

Hybrid retrieval improves:

* precision
* control
* explainability
* filtering

Production systems increasingly combine multiple retrieval signals.

---

# Indexing and RAG

RAG systems depend heavily on indexing quality.

Poor indexing may cause:

* slow retrieval
* missing neighbors
* weak search quality
* scalability problems

Indexing is foundational infrastructure.

---

# Indexing and Agents

Agents may continuously:

* store memory
* retrieve context
* update embeddings
* query semantic history

Efficient indexing becomes critical.

---

# Multimodal Indexing

Modern systems may index:

* text embeddings
* image embeddings
* plot embeddings
* audio embeddings

Different modalities may require specialized indexing strategies.

---

# Scientific Retrieval Indexing

Scientific systems may index:

* experiment summaries
* turbulence descriptors
* module outputs
* comparison reports
* plots
* scientific papers

Efficient indexing enables semantic scientific exploration.

---

# Example Scientific Query

Example:

```text
Find experiments similar to:
strong beam spreading with high scintillation
```

Efficient retrieval depends heavily on indexing quality.

---

# Indexing in This Project

Potential indexed entities:

```text
experiment summaries
module analyses
paper chunks
comparison reports
plot descriptions
```

Potential retrieval tasks:

* turbulence regime similarity
* experiment clustering
* scientific semantic retrieval
* paper-experiment linking

---

# Why Indexing Matters for Your Project

Your project may eventually contain:

* many experiments
* many module outputs
* many embeddings
* multimodal retrieval artifacts

Efficient indexing becomes essential as scale grows.

---

# Indexing and Scalability

Without indexing:

```text
retrieval time grows badly with dataset size
```

Indexes make large-scale semantic retrieval practical.

---

# Observability and Indexing

Production systems monitor:

* retrieval latency
* recall quality
* indexing throughput
* memory usage
* query performance

Indexes require observability.

---

# Index Updates and Workflows

Workflow systems often manage:

* ingestion
* embedding generation
* vector insertion
* index updates
* reindexing

Indexing becomes part of orchestration infrastructure.

---

# Indexing and Cost

Indexes consume:

* RAM
* CPU
* storage
* infrastructure resources

Indexing strategy affects operational cost.

---

# Common Misconceptions

## “Vector Search is Just SQL Search”

Vector retrieval is fundamentally different.

---

## “Exact Search is Always Better”

Exact search often becomes impractical at scale.

---

## “Indexes Are Optional”

Large-scale semantic retrieval depends heavily on indexing.

---

# Common Mistakes

## Ignoring Recall Tradeoffs

Fast retrieval may lose relevant results.

---

## Weak Payload Indexing

Filtering becomes slow.

---

## No Observability

Performance degradation becomes invisible.

---

## Poor Reindexing Strategy

Infrastructure migrations become difficult.

---

## Embedding Everything Indiscriminately

Indexes become noisy and expensive.

---

# Recommended Mental Model

Useful perspective:

```text
indexes organize semantic space
```

for efficient navigation.

Vector indexes allow systems to:

```text
search meaning geometrically at scale
```

---

# Important Insight

Modern semantic retrieval is possible largely because:

```text
ANN indexing makes vector search scalable
```

Without ANN, large-scale RAG systems would often be impractical.

---

# Key Insight

Modern AI retrieval systems fundamentally rely on:

```text
embeddings
+
nearest-neighbor search
+
ANN indexing
+
semantic geometry
+
scalable retrieval infrastructure
```

Vector indexing is one of the core engineering mechanisms enabling semantic search at production scale.
