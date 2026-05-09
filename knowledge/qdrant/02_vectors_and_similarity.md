# Vectors and Similarity

---

# Why Vectors Matter

Modern AI systems increasingly represent information as:

```text
vectors
```

Vectors are numerical representations encoding:

```text
semantic meaning
```

Embeddings are vectors.

Semantic retrieval depends entirely on vector representations.

---

# Core Idea

Instead of representing information as:

```text
raw text only
```

embedding models transform information into:

```text
points in high-dimensional space
```

Semantically similar information becomes:

```text
geometrically close
```

inside vector space.

---

# What is a Vector?

Mathematically:

```text
v = [x1, x2, x3, ..., xn]
```

A vector is simply:

```text
an ordered list of numbers
```

Example:

```text
[0.14, -0.83, 1.22, 0.09, ...]
```

Modern embeddings may contain:

* hundreds of dimensions
* thousands of dimensions

---

# What Do These Numbers Mean?

Individual dimensions usually do NOT have direct human interpretation.

Instead:

```text
meaning emerges from the full vector geometry
```

Embedding spaces are learned statistical representations.

---

# Embedding Models

Embedding models transform:

```text
text
images
plots
scientific summaries
```

into vectors.

Examples:

* OpenAI embeddings
* sentence-transformers
* BGE
* E5
* CLIP

Pipeline:

```text
raw information
      ↓
embedding model
      ↓
vector
```

---

# Semantic Meaning in Vector Space

Core principle:

```text
similar meaning
→ similar vectors
```

Example:

```text
"optical turbulence"
```

may be geometrically close to:

```text
"beam propagation instability"
```

Even if exact words differ.

---

# Why This is Powerful

Traditional search relies on:

```text
exact keyword overlap
```

Vector retrieval enables:

```text
meaning-based retrieval
```

This is foundational for modern RAG systems.

---

# High-Dimensional Space

Embeddings exist in:

```text
high-dimensional vector spaces
```

Examples:

```text
384 dimensions
768 dimensions
1536 dimensions
3072 dimensions
```

Humans cannot visualize these spaces directly.

---

# Geometric Interpretation

Conceptually:

```text
similar concepts cluster together
```

inside embedding space.

Example:

```text
strong turbulence experiments
```

may cluster near:

```text
high scintillation
beam spreading
centroid instability
```

---

# Similarity Search

Core retrieval operation:

```text
find nearest vectors
```

Conceptually:

```text
query vector
      ↓
search nearby vectors
      ↓
retrieve semantically similar content
```

This is the foundation of semantic search.

---

# Nearest Neighbor Search

Important concept:

```text
nearest neighbors
```

Vectors close together are assumed to represent:

```text
related semantic meaning
```

Qdrant retrieves nearest neighbors efficiently.

---

# Why Similarity is Mathematical

Similarity is computed numerically.

The database does not:

```text
understand language
```

It computes:

```text
vector relationships
```

through mathematical similarity metrics.

---

# Similarity Metrics

Common metrics:

* cosine similarity
* dot product
* Euclidean distance

These measure how close vectors are.

---

# Cosine Similarity

One of the most common metrics.

Measures:

```text
angle similarity between vectors
```

Conceptually:

```text
similar direction
→ similar meaning
```

Widely used in semantic retrieval.

---

# Dot Product

Measures:

```text
vector alignment and magnitude interaction
```

Often used in:

* neural retrieval systems
* recommendation systems
* transformer embeddings

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

Less common for modern semantic embeddings.

---

# Why Metric Choice Matters

Different metrics influence:

* retrieval quality
* ranking behavior
* clustering
* search performance

Metric selection is an important system design decision.

---

# Embedding Space Geometry

Embedding spaces often contain:

* clusters
* semantic neighborhoods
* relationships
* latent structure

Retrieval systems exploit this geometry.

---

# Semantic Clusters

Example conceptual clusters:

```text
beam wander
scintillation
FWHM broadening
optical distortion
```

Similar concepts may occupy nearby regions.

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
similarity search
```

Retrieval occurs in vector space.

---

# Example Retrieval Flow

Example:

```text
Query:
"strong turbulence with beam fragmentation"
```

Pipeline:

```text
embed query
      ↓
search vector space
      ↓
