# Metadata Filtering

---

# What is Metadata Filtering?

Metadata filtering is the process of restricting retrieval using structured information attached to documents or chunks.

In modern RAG systems, retrieval is often based on:

```text
semantic similarity
+
structured filtering
```

This allows systems to retrieve information that is not only semantically relevant, but also satisfies specific conditions.

---

# What is Metadata?

Metadata is:

```text
information about information
```

Metadata describes properties associated with a document, chunk, image, experiment, or embedding.

Examples:

```json
{
  "experiment": "run_42",
  "heater_voltage": 16,
  "scintillation_index": 0.31,
  "regime": "strong turbulence",
  "date": "2026-05-04"
}
```

The metadata is not the main content itself.

It is structured contextual information.

---

# Why Metadata Matters

Semantic search alone is often insufficient.

Example:

```text
"find strong turbulence experiments"
```

Semantic retrieval may return:

* related experiments
* papers
* discussions
* weak turbulence examples

But suppose we want:

```text
ONLY experiments with:
heater_voltage > 10
```

This requires structured filtering.

---

# Core Idea

Metadata filtering combines:

```text
semantic meaning
```

with:

```text
structured constraints
```

This is one of the most powerful capabilities of modern vector databases.

---

# Typical Retrieval Pipeline

Without filtering:

```text
Query
   ↓
Semantic Search
   ↓
Top-K Results
```

With filtering:

```text
Query
   ↓
Metadata Constraints
   ↓
Semantic Search
   ↓
Filtered Results
```

---

# Examples of Metadata

## Document Metadata

```json
{
  "author": "John Doe",
  "year": 2025,
  "topic": "RAG"
}
```

---

## Scientific Metadata

```json
{
  "heater_voltage": 16,
  "fan_voltage": 7,
  "fried_parameter": 0.002,
  "regime": "strong turbulence"
}
```

---

## Image Metadata

```json
{
  "resolution": "1920x1080",
  "camera": "Basler",
  "timestamp": "2026-05-04"
}
```

---

# Why Metadata Filtering is Powerful

Metadata filtering enables:

* precise retrieval
* controlled context selection
* domain-aware search
* structured querying
* scientific filtering
* efficient narrowing of search space

Without filtering, retrieval can become noisy.

---

# Semantic Search Alone is Not Enough

Semantic retrieval answers:

```text
what is conceptually similar?
```

Metadata filtering answers:

```text
what satisfies structured constraints?
```

Modern systems usually need both.

---

# Example

Suppose the query is:

```text
"retrieve experiments with strong beam wander"
```

The system may also apply filters:

```text
heater_voltage > 10
AND
scintillation_index > 0.3
```

This dramatically improves retrieval precision.

---

# Types of Metadata Filters

## Equality Filters

Example:

```text
regime = "strong turbulence"
```

---

## Range Filters

Example:

```text
scintillation_index > 0.2
```

---

## Boolean Filters

Example:

```text
has_plots = true
```

---

## Date Filters

Example:

```text
date > "2026-05-01"
```

---

## Set Membership Filters

Example:

```text
regime IN ["weak", "moderate"]
```

---

# Filtering Before Retrieval

Some systems apply filters before semantic search.

Pipeline:

```text
Filter Candidates
      ↓
Semantic Retrieval
```

Advantages:

* faster retrieval
* reduced search space
* lower noise

---

# Filtering After Retrieval

Other systems retrieve first, then filter.

Pipeline:

```text
Semantic Retrieval
      ↓
Metadata Filtering
```

Advantages:

* preserves semantic recall

Disadvantages:

* more expensive
* potentially noisier

---

# Hybrid Retrieval Systems

Modern retrieval systems often combine:

```text
semantic retrieval
+
keyword search
+
metadata filtering
```

This creates highly flexible retrieval pipelines.

---

# Metadata and Chunking

Metadata is often attached to chunks.

Example:

```json
{
  "experiment": "run_42",
  "module": "beam_wander",
  "heater_voltage": 16
}
```

This allows retrieval at chunk level.

---

# Metadata and Traceability

Metadata improves:

```text
traceability
```

Meaning:

retrieved chunks can be linked back to:

* original documents
* experiments
* papers
* figures
* runs

This is critical in scientific systems.

---

# Metadata in Vector Databases

Most vector databases support metadata payloads.

Examples:

* Qdrant
* Pinecone
* Weaviate

Typical structure:

```text
vector
+
payload
```

Where:

* vector → semantic representation
* payload → structured metadata

---

# Metadata Indexing

Some databases index metadata separately.

This improves:

* filtering speed
* scalability
* query efficiency

Important for large datasets.

---

# Metadata and Scientific Systems

Scientific retrieval systems depend heavily on metadata.

Examples:

* experimental conditions
* acquisition parameters
* turbulence regimes
* timestamps
* statistical metrics
* instrument settings

Metadata often becomes as important as semantic retrieval itself.

---

# Example Scientific Query

```text
"Find experiments similar to this turbulence regime"
```

Possible retrieval pipeline:

```text
Semantic Similarity:
beam behavior

Metadata Filters:
heater_voltage > 12
beam_wander_rms > threshold
scintillation_index > 0.3
```

---

# Metadata and Context Quality

Filtering improves:

* retrieval precision
* prompt quality
* grounding
* reasoning quality

By reducing:

* irrelevant context
* noisy retrieval
* unrelated documents

---

# Metadata and Hallucinations

Good filtering can reduce hallucinations.

Why?

Because the LLM receives:

```text
more relevant evidence
```

instead of broad noisy context.

---

# Metadata Design

Good metadata should be:

* consistent
* structured
* searchable
* meaningful
* domain-relevant

Bad metadata design causes:

* poor filtering
* retrieval confusion
* inconsistent queries

---

# Common Metadata Fields

## General AI Systems

```text
source
author
date
topic
language
```

---

## Scientific Systems

```text
experiment_id
regime
heater_voltage
fan_voltage
fried_parameter
rytov_variance
beam_wander
scintillation_index
```

---

# Metadata in This Project

Potential metadata fields:

```text
run_id
heater_voltage
fan_voltage
fps
exposure
fried_parameter
rytov_variance
scintillation_index
beam_wander
regime
analysis_module
```

Potential retrieval tasks:

```text
retrieve experiments with:
- strong turbulence
- high beam wander
- low Fried parameter
- similar morphology
```

---

# Future Multimodal Metadata

Future systems may include metadata for:

* plots
* images
* videos
* temporal sequences
* multimodal embeddings

Example:

```json
{
  "plot_type": "beam_profile",
  "regime": "strong turbulence",
  "fwhm": 14.2
}
```

---

# Common Problems

## Missing Metadata

Important filtering becomes impossible.

---

## Inconsistent Metadata

Queries become unreliable.

---

## Excessive Metadata

Too many fields increase complexity.

---

## Poor Naming

Difficult query construction.

---

# Key Insight

Metadata filtering fundamentally allows:

```text
semantic retrieval with structure
```

This transforms retrieval systems from:

```text
general semantic search
```

into:

```text
controlled domain-aware retrieval
```

Modern scientific RAG systems rely heavily on metadata filtering for precision, traceability, and scalable retrieval.
