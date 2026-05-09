# Embeddings

---

# What is an Embedding?

An embedding is a numerical vector representation of information.

The purpose of an embedding is to transform complex data into a mathematical representation that preserves semantic meaning.

Very simplified idea:

```text
text / image / data
        ↓
vector representation
```

Embeddings allow machines to compare meaning mathematically.

---

# Why Embeddings Exist

Computers cannot directly understand:

* language
* meaning
* concepts
* semantic similarity

Computers operate on numbers.

Embeddings convert information into numerical spaces where:

```text
similar meanings → nearby vectors
```

This is one of the foundations of modern AI systems.

---

# Basic Intuition

Suppose we have two sentences:

```text
"strong optical turbulence"
```

and:

```text
"severe atmospheric distortion"
```

Even though the words are different, the meanings are related.

A good embedding model produces vectors that are close together in vector space.

---

# Embedding Space

Embeddings exist inside a mathematical space called:

```text
vector space
```

Each piece of information becomes a point in that space.

Conceptually:

```text
similar concepts cluster together
```

while unrelated concepts remain far apart.

---

# Example

Very simplified representation:

```text
"cat"     → [0.12, 0.44, -0.31, ...]
"dog"     → [0.10, 0.41, -0.28, ...]
"galaxy"  → [-0.77, 0.92, 0.11, ...]
```

The vectors for:

```text
cat
```

and:

```text
dog
```

are closer than:

```text
cat
```

and:

```text
galaxy
```

because their meanings are more related.

---

# Embedding Dimensions

Embeddings usually contain hundreds or thousands of dimensions.

Examples:

* 384 dimensions
* 768 dimensions
* 1536 dimensions
* 3072 dimensions

Each dimension represents learned abstract features.

Humans usually cannot interpret individual dimensions directly.

Meaning emerges from the full vector.

---

# Semantic Similarity

The core idea behind embeddings:

```text
semantic similarity becomes geometric similarity
```

Meaning can be measured mathematically.

---

# Cosine Similarity

The most common similarity metric is:

```text
cosine similarity
```

Formula:

genui{"math_block_widget_always_prefetch_v2":{"content":"\cos(\theta)=\frac{\vec a \cdot \vec b}{\|a\|\|b\|}"}}

Where:

* vectors pointing in similar directions produce high similarity
* vectors pointing in different directions produce low similarity

---

# Why Cosine Similarity Works

Cosine similarity measures:

```text
orientation
```

instead of:

```text
absolute magnitude
```

This is useful because semantic meaning is usually related more to:

```text
direction in embedding space
```

than vector length.

---

# Embedding Models

Embeddings are generated using embedding models.

Examples:

* OpenAI embedding models
* Sentence Transformers
* BERT-based models
* E5 models
* Instructor models
* CLIP embeddings

Different models are optimized for:

* retrieval
* clustering
* classification
* multimodal understanding
* scientific text

---

# Text Embeddings

Most RAG systems start with text embeddings.

Pipeline:

```text
Text
   ↓
Tokenizer
   ↓
Embedding Model
   ↓
Vector
```

The resulting vector represents semantic meaning.

---

# Image Embeddings

Embeddings are not limited to text.

Images can also be embedded.

Pipeline:

```text
Image
   ↓
Vision Model
   ↓
Embedding Vector
```

This enables:

* image retrieval
* similarity search
* multimodal AI systems

---

# Multimodal Embeddings

Some models can embed:

* text
* images
* audio

inside the same vector space.

This allows relationships like:

```text
text query ↔ image retrieval
```

Examples:

* CLIP
* multimodal transformers

---

# Embeddings in RAG

Embeddings are one of the core components of RAG systems.

Typical pipeline:

```text
Documents
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database
```

When a user asks a question:

```text
User Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
```

The system retrieves semantically similar information.

---

# Query Embeddings

The user query is also converted into an embedding.

This is critical.

The system compares:

```text
query vector
```

against:

```text
document vectors
```

inside the vector database.

---

# Embedding Quality

Not all embeddings are equally good.

Good embeddings should:

* preserve semantic meaning
* separate unrelated concepts
* cluster related concepts
* generalize well

Poor embeddings produce poor retrieval.

---

# Embedding Drift

Embedding spaces depend on the model.

Changing embedding models may:

* shift vector distributions
* break compatibility
* require reindexing

This is important in production systems.

---

# Chunk Embeddings

In RAG systems, embeddings are usually generated for:

```text
chunks
```

instead of full documents.

Why?

Because:

* retrieval becomes more precise
* context becomes smaller
* semantic specificity improves

---

# Embedding Tradeoffs

Larger embeddings usually:

* capture richer semantics
* improve retrieval quality

but also:

* require more storage
* increase computation
* increase search costs

Real systems must balance:

```text
quality vs efficiency
```

---

# Clustering in Embedding Space

Embeddings naturally create clusters.

Conceptually:

```text
similar topics → nearby regions
```

Examples:

* turbulence papers
* centroid analysis
* beam morphology
* scintillation metrics

may cluster together automatically.

---

# Embeddings and Retrieval

Retrieval systems use embeddings to perform:

```text
nearest neighbor search
```

Goal:

```text
find vectors most similar to the query vector
```

This enables semantic search.

---

# Dense Retrieval

Embedding-based retrieval is usually called:

```text
dense retrieval
```

because vectors are dense numerical representations.

Dense retrieval differs from:

```text
sparse retrieval
```

which relies more on keyword matching.

---

# Embeddings for Scientific Data

Scientific embeddings are especially important because:

* terminology is complex
* wording varies
* concepts are highly related
* semantic retrieval matters more than exact keywords

Examples:

```text
"beam wander"
```

may relate semantically to:

```text
"centroid instability"
```

without exact word overlap.

---

# Embeddings in This Project

Potential embedding sources:

```text
metadata.json
analysis.json
comparison results
scientific notes
papers
plots
```

Potential future embeddings:

* turbulence regimes
* beam morphology
* temporal behavior
* experimental conditions
* image embeddings
* multimodal embeddings

---

# Important Limitations

Embeddings are powerful but imperfect.

Common limitations:

* semantic ambiguity
* retrieval noise
* domain mismatch
* weak scientific understanding
* information compression loss

Embeddings do not perfectly represent meaning.

They approximate semantic relationships.

---

# Key Insight

Embeddings transform:

```text
meaning
```

into:

```text
geometry
```

This allows AI systems to perform:

* semantic retrieval
* similarity search
* clustering
* recommendation
* multimodal search

using mathematical operations in vector space.
