# What is RAG?

---

# Definition

RAG stands for:

```text
Retrieval-Augmented Generation
```

RAG is an AI architecture that combines:

* retrieval systems
* external knowledge sources
* large language models (LLMs)

The purpose of RAG is to allow a language model to answer questions using external information retrieved dynamically at inference time.

Instead of relying only on its internal training knowledge, the model can access relevant information before generating a response.

---

# Fundamental Idea

Traditional LLMs work mainly like this:

```text
Training Data
      ↓
LLM
      ↓
Answer
```

The model answers using:

* learned statistical patterns
* internal parameters
* information present during training

This creates important limitations:

* no access to new information
* no access to private information
* hallucinations
* limited reliability
* limited context capacity

RAG introduces a retrieval step.

---

# RAG Architecture

A RAG system works like this:

```text
External Knowledge
        ↓
Retrieval System
        ↓
Relevant Context
        ↓
LLM
        ↓
Grounded Answer
```

The model no longer depends only on memory.

Instead, it retrieves relevant information dynamically.

---

# Why Retrieval Matters

A language model cannot realistically memorize:

* all scientific papers
* all company documents
* all experimental datasets
* all user-specific information
* all updated information

Even very large models have:

* finite parameters
* finite context windows
* finite training cutoffs

Retrieval solves this problem by separating:

```text
knowledge storage
```

from:

```text
language reasoning
```

---

# Main Components of RAG

## 1. Knowledge Source

The external information source.

Examples:

* PDFs
* websites
* databases
* scientific papers
* notes
* experiment results
* JSON files
* APIs

---

## 2. Retrieval System

Responsible for searching relevant information.

Usually based on:

* embeddings
* vector search
* semantic similarity

The retrieval system decides:

```text
which information is relevant
```

for the current query.

---

## 3. Language Model

The LLM receives:

* the user query
* the retrieved information
* system instructions

Then generates the final answer.

The LLM becomes a reasoning engine over retrieved context.

---

# Retrieval vs Training

A very important distinction:

## Fine-Tuning

```text
knowledge is stored inside model weights
```

## RAG

```text
knowledge is retrieved externally
```

This difference is fundamental.

RAG allows:

* dynamic updates
* private data access
* scalable knowledge bases
* lower costs
* easier maintenance

without retraining the model.

---

# What Makes RAG Powerful

RAG combines:

## Retrieval

Ability to search large knowledge sources.

## Semantic Understanding

Ability to retrieve conceptually related information.

## Language Reasoning

Ability of LLMs to:

* summarize
* explain
* compare
* reason
* answer questions

---

# Example

Suppose the user asks:

```text
"What experiments show strong scintillation and large beam wander?"
```

The pipeline may work like this:

```text
User Query
      ↓
Embedding Generation
      ↓
Vector Search
      ↓
Relevant Experiment Chunks
      ↓
Prompt Construction
      ↓
LLM Response
```

The final answer is grounded on retrieved experiment data.

---

# Grounded Responses

One of the biggest advantages of RAG is grounding.

A grounded response means:

```text
the answer is based on retrieved evidence
```

instead of pure model generation.

Grounding helps reduce:

* hallucinations
* fabricated facts
* unsupported claims

---

# RAG vs Search Engines

Traditional search engines mostly rely on:

* keywords
* exact matching
* lexical similarity

Modern RAG systems usually rely on:

* embeddings
* semantic similarity
* vector search

This means retrieval can work even when:

* exact words are different
* wording changes
* synonyms are used
* concepts are related semantically

---

# Dense Retrieval

Most modern RAG systems use dense retrieval.

Dense retrieval means:

```text
text → dense numerical vectors
```

The vectors encode semantic meaning.

Semantically related texts are located close together in vector space.

---

# Typical RAG Workflow

## Offline Stage

Usually performed once during indexing.

```text
Documents
    ↓
Cleaning
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
```

---

## Online Stage

Executed for each user query.

```text
User Query
      ↓
Query Embedding
      ↓
Retrieval
      ↓
Context Injection
      ↓
LLM Generation
```

---

# Types of RAG Systems

## Basic RAG

Simple retrieval + generation.

---

## Hybrid RAG

Combines:

* vector search
* keyword search

---

## Agentic RAG

Uses AI agents capable of:

* tool usage
* planning
* iterative retrieval
* reasoning loops

---

## Multimodal RAG

Retrieves:

* text
* images
* plots
* audio
* video
* sensor data

---

# Common Problems in RAG

RAG systems are powerful but not perfect.

Common challenges:

* poor chunking
* weak embeddings
* irrelevant retrieval
* hallucinations
* context overload
* latency
* retrieval noise
* missing information

Building a good RAG system requires optimizing each stage.

---

# Scientific RAG

Scientific RAG systems are especially useful for:

* research papers
* experiment databases
* laboratory notes
* numerical results
* scientific datasets
* technical documentation

Scientific data is often:

* large
* fragmented
* multimodal
* difficult to search manually

RAG can help organize and retrieve this information semantically.

---

# RAG in This Project

In this project, the long-term objective is to build a scientific retrieval system for optical turbulence experiments.

Potential data sources include:

```text
metadata.json
analysis.json
comparison results
scientific notes
papers
plots
```

Potential future capabilities:

* semantic experiment search
* turbulence regime retrieval
* experiment similarity search
* AI-assisted scientific analysis
* multimodal scientific retrieval

---

# Key Takeaway

RAG fundamentally changes how language models use knowledge.

Instead of storing all information internally:

```text
knowledge is retrieved dynamically
```

This allows AI systems to:

* work with external data
* access updated information
* use private datasets
* scale knowledge efficiently
* generate more grounded responses
