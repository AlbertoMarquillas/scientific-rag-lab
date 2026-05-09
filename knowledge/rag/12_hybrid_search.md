# Hybrid Search

---

# What is Hybrid Search?

Hybrid search is a retrieval strategy that combines multiple search methods to improve retrieval quality.

In RAG systems, hybrid search usually combines:

```text
vector search
+
keyword search
```

The goal is to retrieve information that is both:

* semantically relevant
* lexically precise

---

# Why Hybrid Search Exists

Dense vector retrieval is powerful, but it is not perfect.

Keyword search is also powerful, but it is not perfect.

Hybrid search exists because each method compensates for the weaknesses of the other.

---

# Dense Search

Dense search uses embeddings.

Pipeline:

```text
Text
   ↓
Embedding Model
   ↓
Vector Search
```

Dense search retrieves information based on:

```text
semantic similarity
```

---

# Sparse Search

Sparse search uses keyword-based representations.

Common methods:

* keyword matching
* TF-IDF
* BM25

Sparse search retrieves information based on:

```text
lexical similarity
```

---

# Dense vs Sparse Search

## Dense Search Strengths

Dense search is good at:

* synonyms
* paraphrases
* semantic similarity
* conceptual retrieval

Example:

```text
"beam wander"
```

may retrieve:

```text
"centroid instability"
```

---

## Dense Search Weaknesses

Dense search may struggle with:

* exact identifiers
* rare terms
* numerical values
* acronyms
* code names
* specific file names

Example:

```text
"2026-05-04_143509_v1-7_v2-7"
```

is better handled by keyword or metadata search.

---

## Sparse Search Strengths

Sparse search is good at:

* exact terms
* IDs
* numbers
* names
* acronyms
* technical keywords

---

## Sparse Search Weaknesses

Sparse search struggles with:

* synonyms
* paraphrases
* semantic similarity
* concept-level retrieval

Example:

```text
"centroid instability"
```

may not retrieve:

```text
"beam wander"
```

if exact terms do not overlap.

---

# Core Idea

Hybrid search combines:

```text
meaning-based retrieval
```

with:

```text
term-based retrieval
```

This improves robustness.

---

# Basic Hybrid Search Pipeline

```text
User Query
      ↓
Dense Retrieval
      ↓
Sparse Retrieval
      ↓
Score Fusion
      ↓
Top-K Results
```

---

# Score Fusion

Hybrid search needs a way to combine scores from different retrieval systems.

Typical scores:

* vector similarity score
* keyword relevance score
* metadata filter score

The final ranking combines them.

---

# Simple Weighted Fusion

A simple approach:

```text
final_score = α · dense_score + β · sparse_score
```

where:

* α controls dense retrieval importance
* β controls sparse retrieval importance

---

# Reciprocal Rank Fusion

A common method is:

```text
Reciprocal Rank Fusion
```

It combines rankings instead of raw scores.

This is useful because dense and sparse scores may have different scales.

Formula:

```text
RRF_score(d) = Σ 1 / (k + rank_i(d))
```

where:

* d is a document
* rank_i(d) is the rank of document d in retrieval system i
* k is a smoothing constant

---

# Why Score Normalization Matters

Dense and sparse scores often have different meanings.

Example:

```text
cosine similarity = 0.82
```

is not directly comparable to:

```text
BM25 score = 14.7
```

Hybrid systems usually need:

* normalization
* rank fusion
* reranking

---

# Hybrid Search and Reranking

Hybrid search is often followed by reranking.

Pipeline:

```text
Dense Search
      ↓
Sparse Search
      ↓
Merge Candidates
      ↓
Rerank
      ↓
Final Top-K
```

This improves final precision.

---

# Hybrid Search and Metadata Filtering

Hybrid search can also include metadata filters.

Example:

```text
semantic search
+
keyword search
+
heater_voltage > 10
```

This is extremely powerful in scientific retrieval.

---

# When Hybrid Search is Useful

Hybrid search is especially useful when queries contain:

* exact terms
* technical vocabulary
* identifiers
* acronyms
* numbers
* domain-specific language
* semantic concepts

Scientific systems often contain all of these.

---

# Example

Query:

```text
"Find runs with strong scintillation around r0 = 2 mm"
```

Dense search helps with:

```text
strong scintillation
```

Sparse or metadata search helps with:

```text
r0 = 2 mm
```

---

# Hybrid Search in Scientific Systems

Scientific retrieval often needs both:

```text
semantic understanding
```

and:

```text
exact technical precision
```

Examples:

* equation names
* experimental IDs
* parameter values
* instrument names
* physical metrics
* abbreviations

Hybrid search is usually better than pure vector search in this context.

---

# Hybrid Search in This Project

Potential dense retrieval targets:

```text
turbulence behavior
beam morphology
scientific notes
paper descriptions
experiment summaries
```

Potential sparse retrieval targets:

```text
run_id
module number
heater voltage
fan voltage
FWHM
Cn2
r0
Rytov
scintillation index
```

Potential filters:

```text
regime = "strong turbulence"
heater_voltage > 10
scintillation_index > 0.3
beam_wander_rms > threshold
```

---

# Example Pipeline for This Project

```text
User Query
      ↓
Dense retrieval over experiment summaries
      ↓
Sparse retrieval over metrics and IDs
      ↓
Metadata filtering over physical parameters
      ↓
Reranking
      ↓
Scientific answer generation
```

---

# Advantages

Hybrid search improves:

* recall
* robustness
* exact matching
* semantic matching
* scientific precision
* retrieval stability

---

# Limitations

Hybrid search adds complexity.

Challenges:

* score fusion
* tuning weights
* ranking conflicts
* latency
* system complexity
* evaluation complexity

---

# Common Mistake

A common mistake is assuming:

```text
vector search is always enough
```

For many real systems, especially scientific systems, pure vector search is not sufficient.

Exact terms, IDs, and numerical constraints matter.

---

# Key Insight

Hybrid search combines:

```text
semantic flexibility
```

with:

```text
lexical precision
```

For serious RAG systems, especially scientific ones, hybrid search is often much more reliable than using vector search alone.
