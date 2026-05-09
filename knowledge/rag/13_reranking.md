# Reranking

---

# What is Reranking?

Reranking is the process of reordering retrieved results after an initial retrieval step.

In RAG systems, the first retrieval stage usually retrieves a set of candidate chunks.

Reranking then evaluates those candidates more carefully and selects the best ones.

Core idea:

```text
retrieve broadly
      ↓
rerank precisely
      ↓
keep the best context
```

---

# Why Reranking Exists

Initial retrieval is usually optimized for speed.

Vector databases are designed to quickly find approximately relevant results.

However, fast retrieval is not always perfectly accurate.

Reranking improves final retrieval quality by applying a more precise relevance model after candidate retrieval.

---

# Basic Pipeline

Typical pipeline:

```text
User Query
      ↓
Initial Retrieval
      ↓
Candidate Chunks
      ↓
Reranker
      ↓
Final Top-K Chunks
      ↓
Prompt Context
```

---

# Retrieve Many, Keep Few

A common strategy:

```text
retrieve 20-100 candidates
      ↓
rerank candidates
      ↓
keep top 3-10
```

This improves the probability that the final prompt contains the most relevant evidence.

---

# Why Initial Retrieval is Not Enough

Initial retrieval can fail because of:

* embedding noise
* poor chunking
* semantic ambiguity
* approximate nearest neighbor errors
* weak query representation
* missing keyword precision

Reranking helps correct some of these issues.

---

# Reranking vs Retrieval

## Retrieval

Goal:

```text
find potentially relevant candidates quickly
```

Usually optimized for:

* speed
* scalability
* broad recall

---

## Reranking

Goal:

```text
choose the most relevant candidates carefully
```

Usually optimized for:

* precision
* relevance
* final context quality

---

# Candidate Generation

The first stage retrieves candidate chunks.

Candidate generation may use:

* dense retrieval
* sparse retrieval
* hybrid retrieval
* metadata filtering

The goal is high recall.

It is better to retrieve extra candidates than to miss important evidence.

---

# Reranker Model

A reranker is a model that scores the relevance of each candidate with respect to the query.

Input:

```text
query + candidate chunk
```

Output:

```text
relevance score
```

The candidates are then sorted by this score.

---

# Cross-Encoders

Many rerankers use cross-encoders.

A cross-encoder processes the query and candidate together.

Conceptually:

```text
[query, chunk] → relevance score
```

This allows deeper interaction between the query and the retrieved text.

---

# Bi-Encoders vs Cross-Encoders

## Bi-Encoder

Used in standard dense retrieval.

Pipeline:

```text
query → vector
chunk → vector
compare vectors
```

Advantages:

* fast
* scalable
* reusable embeddings

Disadvantages:

* less precise

---

## Cross-Encoder

Used in reranking.

Pipeline:

```text
query + chunk → relevance score
```

Advantages:

* more precise
* better relevance judgment

Disadvantages:

* slower
* harder to scale

---

# Why Cross-Encoders Improve Precision

Bi-encoders compare independently generated embeddings.

Cross-encoders analyze the full interaction between:

* query terms
* chunk content
* semantic relationships
* contextual meaning

This often produces better relevance rankings.

---

# Reranking and Top-K

Reranking helps decide the final Top-K chunks inserted into the prompt.

Example:

```text
Initial retrieval: Top-50
Reranker output: Top-5
Prompt context: Top-5
```

This reduces context noise.

---

# Reranking and Context Quality

Good reranking improves:

* prompt relevance
* grounding
* answer correctness
* context signal/noise ratio

Poor reranking may still allow irrelevant chunks into the prompt.

---

# Reranking and Hallucinations

Reranking can reduce hallucinations indirectly.

Why?

Because the LLM receives:

```text
cleaner and more relevant evidence
```

This improves grounding and reduces unsupported generation.

---

# Reranking in Hybrid Search

