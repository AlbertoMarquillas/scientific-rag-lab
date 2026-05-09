# Hybrid Search

---

# What is Hybrid Search?

Hybrid search combines:

```text
semantic retrieval
+
traditional retrieval
```

instead of relying on only one retrieval strategy.

Most modern production retrieval systems use:

```text
multiple retrieval signals together
```

Hybrid retrieval is one of the foundations of high-quality RAG systems.

---

# Core Idea

Semantic retrieval is powerful because it captures:

```text
meaning
```

Traditional retrieval is powerful because it captures:

```text
exact matching
```

Hybrid search combines both strengths.

---

# Why Hybrid Search Exists

Pure vector search may:

* miss exact identifiers
* retrieve semantically noisy results
* ignore critical keywords
* retrieve overly broad matches

Pure keyword search may:

* miss semantic relationships
* fail on paraphrases
* fail on synonyms
* fail on implicit meaning

Hybrid search attempts to solve both problems.

---

# Semantic Search

Semantic search uses:

```text
embeddings
+
vector similarity
```

It retrieves:

```text
semantically related information
```

instead of exact keyword overlap.

---

# Keyword Search

Keyword search uses:

```text
exact lexical matching
```

Examples:

* BM25
* TF-IDF
* inverted indexes

Keyword retrieval excels at:

* exact identifiers
* technical terms
* rare tokens
* precise matches

---

# Why Semantic Search Alone is Insufficient

Suppose query:

```text
Module 40 optical turbulence
```

Pure semantic retrieval may:

* retrieve unrelated turbulence concepts
* miss exact module references
* retrieve broad optical propagation discussions

Keyword signals help preserve precision.

---

# Why Keyword Search Alone is Insufficient

Suppose query:

```text
strong atmospheric instability
```

Relevant documents may contain:

```text
beam scintillation
optical turbulence
beam distortion
```

without exact phrase overlap.

Semantic retrieval captures these relationships.

---

# Hybrid Retrieval Pipeline

Typical flow:

```text
user query
      ↓
semantic retrieval
+
keyword retrieval
      ↓
merge results
      ↓
rerank
      ↓
return final candidates
```

Hybrid systems combine multiple retrieval mechanisms.

---

# Retrieval Signals

Hybrid search may combine:

* vector similarity
* BM25 scores
* metadata filters
* reranking scores
* recency signals
* popularity signals

Modern retrieval systems are multi-signal systems.

---

# BM25

One of the most important keyword retrieval algorithms:

```text
BM25
```

BM25 ranks documents using:

* term frequency
* inverse document frequency
* document length normalization

Widely used in traditional information retrieval.

---

# Why BM25 Still Matters

Even in modern AI systems:

BM25 is extremely strong for:

* exact phrases
* identifiers
* technical terminology
* short queries
* rare tokens

Semantic search does not fully replace lexical retrieval.

---

# Semantic Retrieval Strengths

Vector retrieval excels at:

* paraphrases
* conceptual similarity
* semantic meaning
* implicit relationships
* fuzzy language

This complements keyword retrieval.

---

# Combining Scores

Hybrid systems often combine:

```text
semantic similarity score
+
keyword relevance score
```

Results are merged or reranked.

Score fusion becomes an important engineering challenge.

---

# Weighted Retrieval

Hybrid systems may assign:

```text
weights
```

to different retrieval methods.

Example:

```text
70% semantic
30% lexical
```

Weighting strongly affects retrieval behavior.

---

# Why Weighting Matters

Too much semantic retrieval:

* noisy results
* weak exact matching

Too much keyword retrieval:

* poor semantic flexibility
* weak paraphrase handling

Balanced retrieval improves robustness.

---

# Hybrid Retrieval and Metadata

Hybrid systems also commonly use:

```text
metadata filtering
```

Example:

```text
semantic retrieval
+
BM25
+
metadata constraints
```

This creates highly controllable retrieval.

---

# Example Hybrid Query

Example:

```text
Find experiments related to:
strong scintillation
WHERE module = optical_turbulence
```

System may use:

* vector similarity
* BM25 keyword matching
* payload filtering

---

# Why Hybrid Search Improves RAG

RAG quality depends heavily on retrieval quality.

Hybrid retrieval improves:

* precision
* recall
* grounding
* exact matching
* semantic flexibility

Modern RAG systems rarely rely on pure vector search alone.

---

# Retrieval Precision

Keyword retrieval often improves:

