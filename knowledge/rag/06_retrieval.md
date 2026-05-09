# Retrieval

---

# What is Retrieval?

Retrieval is the process of searching and selecting relevant information from a knowledge source.

In RAG systems, retrieval is responsible for deciding:

```text
which information enters the LLM context
```

This makes retrieval one of the most critical components of modern AI systems.

A language model can only reason effectively if the correct information is retrieved.

---

# Fundamental Idea

The retrieval pipeline usually works like this:

```text
User Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
Prompt Context
      ↓
LLM Response
```

The quality of the final answer depends heavily on the quality of retrieved information.

---

# Why Retrieval Matters

LLMs do not automatically know:

* which documents matter
* which experiments are relevant
* which papers contain useful information
* which context is important

Retrieval acts as:

```text
dynamic context selection
```

---

# Retrieval Goals

A good retrieval system should:

* retrieve relevant information
* avoid irrelevant information
* maximize semantic similarity
* preserve important context
* minimize noise
* operate efficiently

---

# Retrieval and Context Windows

LLMs have limited context windows.

This means:

```text
only a small subset of information can enter the prompt
```

Retrieval decides:

```text
which subset is most useful
```

---

# Dense Retrieval

Most modern RAG systems use:

```text
dense retrieval
```

Dense retrieval works using embeddings.

Pipeline:

```text
Documents
      ↓
Embeddings
      ↓
Vector Database
```

At query time:

```text
Query
   ↓
Query Embedding
   ↓
Nearest Neighbor Search
```

The system retrieves semantically similar chunks.

---

# Sparse Retrieval

Traditional retrieval systems often use:

```text
sparse retrieval
```

Examples:

* TF-IDF
* BM25
* keyword search

Sparse retrieval focuses mainly on:

* exact terms
* word frequency
* lexical matching

---

# Dense vs Sparse Retrieval

## Dense Retrieval

Advantages:

* semantic understanding
* synonym handling
* conceptual similarity

Disadvantages:

* may retrieve semantically noisy results
* harder to interpret

---

## Sparse Retrieval

Advantages:

* precise keyword matching
* interpretable scoring
* efficient for exact queries

Disadvantages:

* weak semantic understanding
* poor synonym handling

---

# Hybrid Retrieval

Modern systems often combine:

```text
dense retrieval
+
sparse retrieval
```

This is called:

```text
hybrid retrieval
```

Hybrid systems are usually more robust.

---

# Semantic Retrieval

Semantic retrieval means:

```text
retrieve based on meaning
```

instead of exact wording.

Example:

```text
"beam wander"
```

may retrieve:

```text
"centroid instability"
```

because the concepts are semantically related.

---

# Retrieval Pipeline

A typical retrieval pipeline:

```text
Documents
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Top-K Chunks
```

---

# Query Embeddings

The user query is converted into an embedding vector.

This vector is compared against stored document vectors.

Goal:

```text
find nearest semantic neighbors
```

---

# Top-K Retrieval

Most systems retrieve:

```text
Top-K results
```

Examples:

* Top-3
* Top-5
* Top-10

Choosing K is important.

Too small:

* important information may be missed

Too large:

* context noise increases
* irrelevant information enters the prompt

---

# Retrieval Precision vs Recall

Retrieval systems balance:

## Precision

```text
how relevant retrieved results are
```

---

## Recall

```text
how much relevant information is retrieved
```

High precision:

* fewer irrelevant chunks

High recall:

* lower risk of missing important information

---

# Retrieval Noise

One of the biggest problems in RAG systems:

```text
retrieval noise
```

Meaning:

* irrelevant chunks retrieved
* weakly related information
* semantically confusing context

Noise reduces reasoning quality.

---

# Context Pollution

If retrieval quality is poor:

* prompts become noisy
* hallucinations increase
* answers degrade
* reasoning becomes unstable

This problem is often called:

```text
context pollution
```

---

# Metadata Filtering

Modern retrieval systems often combine:

```text
semantic retrieval
+
structured filtering
```

Example:

```text
retrieve similar experiments
WHERE scintillation_index > 0.3
```

This is especially important in scientific systems.

---

# Reranking

Initial retrieval may not produce optimal ordering.

Many systems use:

```text
retrieve many
      ↓
rerank results
      ↓
keep best chunks
```

Reranking improves precision.

---

# Cross-Encoders

Advanced reranking systems often use:

```text
cross-encoders
```

Cross-encoders jointly analyze:

* query
* retrieved chunk

This often improves ranking quality significantly.

---

# Multi-Stage Retrieval

Modern retrieval pipelines are often hierarchical.

Example:

```text
Fast Retrieval
      ↓
Reranking
      ↓
Filtering
      ↓
Context Selection
```

This balances:

* speed
* quality
* scalability

---

# Query Expansion

Some systems improve retrieval using:

```text
query expansion
```

Meaning:

* generate related queries
* add synonyms
* reformulate questions

This improves recall.

---

# Retrieval Granularity

Systems may retrieve:

* full documents
* sections
* paragraphs
* chunks
* sentences

Granularity strongly affects:

* retrieval precision
* context quality
* prompt efficiency

---

# Retrieval Latency

Retrieval must usually happen quickly.

Production systems often require:

```text
millisecond-scale retrieval
```

Latency becomes critical at scale.

---

# Retrieval Evaluation

Important retrieval metrics:

## Precision@K

How many retrieved results are relevant.

---

## Recall@K

How much relevant information was retrieved.

---

## MRR

Mean Reciprocal Rank.

Measures ranking quality.

---

## NDCG

Normalized Discounted Cumulative Gain.

Measures ranking usefulness.

---

# Retrieval Failure Modes

Common problems:

## Missing Relevant Information

The system fails to retrieve important chunks.

---

## Retrieving Irrelevant Chunks

Context pollution.

---

## Semantic Ambiguity

Query meaning is unclear.

---

## Embedding Failures

Weak semantic representations.

---

## Poor Chunking

Bad chunk boundaries reduce retrieval quality.

---

# Retrieval in Scientific Systems

Scientific retrieval is difficult because:

* terminology varies
* concepts are complex
* experiments are multimodal
* numerical relationships matter
* semantic similarity is subtle

Good scientific retrieval often requires:

* metadata filtering
* structured retrieval
* domain-aware chunking
* reranking

---

# Retrieval in This Project

Potential retrieval targets:

```text
metadata.json
analysis.json
comparison results
scientific notes
papers
plots
```

Potential queries:

```text
"find strong turbulence experiments"

"retrieve experiments with large beam wander"

"find runs similar to this Rytov regime"
```

Potential filters:

```text
heater_voltage
fan_voltage
scintillation_index
fried_parameter
beam_wander
```

---

# Retrieval and Grounding

Retrieval is essential for grounding.

Grounded responses are based on:

```text
retrieved evidence
```

instead of pure model generation.

This helps reduce:

* hallucinations
* fabricated claims
* unsupported reasoning

---

# Key Insight

Retrieval fundamentally determines:

```text
what the LLM is allowed to know
```

A powerful language model with poor retrieval often performs badly.

A strong retrieval system dramatically improves:

* reasoning quality
* factual grounding
* context relevance
* scalability
* scientific usefulness
