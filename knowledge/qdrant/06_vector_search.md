# Vector Search

---

# What is Vector Search?

Vector search is a retrieval method based on:

```text
semantic similarity
```

instead of:

```text
exact keyword matching
```

The goal is:

```text
retrieve vectors geometrically close to a query vector
```

This is one of the foundations of modern AI retrieval systems.

---

# Core Idea

Traditional search asks:

```text
Which documents contain these words?
```

Vector search asks:

```text
Which vectors represent similar meaning?
```

This enables semantic retrieval.

---

# Why Vector Search Exists

Human language is flexible.

The same idea may be expressed using:

* different wording
* synonyms
* paraphrases
* implicit descriptions

Keyword search often misses these relationships.

Vector search attempts to retrieve:

```text
semantic meaning
```

rather than exact text overlap.

---

# Embedding-Based Retrieval

Vector search relies on embeddings.

Pipeline:

```text
raw text
      ↓
embedding model
      ↓
vector representation
```

Retrieval occurs over these vectors.

---

# Query Embeddings

User queries are also embedded.

Pipeline:

```text
user query
      ↓
embedding model
      ↓
query vector
      ↓
vector search
```

The system retrieves nearby vectors.

---

# Semantic Geometry

Core principle:

```text
similar meaning
→ nearby vectors
```

inside high-dimensional space.

Vector search navigates this semantic geometry.

---

# Example

Query:

```text
"strong optical turbulence"
```

Possible retrieved results:

* beam spreading
* scintillation instability
* atmospheric distortion
* centroid fluctuations

Even if exact words differ.

---

# Why This is Powerful

Traditional keyword systems may fail when:

* terminology changes
* wording differs
* concepts are implicit
* synonyms are used

Vector search improves semantic flexibility.

---

# Similarity Search

Core retrieval operation:

```text
find nearest vectors
```

The system computes:

```text
vector similarity
```

between:

* query embedding
* stored embeddings

---

# Similarity Metrics

Common similarity metrics:

* cosine similarity
* dot product
* Euclidean distance

These determine how vector proximity is measured.

---

# Cosine Similarity

Very common in semantic retrieval.

Measures:

```text
angular similarity between vectors
```

Conceptually:

```text
similar direction
→ similar meaning
```

---

# Dot Product

Measures:

```text
alignment and magnitude interaction
```

Often used in:

* neural retrieval
* transformer embeddings
* recommendation systems

---

# Euclidean Distance

Measures:

```text
physical distance in vector space
```

Conceptually:

```text
closer vectors
→ more similar
```

Less common for modern normalized embeddings.

---

# Search Pipeline

Typical vector search flow:

```text
user query
      ↓
embed query
      ↓
search vector index
      ↓
retrieve nearest neighbors
      ↓
rank by similarity
```

This is the foundation of semantic retrieval.

---

# Similarity Ranking

Retrieved results are usually ranked by:

```text
similarity score
```

Higher similarity:

```text
more semantically related
```

Ranking strongly affects retrieval quality.

---

# Top-K Retrieval

Systems often retrieve:

```text
top-k nearest neighbors
```

Example:

```text
retrieve top 5 similar chunks
```

Choosing k affects:

* context size
* retrieval precision
* retrieval recall

---

# Precision vs Recall

Important retrieval tradeoff.

High precision:

```text
fewer but highly relevant results
```

High recall:

```text
more potentially relevant results
```

Retrieval systems balance both.

---

# Similarity Thresholds

Systems may apply:

```text
minimum similarity thresholds
```

Low-quality matches may be:

* discarded
* reranked
* ignored

Threshold tuning affects retrieval behavior.

---

# Approximate Nearest Neighbor Search

Large-scale vector search often uses:

```text
ANN
```

Approximate Nearest Neighbor search.

Reason:

exact search becomes too expensive at scale.

ANN enables fast semantic retrieval.

---

# Why ANN Matters

Production systems may contain:

* millions of vectors
* billions of embeddings
* multimodal retrieval indexes

Efficient search becomes essential.

---

# HNSW Search

Qdrant commonly uses:

```text
HNSW
```

Hierarchical Navigable Small Worlds.

HNSW enables:

* fast retrieval
* scalable search
* strong recall

through graph-based ANN indexing.

---

# Search Latency

Important metric:

```text
retrieval latency
```

Meaning:

```text
how fast results are returned
```

Production systems require low latency.

---

# Retrieval Recall

Important retrieval metric:

```text
recall
```

Meaning:

```text
how often relevant vectors are retrieved
```

Low recall weakens RAG quality.

---

# Retrieval Precision

Another key metric:

```text
precision
```

Meaning:

```text
how many retrieved results are truly relevant
```

Precision strongly affects answer quality.

---

# Similarity ≠ Truth

Important limitation.

Vector similarity means:

