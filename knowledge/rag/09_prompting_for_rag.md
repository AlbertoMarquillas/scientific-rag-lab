# Prompting for RAG

---

# What is Prompting in RAG?

In a RAG system, prompting is the process of constructing the input that will be sent to the language model.

The prompt usually combines:

```text
system instructions
+
retrieved context
+
user query
```

The quality of the prompt strongly affects:

* reasoning quality
* hallucinations
* grounding
* answer structure
* factual accuracy
* context usage

Even with excellent retrieval, poor prompting can significantly degrade system performance.

---

# Core Idea

The language model does not automatically know:

* which retrieved information is important
* how to use retrieved context
* how much confidence it should have
* which parts are evidence
* which parts are instructions

The prompt defines:

```text
how the model should reason over retrieved information
```

---

# Basic Prompt Structure

A typical RAG prompt may look like this:

```text
System Instructions

Retrieved Context

User Query
```

Example:

```text
You are a scientific assistant.

Context:
[Retrieved experiment chunks]

Question:
What experiments show strong scintillation?
```

---

# System Instructions

System instructions define:

* model behavior
* reasoning style
* response constraints
* formatting rules
* grounding requirements

Examples:

```text
Use only retrieved information.
```

```text
If information is missing, say so clearly.
```

```text
Cite retrieved evidence whenever possible.
```

---

# Retrieved Context

The retrieved context contains:

```text
external knowledge
```

inserted into the prompt.

Examples:

* experiment summaries
* scientific papers
* analysis results
* metadata
* notes

The retrieved context becomes the temporary working memory of the model.

---

# User Query

The user query defines:

```text
what information is needed
```

The retrieval system attempts to find relevant context for the query.

---

# Prompting and Grounding

Grounding means:

```text
answers should be based on retrieved evidence
```

Prompting plays a major role in grounding.

Weak prompts may cause:

* hallucinations
* unsupported claims
* ignored context

Strong prompts encourage:

* evidence-based reasoning
* context usage
* factual consistency

---

# Context Injection

RAG systems inject retrieved information into the prompt.

Conceptually:

```text
external knowledge
→
temporary LLM memory
```

The prompt acts as the interface between:

* retrieval
* reasoning

---

# Why Prompting Matters

Even if retrieval is perfect:

```text
bad prompts
→
bad answers
```

Examples of poor prompting:

* ambiguous instructions
* overloaded context
* conflicting instructions
* weak grounding constraints

---

# Prompt Engineering

Prompt engineering is the process of designing prompts that improve:

* reasoning quality
* grounding
* consistency
* structure
* reliability

Modern RAG systems rely heavily on good prompt engineering.

---

# Common Prompt Sections

Typical prompt components:

## Role Definition

Example:

```text
You are an expert scientific assistant.
```

---

## Behavioral Constraints

Example:

```text
Use only retrieved context.
```

---

## Retrieved Evidence

Example:

```text
[Retrieved chunks]
```

---

## Task Definition

Example:

```text
Compare the experiments.
```

---

## Formatting Instructions

Example:

```text
Answer using bullet points.
```

---

# Prompting Strategies

## Direct Answering

Simple QA prompting.

Example:

```text
Answer the question using the provided context.
```

---

## Step-by-Step Reasoning

Encourages structured reasoning.

Example:

```text
Reason step by step before answering.
```

---

## Evidence-Based Prompting

Encourages explicit grounding.

Example:

```text
Cite which retrieved chunks support the answer.
```

---

## Comparative Prompting

Useful for scientific systems.

Example:

```text
Compare similarities and differences between experiments.
```

---

# Prompt Length

Longer prompts are not always better.

Problems with overly large prompts:

* context overload
* reasoning degradation
* distraction
* higher costs
* increased latency

Good prompts maximize:

```text
signal / noise ratio
```

inside the context window.

---

# Prompt Ordering

Ordering matters.

Important information is often placed:

* near the beginning
* near the user query

Some models pay more attention to certain prompt regions.

---

# Retrieval Noise and Prompting

Retrieved context may contain irrelevant information.

Prompting can help reduce the impact of noise.

Example:

```text
Ignore irrelevant retrieved information.
Focus only on evidence related to the query.
```

---

# Hallucination Reduction

Prompting helps reduce hallucinations.

Examples:

```text
If the answer is not supported by retrieved context, say so explicitly.
```

```text
Do not invent information.
```

However:

prompting alone cannot fully solve hallucinations.

Good retrieval is still essential.

---

# Prompt Templates

Production systems often use templates.

Example:

```text
SYSTEM:
You are a scientific assistant.

CONTEXT:
{retrieved_chunks}

QUESTION:
{user_query}
```

Templates improve:

* consistency
* maintainability
* scalability

---

# Dynamic Prompt Construction

Modern systems build prompts dynamically.

Pipeline:

```text
Retrieve Context
      ↓
Select Relevant Chunks
      ↓
Construct Prompt
      ↓
Generate Response
```

The prompt changes for every query.

---

# Context Compression

Retrieved information may be compressed before insertion.

Examples:

* summarization
* chunk selection
* filtering
* reranking

Goal:

```text
maximize useful information density
```

inside the prompt.

---

# Prompting and Scientific Systems

Scientific systems require especially careful prompting because:

* precision matters
* numerical details matter
* ambiguity is dangerous
* hallucinations are costly

Scientific prompts often encourage:

* evidence-based reasoning
* cautious language
* structured comparison
* citation usage

---

# Example Scientific Prompt

```text
You are a scientific assistant specialized in optical turbulence.

Use only the retrieved experimental data.

If information is insufficient, state the limitation clearly.

Compare the experiments focusing on:
- scintillation
- beam wander
- Fried parameter
- turbulence regime

Retrieved Context:
[Chunks]

Question:
Which experiments show strong turbulence behavior?
```

---

# Prompting in This Project

Potential prompt goals:

* compare turbulence regimes
* retrieve similar experiments
* summarize experiment behavior
* analyze beam morphology
* connect papers with experiments
* explain turbulence metrics

Potential retrieved context:

```text
metadata.json
analysis.json
comparison results
scientific notes
papers
plots
```

---

# Common Prompting Problems

## Ambiguous Instructions

The model becomes inconsistent.

---

## Weak Grounding

The model ignores retrieved evidence.

---

## Excessive Context

Important information gets buried.

---

## Contradictory Context

The model becomes confused.

---

## Poor Formatting

Reasoning quality decreases.

---

# Advanced Prompting

Modern systems may include:

* chain-of-thought prompting
* self-reflection
* tool usage
* agentic reasoning
* iterative retrieval
* retrieval-aware prompting

These techniques are common in advanced AI systems.

---

# Key Insight

In RAG systems, prompting is fundamentally:

```text
context orchestration
```

The prompt determines:

* how retrieved information is interpreted
* how the model reasons
* how grounded the answer becomes
* how effectively context is used

Modern RAG systems depend heavily on:

```text
retrieval quality
+
prompt quality
```

Both components are essential for reliable AI systems.
