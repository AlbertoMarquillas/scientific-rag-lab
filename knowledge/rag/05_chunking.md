# Chunking

---

# What is Chunking?

Chunking is the process of dividing information into smaller pieces called:

```text
chunks
```

In RAG systems, chunking is one of the most important preprocessing steps.

The quality of chunking strongly affects:

* retrieval quality
* context quality
* hallucinations
* reasoning performance
* embedding quality

Many RAG systems fail primarily because of poor chunking.

---

# Why Chunking Exists

LLMs and embedding models cannot efficiently process:

* entire books
* huge PDFs
* large datasets
* complete scientific papers

as single units.

Problems with very large documents:

* context limits
* semantic dilution
* poor retrieval precision
* inefficient embeddings

Chunking solves this by dividing information into smaller semantic units.

---

# Basic Idea

Instead of embedding:

```text
entire document
```

we embed:

```text
small meaningful sections
```

Example:

```text
Paper
  ↓
Introduction chunk
Methods chunk
Results chunk
Discussion chunk
```

This improves semantic retrieval.

---

# What Makes a Good Chunk?

A good chunk should:

* contain coherent meaning
* preserve context
* avoid unrelated topics
* fit inside token limits
* remain semantically useful

A chunk should ideally represent:

```text
one semantic idea
```

---

# Chunk Size

Chunk size is one of the most important parameters.

Usually measured in:

```text
tokens
```

Examples:

* 128 tokens
* 256 tokens
* 512 tokens
* 1024 tokens

---

# Small Chunks

Advantages:

* precise retrieval
* cleaner embeddings
* lower noise
* more focused semantics

Disadvantages:

* loss of context
* fragmented information
* incomplete reasoning

---

# Large Chunks

Advantages:

* richer context
* more complete information
* better local reasoning

Disadvantages:

* semantic dilution
* noisier retrieval
* irrelevant information
* larger prompts

---

# Chunking Tradeoff

Chunking is fundamentally a balance between:

```text
precision
```

and:

```text
context preservation
```

This is one of the core optimization problems in RAG systems.

---

# Overlap

Chunks often include overlapping regions.

Example:

```text
Chunk 1:
[Sentence 1 ... Sentence 10]

Chunk 2:
[Sentence 8 ... Sentence 18]
```

Overlap helps preserve continuity between chunks.

---

# Why Overlap Matters

Without overlap:

* information may be split abruptly
* relationships may disappear
* retrieval may lose context

Overlap improves:

* semantic continuity
* retrieval robustness
* reasoning quality

---

# Overlap Tradeoffs

Too little overlap:

* context fragmentation
* semantic discontinuities

Too much overlap:

* duplicated information
* wasted storage
* retrieval redundancy
* larger indexes

---

# Fixed-Size Chunking

Simplest approach.

Documents are split every:

```text
N tokens
```

Example:

```text
split every 512 tokens
```

Advantages:

* simple
* fast
* scalable

Disadvantages:

* ignores semantic structure
* may split ideas incorrectly

---

# Recursive Chunking

More advanced approach.

The system tries to split using:

1. sections
2. paragraphs
3. sentences
4. words

Goal:

```text
preserve semantic structure as much as possible
```

Very common in modern RAG systems.

---

# Semantic Chunking

Semantic chunking attempts to split information based on:

```text
meaning
```

instead of fixed token counts.

Example:

* one chunk per concept
* one chunk per experiment
* one chunk per section

This often improves retrieval quality significantly.

---

# Sentence-Based Chunking

Chunks are built using full sentences.

Advantages:

* grammatical coherence
* cleaner semantics

Disadvantages:

* variable chunk sizes
* inconsistent token lengths

---

# Structure-Aware Chunking

Very important for scientific systems.

The chunker uses document structure:

* titles
* headings
* tables
* figures
* sections
* metadata

Examples:

```text
Methods
Results
Discussion
```

can become separate chunks.

---

# Chunking for Scientific Papers

Scientific papers are especially sensitive to chunking quality.

Poor chunking may:

* separate equations from explanations
* disconnect figures from captions
* break methodological context
* fragment experimental descriptions

Good scientific chunking preserves:

* conceptual coherence
* experimental context
* numerical relationships

---

# Chunking and Embeddings

Chunking directly affects embeddings.

Bad chunks produce:

* noisy embeddings
* weak semantic representation
* poor retrieval

Good chunks produce:

* focused embeddings
* stronger semantic clustering
* cleaner retrieval

---

# Chunking and Retrieval

Chunk size affects retrieval behavior.

Small chunks:

```text
higher precision
```

Large chunks:

```text
higher contextual richness
```

The best configuration depends on:

* document type
* retrieval goals
* model capabilities
* application domain

---

# Chunking and Context Windows

Chunking is heavily related to:

```text
LLM context limits
```

Retrieved chunks eventually enter the prompt.

If chunks are too large:

* prompts become expensive
* context overload increases
* irrelevant information grows

---

# Metadata-Aware Chunking

Chunks can include metadata.

Example:

```json
{
  "experiment": "run_42",
  "section": "beam wander",
  "heater_voltage": 16
}
```

This improves:

* filtering
* retrieval precision
* traceability

---

# Hierarchical Chunking

Advanced systems may use multiple chunk levels.

Example:

```text
Document
   ↓
Section
   ↓
Paragraph
   ↓
Sentence
```

This enables:

* coarse retrieval
* fine retrieval
* hierarchical navigation

---

# Chunking Strategies in Practice

Typical chunk sizes:

| Use Case             | Typical Size |
| -------------------- | ------------ |
| Small notes          | 128-256      |
| General RAG          | 256-512      |
| Scientific documents | 512-1024     |
| Long-context systems | 1024+        |

These are not strict rules.

Optimal chunking depends on experimentation.

---

# Chunk Evaluation

Good chunking should improve:

* retrieval relevance
* semantic coherence
* grounding quality
* answer precision

Bad chunking often causes:

* hallucinations
* missing context
* retrieval noise
* fragmented reasoning

---

# Chunking in This Project

Potential chunk sources:

```text
metadata.json
analysis.json
comparison results
scientific notes
papers
plots
```

Potential chunking strategies:

* one chunk per experiment
* one chunk per metric category
* one chunk per turbulence regime
* one chunk per analysis module

Example:

```text
Chunk:
"Beam wander analysis for strong turbulence regime"
```

instead of embedding the full experiment report.

---

# Future Multimodal Chunking

Advanced systems may chunk:

* images
* plots
* videos
* time series
* sensor data

Examples:

* one chunk per figure
* one chunk per temporal segment
* one chunk per experimental event

---

# Common Chunking Mistakes

## Chunks Too Large

Problems:

* noisy retrieval
* diluted semantics
* larger prompts

---

## Chunks Too Small

Problems:

* missing context
* fragmented meaning
* incomplete reasoning

---

## Ignoring Structure

Problems:

* broken semantics
* disconnected explanations
* retrieval confusion

---

## No Overlap

Problems:

* abrupt information boundaries
* missing continuity

---

# Key Insight

Chunking is fundamentally:

```text
context engineering
```

A chunk defines:

```text
what information becomes retrievable
```

Good chunking creates:

* better embeddings
* better retrieval
* better prompts
* better reasoning

Poor chunking degrades the entire RAG pipeline.
