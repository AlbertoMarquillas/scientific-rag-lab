# RAG Overview

---

# What is RAG?

RAG stands for:

```text
Retrieval-Augmented Generation
```

RAG is an AI architecture that combines:

* information retrieval systems
* vector search
* large language models (LLMs)

The main idea behind RAG is simple:

> instead of forcing the language model to memorize all information during training, the system retrieves relevant external information dynamically at inference time.

---

# Why RAG Exists

Large Language Models have several limitations:

* limited context windows
* no reliable long-term memory
* outdated training data
* hallucinations
* inability to access private data directly

Without retrieval, an LLM can only answer using:

* its training data
* the prompt context

This creates major problems for:

* scientific systems
* company documentation
* private datasets
* dynamic information
* experimental databases

RAG solves this by allowing the model to retrieve external knowledge before generating a response.

---

# Core Idea

A RAG system works in two stages:

## 1. Retrieval

Relevant information is searched from an external knowledge source.

## 2. Generation

The retrieved information is injected into the prompt context and used by the LLM to generate the final answer.

The language model does not need to memorize the information.

It only needs to:

* understand the retrieved context
* reason over the retrieved context
* generate a grounded response

---

# Basic Architecture

```text
Documents / Data
        ↓
Chunking
        ↓
Embeddings
        ↓
Vector Database
        ↓
Retrieval
        ↓
Prompt Construction
        ↓
LLM Generation
```

---

# Main Components

## Documents / Data

The information source.

Examples:

* PDFs
* notes
* web pages
* experiment results
* scientific papers
* JSON files
* databases
* images
* metadata

---

## Chunking

Documents are divided into smaller pieces called chunks.

Chunking is important because:

* LLM context windows are limited
* embeddings work better on smaller semantic units
* retrieval becomes more accurate

---

## Embeddings

Each chunk is transformed into a numerical vector representation.

The embedding captures semantic meaning.

Semantically similar texts produce vectors that are close in vector space.

---

## Vector Database

Embeddings are stored inside a vector database.

The database allows efficient similarity search.

Examples:

* Qdrant
* Pinecone
* Weaviate
* Chroma
* FAISS

---

## Retrieval

When the user asks a question:

1. the query is converted into an embedding
2. the vector database searches for similar vectors
3. the most relevant chunks are returned

This process is called semantic retrieval.

---

## Prompt Construction

The retrieved chunks are inserted into the LLM prompt.

The prompt usually contains:

* system instructions
* user question
* retrieved context

---

## Generation

The LLM generates the final response using:

* the retrieved context
* the user query
* its reasoning capabilities

---

# Why Embeddings Matter

Traditional search relies mostly on keywords.

RAG systems rely heavily on semantic similarity.

Example:

```text
"beam wander under strong turbulence"
```

can retrieve documents containing:

```text
"large centroid fluctuations in saturated turbulence regimes"
```

Even if the exact words are different.

This is possible because embeddings capture semantic relationships.

---

# Typical RAG Pipeline

```text
Raw Documents
      ↓
Cleaning
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Storage
      ↓
Retrieval
      ↓
Context Injection
      ↓
LLM Response
```

---

# Types of Data Used in RAG

RAG systems are not limited to PDFs.

Possible data sources include:

* text documents
* scientific papers
* structured metadata
* databases
* experiment results
* logs
* images
* plots
* videos
* sensor measurements
* multimodal datasets

---

# Scientific RAG

Scientific RAG systems are designed to retrieve and reason over:

* papers
* experiments
* numerical metrics
* laboratory notes
* scientific datasets
* plots and figures

Scientific RAG is especially useful when:

* datasets are large
* experiments are difficult to organize manually
* information is distributed across many files
* semantic relationships matter

---

# RAG for Optical Turbulence Research

In this project, the long-term objective is to apply RAG techniques to optical turbulence experiments.

Potential data sources include:

```text
metadata.json
analysis.json
comparison results
scientific notes
papers
plots
```

Potential retrieval tasks:

* finding similar turbulence regimes
* comparing experiments
* retrieving papers related to experimental behavior
* searching experiments semantically
* AI-assisted scientific analysis

---

# Important Concepts to Learn Next

The most important topics after this overview are:

1. LLM context and limitations
2. embeddings
3. vector databases
4. chunking strategies
5. semantic retrieval
6. prompt construction
7. evaluation and hallucinations

These concepts form the foundation of modern RAG systems.

---

# Key Takeaway

A RAG system is fundamentally:

```text
retrieval system
+
language model
+
external knowledge
```

The model becomes more useful not because it memorizes more information, but because it can retrieve the right information at the right time.