retrieve nearby experiment summaries
```

This is semantic retrieval.

---

# Why Embedding Quality Matters

Vector quality determines retrieval quality.

Poor embeddings produce:

* weak similarity
* irrelevant retrieval
* semantic confusion
* poor clustering

Embeddings are foundational.

---

# Garbage In → Garbage Out

If embeddings represent:

```text
poor chunks
noise
corrupted summaries
```

retrieval quality collapses.

Good retrieval depends on:

* chunking
* embeddings
* metadata
* indexing

---

# Similarity ≠ Truth

Important limitation.

Vector similarity means:

```text
statistical semantic proximity
```

not:

```text
factual correctness
```

Retrieval systems still require:

* grounding
* evaluation
* verification

---

# Approximate Nearest Neighbor Search

Searching all vectors exactly becomes expensive.

Large systems use:

```text
ANN
```

Approximate Nearest Neighbor search.

ANN trades:

```text
slight accuracy loss
```

for:

```text
massive speed improvements
```

---

# Why ANN Matters

Production systems may contain:

* millions of chunks
* billions of vectors
* multimodal embeddings

Efficient indexing becomes essential.

---

# Similarity Ranking

Retrieved vectors are usually ranked by:

```text
similarity score
```

Higher similarity:

```text
more likely semantically related
```

Ranking determines retrieval order.

---

# Retrieval Thresholds

Systems may apply:

```text
minimum similarity thresholds
```

Low similarity results may be:

* discarded
* reranked
* filtered

Threshold tuning affects retrieval behavior.

---

# Similarity Search and Metadata

Semantic retrieval is often combined with:

```text
metadata filtering
```

Example:

```text
similar experiments
WHERE heater_voltage > 10
```

This hybrid approach is extremely powerful.

---

# Hybrid Retrieval

Modern retrieval often combines:

* embeddings
* keyword search
* metadata filters
* reranking

Embeddings are one component of retrieval systems.

---

# Embeddings and Multimodality

Vectors may represent:

* text
* images
* plots
* audio
* video
* scientific descriptors

This enables multimodal retrieval.

---

# Visual Embeddings

Images can also become vectors.

Example:

```text
beam profile image
      ↓
image embedding
      ↓
visual similarity search
```

This enables visual retrieval systems.

---

# Scientific Embeddings

Scientific systems may embed:

* experiment summaries
* module outputs
* plot descriptions
* turbulence observations
* comparison reports

These embeddings enable scientific semantic retrieval.

---

# Scientific Similarity Search

Possible query:

```text
Find experiments similar to:
strong beam wander with stable mean intensity
```

Retrieval may use:

* semantic embeddings
* metadata filtering
* vector similarity

---

# Similarity Search in This Project

Potential embedded objects:

```text
experiment summaries
module analyses
scientific observations
paper chunks
comparison descriptions
```

Potential retrieval tasks:

* turbulence regime similarity
* experiment clustering
* semantic scientific exploration
* paper-experiment linking

---

# Embedding Design Matters

Important design decisions:

* what to embed
* chunk size
* metadata structure
* embedding model choice
* retrieval strategy

Retrieval quality depends heavily on embedding architecture.

---

# Common Misconceptions

## “Vectors Store Meaning Explicitly”

Meaning emerges statistically from geometry.

Individual dimensions rarely have direct interpretation.

---

## “Nearest Neighbor Means Correct Answer”

Similarity ≠ factual correctness.

Retrieval still requires evaluation.

---

## “Better Embeddings Solve Everything”

Retrieval quality also depends on:

* chunking
* metadata
* reranking
* indexing
* filtering

---

# Common Mistakes

## Embedding Noisy Content

Retrieval quality degrades.

---

## Weak Chunking

Embeddings lose semantic coherence.

---

## Ignoring Metadata

Retrieval flexibility becomes limited.

---

## Treating Similarity as Truth

Retrieval errors become dangerous.

---

## No Retrieval Evaluation

Weak search quality remains hidden.

---

# Recommended Mental Model

Useful perspective:

```text
embeddings create geometric meaning spaces
```

Similarity search navigates these spaces.

Qdrant efficiently retrieves nearby semantic regions.

---

# Important Insight

Modern AI retrieval systems work because:

```text
semantic meaning
can be approximated geometrically
```

inside high-dimensional vector spaces.

This is one of the key ideas behind embeddings and semantic retrieval.

---

# Key Insight

Modern RAG systems fundamentally depend on:

```text
embeddings
+
vector similarity
+
nearest-neighbor retrieval
+
semantic geometry
```

Vector databases like Qdrant provide the infrastructure enabling efficient navigation through these semantic spaces at production scale.