Hybrid search often produces candidates from multiple retrieval methods.

Pipeline:

```text
Dense Retrieval
      ↓
Sparse Retrieval
      ↓
Merge Candidates
      ↓
Rerank
      ↓
Final Results
```

Reranking is especially useful after hybrid retrieval.

---

# Score-Based Reranking

Some systems rerank using a numerical relevance score.

Example:

```text
chunk_A → 0.91
chunk_B → 0.76
chunk_C → 0.43
```

Higher scores indicate stronger relevance.

---

# LLM-Based Reranking

Some systems use an LLM as a reranker.

The model is asked to judge which chunks are most relevant.

Advantages:

* flexible
* reasoning-aware
* useful for complex tasks

Disadvantages:

* slower
* more expensive
* can be inconsistent

---

# Rule-Based Reranking

In scientific systems, reranking can also use domain rules.

Example:

```text
increase score if:
- same turbulence regime
- similar heater voltage
- similar scintillation index
- same analysis module
```

This can be combined with semantic reranking.

---

# Scientific Reranking

Scientific retrieval often needs more than semantic relevance.

Good scientific reranking may consider:

* semantic similarity
* numerical similarity
* experimental conditions
* physical regime
* metadata constraints
* source reliability

This is very relevant for experimental AI systems.

---

# Example in This Project

Query:

```text
"Find experiments similar to this strong turbulence run"
```

Initial retrieval may find semantically related experiments.

Reranking could prioritize experiments with:

```text
similar scintillation index
similar beam wander
similar Rytov variance
similar heater voltage
same analysis module
```

---

# Reranking Formula Example

A simple domain-aware score could combine several terms:

```text
final_score = α · semantic_score
            + β · metadata_score
            + γ · numerical_similarity
```

Where:

* semantic_score measures text similarity
* metadata_score measures filter compatibility
* numerical_similarity measures physical similarity

---

# Numerical Similarity

For scientific metrics, similarity can be based on normalized distance.

Example:

```text
similarity = 1 / (1 + normalized_distance)
```

This gives higher scores to experiments with closer physical values.

---

# Reranking Evaluation

Reranking should be evaluated using ranking metrics.

Examples:

* Precision@K
* Recall@K
* MRR
* NDCG

Good reranking should improve the quality of the final Top-K results.

---

# Latency Tradeoff

Reranking improves quality but adds latency.

Tradeoff:

```text
better relevance
vs
slower responses
```

Production systems must balance both.

---

# Cost Tradeoff

Reranking may require additional model calls.

This increases:

* computation
* API cost
* latency

For large systems, reranking strategy must be carefully designed.

---

# When Reranking is Most Useful

Reranking is especially useful when:

* retrieval returns noisy results
* queries are complex
* scientific precision matters
* hybrid search is used
* retrieved candidates are many
* final context must be small

---

# Common Mistakes

## Retrieving Too Few Candidates

If the correct chunk is not retrieved initially, reranking cannot recover it.

---

## Reranking Too Many Candidates

This may become slow and expensive.

---

## Ignoring Metadata

Semantic relevance alone may not be enough.

---

## Evaluating Only Final Answers

Reranking quality should also be evaluated directly.

---

# Reranking in This Project

Potential reranking signals:

```text
semantic similarity
run_id similarity
heater_voltage similarity
fan_voltage similarity
scintillation_index similarity
fried_parameter similarity
rytov_variance similarity
beam_wander similarity
analysis_module match
```

Potential use cases:

* experiment similarity search
* turbulence regime retrieval
* paper-to-experiment matching
* plot retrieval
* scientific comparison

---

# Key Insight

Reranking is a precision layer.

It improves RAG systems by turning broad retrieval into focused context selection.

A strong RAG system often uses:

```text
fast retrieval for recall
+
reranking for precision
```

This is especially important in scientific systems where the final context must be accurate, relevant, and traceable.