```text
semantic proximity
```

not:

```text
factual correctness
```

Retrieved information may still be:

* incorrect
* hallucinated
* outdated
* noisy

Retrieval systems still require evaluation.

---

# Why Retrieval Quality Matters

In RAG systems:

```text
retrieval quality
≈ answer quality
```

Weak retrieval produces:

* hallucinations
* irrelevant context
* incorrect grounding

Retrieval is foundational.

---

# Hybrid Retrieval

Modern systems rarely rely only on vectors.

They often combine:

* vector similarity
* keyword search
* metadata filtering
* reranking

This is called:

```text
hybrid retrieval
```

---

# Metadata Filtering

Vector search may be constrained using metadata.

Example:

```text
find similar experiments
WHERE heater_voltage > 10
```

Filtering improves:

* precision
* control
* explainability

---

# Reranking

Many systems apply:

```text
reranking
```

after vector retrieval.

Pipeline:

```text
vector search
      ↓
retrieve candidates
      ↓
rerank using stronger model
```

Reranking improves retrieval quality.

---

# Why Vector Search Alone is Often Insufficient

Embedding retrieval may:

* retrieve noisy chunks
* miss exact keywords
* return loosely related content

Production systems usually combine multiple retrieval strategies.

---

# Vector Search and RAG

Typical RAG pipeline:

```text
user query
      ↓
query embedding
      ↓
vector retrieval
      ↓
retrieve chunks
      ↓
augment LLM context
      ↓
generate answer
```

Vector search powers the retrieval stage.

---

# Context Window Constraints

LLMs have limited context windows.

Vector retrieval helps select:

```text
most relevant information
```

instead of sending entire datasets.

---

# Vector Search and Agents

Agents use vector retrieval for:

* memory
* contextual reasoning
* semantic lookup
* tool context
* long-term knowledge

Semantic retrieval increasingly powers agent memory.

---

# Multimodal Vector Search

Vectors may represent:

* text
* images
* plots
* audio
* video
* scientific descriptors

Vector search can retrieve across modalities.

---

# Visual Retrieval Example

Example:

```text
beam profile image
      ↓
image embedding
      ↓
retrieve visually similar experiments
```

This enables multimodal scientific retrieval.

---

# Scientific Vector Search

Scientific systems may search over:

* experiment summaries
* turbulence descriptors
* module outputs
* plots
* papers
* comparison reports

Vector search enables semantic scientific exploration.

---

# Example Scientific Query

Example:

```text
Find experiments similar to:
strong beam spreading with intermittent fading
```

This is semantic retrieval.

---

# Vector Search in This Project

Potential retrieval objects:

```text
experiment summaries
module analyses
paper chunks
comparison reports
scientific observations
```

Potential retrieval capabilities:

* turbulence regime retrieval
* experiment similarity search
* semantic scientific exploration
* paper-experiment linking

---

# Why Vector Search Fits Your Project

Your system naturally generates:

* summaries
* descriptors
* metadata
* scientific observations
* multimodal artifacts

These are ideal semantic retrieval objects.

---

# Retrieval Evaluation

Vector search quality should be evaluated.

Possible metrics:

* recall
* precision
* latency
* ranking quality
* grounding quality

Production retrieval systems require evaluation.

---

# Observability in Retrieval

Production systems monitor:

* retrieval latency
* query throughput
* similarity distributions
* failed queries
* reranking quality

Retrieval infrastructure requires observability.

---

# Common Misconceptions

## “Semantic Search Understands Truth”

Similarity ≠ factual correctness.

---

## “Embeddings Solve Retrieval Automatically”

Retrieval quality also depends on:

* chunking
* metadata
* reranking
* indexing
* filtering

---

## “Top Similarity Means Best Answer”

Nearest neighbor may still be noisy or incomplete.

---

# Common Mistakes

## Weak Chunking

Semantic retrieval quality degrades.

---

## Ignoring Metadata

Filtering becomes limited.

---

## No Retrieval Evaluation

Weak search quality remains hidden.

---

## Embedding Noisy Data

Retrieval becomes unreliable.

---

## No Hybrid Retrieval

Precision may suffer.

---

# Recommended Mental Model

Useful perspective:

```text
vector search navigates semantic geometry
```

The system retrieves:

```text
nearby meaning representations
```

inside embedding space.

---

# Important Insight

Modern semantic retrieval systems work because:

```text
semantic meaning
can be approximated geometrically
```

through embeddings and vector similarity.

Vector search operationalizes this idea.

---

# Key Insight

Modern AI retrieval systems fundamentally depend on:

```text
embeddings
+
vector similarity
+
nearest-neighbor search
+
ANN indexing
+
hybrid retrieval
```

Vector search is one of the core mechanisms enabling scalable semantic memory and retrieval systems in modern AI infrastructure.