```text
precision
```

because exact terms remain important.

Examples:

* module names
* IDs
* formulas
* variable names
* experiment identifiers

---

# Retrieval Recall

Semantic retrieval often improves:

```text
recall
```

because semantically related concepts can still be retrieved.

Hybrid search balances both.

---

# Hybrid Search and Reranking

Many systems also apply:

```text
reranking
```

after hybrid retrieval.

Pipeline:

```text
semantic retrieval
+
keyword retrieval
      ↓
candidate set
      ↓
reranking model
```

Reranking further improves retrieval quality.

---

# Why Retrieval Pipelines Become Complex

Modern retrieval systems may contain:

* embeddings
* BM25
* metadata filters
* rerankers
* recency weighting
* personalization

Retrieval engineering becomes sophisticated infrastructure work.

---

# Hybrid Search and Qdrant

Qdrant supports:

* vector retrieval
* metadata filtering
* hybrid retrieval integration

Qdrant is often combined with:

* BM25 engines
* rerankers
* retrieval orchestration systems

---

# Hybrid Retrieval and Agents

Agents often benefit from hybrid retrieval because:

* exact tools matter
* semantic flexibility matters
* memory recall matters
* identifiers matter

Agent retrieval systems are frequently hybrid.

---

# Hybrid Search and Scientific Systems

Scientific retrieval especially benefits from hybrid search.

Scientific queries often contain:

* formulas
* identifiers
* module names
* parameter values
* scientific terminology

Exact lexical matching remains important.

---

# Example Scientific Query

Example:

```text
Module 40 strong turbulence with high scintillation
```

Semantic retrieval captures:

* turbulence concepts
* beam instability
* optical propagation

Keyword retrieval captures:

* exact module references
* exact terminology

Hybrid retrieval combines both.

---

# Hybrid Search in This Project

Potential retrieval targets:

```text
experiment summaries
module analyses
comparison reports
paper chunks
scientific notes
```

Potential retrieval signals:

```text
semantic embeddings
+
module names
+
run IDs
+
scientific metadata
+
technical terminology
```

Hybrid retrieval fits your project extremely well.

---

# Why Hybrid Search is Important for Your Project

Your experiments contain:

* semantic scientific observations
* exact module names
* exact metrics
* numeric metadata
* structured identifiers

Pure vector retrieval would likely lose important precision.

Hybrid search solves this.

---

# Hybrid Retrieval and Observability

Production systems monitor:

* retrieval latency
* retrieval quality
* score distributions
* reranking quality
* retrieval source contribution

Hybrid systems require observability.

---

# Hybrid Retrieval and Evaluation

Evaluation may compare:

* vector-only retrieval
* keyword-only retrieval
* hybrid retrieval

Hybrid systems often outperform pure approaches.

---

# Retrieval Complexity

As retrieval systems evolve:

* pipelines become deeper
* scoring becomes harder
* orchestration becomes important
* observability becomes essential

Retrieval engineering becomes infrastructure engineering.

---

# Common Misconceptions

## “Vector Search Replaces Keyword Search”

Usually false.

Modern systems often combine both.

---

## “Semantic Retrieval Understands Everything”

Exact identifiers and keywords still matter.

---

## “Hybrid Retrieval is Simple”

Score fusion and orchestration can become complex.

---

# Common Mistakes

## Ignoring Exact Matching

Critical identifiers may disappear.

---

## Overweighting Semantic Search

Retrieval becomes noisy.

---

## Overweighting Keywords

Semantic flexibility weakens.

---

## No Reranking

Candidate quality may remain weak.

---

## Weak Metadata Design

Hybrid retrieval becomes less controllable.

---

# Recommended Mental Model

Useful perspective:

```text
hybrid search combines meaning and precision
```

Semantic retrieval captures:

```text
conceptual similarity
```

Keyword retrieval captures:

```text
exact lexical information
```

Modern retrieval systems need both.

---

# Important Insight

The strongest retrieval systems are often not:

```text
pure vector systems
```

or:

```text
pure keyword systems
```

but:

```text
hybrid multi-signal retrieval systems
```

combining semantic and lexical information.

---

# Key Insight

Modern production retrieval systems increasingly combine:

```text
embeddings
+
vector similarity
+
keyword retrieval
+
metadata filtering
+
reranking
+
retrieval orchestration
```

Hybrid search is one of the key architectural ideas enabling robust, precise, and scalable RAG systems.
