# Common Failure Modes

## Introduction

Modern local AI systems are complex.

A typical local RAG architecture may involve:

* local LLMs
* embeddings models
* vector databases
* retrieval pipelines
* APIs
* frontends
* GPUs
* storage systems
* orchestration frameworks

Failures can occur at any layer.

Understanding common failure modes is essential for:

* debugging
* system reliability
* observability
* production readiness
* scientific reproducibility
* performance optimization

---

# What Is a Failure Mode?

A failure mode is:

```text
A recurring way in which a system can malfunction or produce degraded behavior
```

Failure modes may be:

* obvious
* silent
* intermittent
* performance-related
* retrieval-related
* reasoning-related

Some failures crash the system.

Others quietly reduce quality.

---

# Why AI Systems Fail Differently

Traditional software failures are often deterministic.

AI systems introduce additional uncertainty:

* probabilistic outputs
* retrieval errors
* hallucinations
* prompt sensitivity
* context limitations
* model variability

AI failures are often subtle.

---

# High-Level Failure Categories

Common categories:

| Category       | Examples               |
| -------------- | ---------------------- |
| Infrastructure | GPU exhaustion         |
| Retrieval      | Wrong chunks retrieved |
| Prompting      | Prompt injection       |
| Inference      | Hallucinations         |
| Data           | Bad chunking           |
| Deployment     | Missing models         |
| Performance    | Slow inference         |
| Observability  | Missing logs           |

Understanding categories improves debugging.

---

# Infrastructure Failures

## VRAM Exhaustion

One of the most common local AI failures.

Causes:

* oversized model
* large context window
* multimodal inference
* concurrent requests

Symptoms:

* crashes
* swapping to RAM
* severe slowdown
* model unloads

---

## CPU Fallback

If GPU inference fails:

```text
Inference may silently move to CPU
```

Symptoms:

* extremely slow generation
* low GPU utilization
* low tokens per second

---

## Thermal Throttling

Heavy inference workloads may overheat hardware.

Symptoms:

* unstable performance
* sudden TPS drops
* high temperatures

---

## Disk Bottlenecks

Slow storage affects:

* model loading
* embeddings ingestion
* vector database performance

SSD storage is strongly preferred.

---

# Ollama-Specific Failures

## Model Not Installed

Example:

```text
Model not found
```

Cause:

Required model was not pulled.

---

## Ollama Server Not Running

Backend cannot connect to:

```text
http://localhost:11434
```

Symptoms:

* connection refused
* inference unavailable

---

## Wrong Model Tag

Example:

```text
qwen2.5
```

vs

```text
qwen2.5:7b
```

Incorrect tags cause runtime failures.

---

## Context Overflow

Prompt exceeds model context window.

Consequences:

* truncation
* dropped retrieval chunks
* degraded reasoning

---

# Retrieval Failures

## Poor Chunking

One of the most common RAG failures.

Problems:

* important information split incorrectly
* chunks too small
* chunks too large
* missing semantic boundaries

Retrieval quality degrades significantly.

---

## Weak Embeddings

Poor embeddings reduce semantic retrieval quality.

Symptoms:

* irrelevant chunks
* weak similarity search
* hallucinations

Embeddings quality strongly affects RAG quality.

---

## Missing Metadata

Without metadata:

* filtering becomes difficult
* retrieval becomes noisy
* experiments become hard to isolate

Metadata is essential in serious systems.

---

## Vector Dimension Mismatch

Changing embedding models without reindexing may cause:

```text
Vector size mismatch
```

Vectors from different models are incompatible.

---

## Empty Retrieval

Retriever returns no useful context.

Possible causes:

* ingestion failed
* wrong collection
* weak embeddings
* metadata filters too strict

---

## Retrieval Noise

Too many irrelevant chunks retrieved.

Consequences:

* noisy prompts
* hallucinations
* slower inference
* reduced focus

---

# Prompt Failures

## Prompt Injection

Malicious instructions override intended behavior.

Example:

```text
Ignore all previous instructions
```

RAG systems are particularly vulnerable.

---

## Prompt Leakage

The model reveals:

* system prompts
* hidden instructions
* internal metadata

This may expose sensitive information.

---

## Contradictory Instructions

Example:

```text
Be concise
```

vs

```text
Provide exhaustive detail
```

Conflicting prompts create unstable behavior.

---

## Oversized Prompts

Large prompts consume context inefficiently.

Consequences:

* retrieval truncation
* higher latency
* reduced reasoning quality

---

# Inference Failures

## Hallucinations

The model invents unsupported information.

Common causes:

* weak retrieval
* excessive randomness
* missing context
* ambiguous prompts

Hallucinations are one of the central AI reliability problems.

---

## Repetition Loops

The model repeats tokens or phrases.

Causes:

* poor sampling settings
* weak repetition penalties
* unstable prompts

---

## Output Instability

Same question produces inconsistent answers.

Causes:

* stochastic sampling
* prompt sensitivity
* changing retrieval

---

## Formatting Failures

Structured outputs become malformed.

Examples:

* invalid JSON
* broken markdown
* incomplete XML

Streaming generation may worsen this.

---

# Context Failures

## Lost in the Middle

Models may ignore middle sections of long contexts.

Consequences:

* critical evidence overlooked
* degraded reasoning

---

## Context Saturation

Too much information inside the prompt.

Symptoms:

* noisy responses
* slower inference
* lower answer quality

More context is not always better.

---

## Conversation Drift

Long conversations accumulate irrelevant history.

Consequences:

* degraded focus
* context pressure
* memory inefficiency

---

# Qdrant Failures

## Collection Missing

Expected collection does not exist.

---

## Corrupted Metadata

Filters behave incorrectly.

---

## Slow Similarity Search

Possible causes:

* oversized collections
* poor indexing
* hardware bottlenecks

---

## Duplicate Vectors

Repeated ingestion creates redundant entries.

Consequences:

* noisy retrieval
* inflated storage

---

# Ingestion Failures

## Parsing Errors

Documents fail during ingestion.

Examples:

* malformed PDFs
* encoding issues
* unsupported formats

---

## Silent Ingestion Failure

Documents appear indexed but are missing.

Dangerous because:

```text
The failure is invisible
```

---

## Chunk Overlap Problems

Improper overlap creates:

* fragmented context
* duplicated retrieval
* missing semantic continuity

---

# Deployment Failures

## Missing Environment Variables

Example:

```env
OLLAMA_BASE_URL
```

not configured.

---

## Port Conflicts

Services attempt to use the same port.

---

## Broken Persistence

Qdrant data disappears after restart.

---

## Wrong Model Configuration

Deployment references unavailable models.

---

# Security Failures

## Exposed APIs

Services accessible without authentication.

---

## Hardcoded Secrets

Credentials committed to repositories.

---

## Poisoned Documents

Malicious content influences retrieval.

---

## Unsafe File Uploads

Untrusted files compromise the system.

---

# Observability Failures

## Missing Retrieval Logs

Impossible to debug RAG quality.

---

## No Model Version Tracking

Results become unreproducible.

---

## Weak Error Messages

Failures become difficult to diagnose.

---

## No GPU Monitoring

Performance bottlenecks remain invisible.

---

# Scientific AI Failure Modes

Scientific systems face additional risks.

Examples:

* fabricated citations
* unsupported scientific claims
* retrieval from outdated papers
* unit inconsistencies
* incorrect equations
* misleading summaries

Scientific AI requires strong validation.

---

# Human Factors

Not all failures are technical.

Possible issues:

* unrealistic expectations
* poor evaluation
* misuse of outputs
* overtrust in generated answers
* ignoring uncertainty

AI systems require human judgment.

---

# Failure Cascades

A small problem may propagate.

Example:

```text
Bad chunking
    ↓
Weak retrieval
    ↓
Poor prompt context
    ↓
Hallucinated answer
```

Many AI failures are cascading systems failures.

---

# Debugging Strategy

A useful debugging order:

```text
1. Infrastructure
2. Retrieval
3. Prompt assembly
4. Generation
5. UI/Frontend
```

Most RAG problems originate before generation.

---

# Failure Prevention

Useful strategies:

* strong logging
* observability
* health checks
* prompt versioning
* retrieval evaluation
* metadata validation
* GPU monitoring
* automated testing

Reliable systems are engineered intentionally.

---

# Evaluation Importance

Many failures remain hidden without evaluation.

Questions to evaluate:

* Was retrieval correct?
* Was the answer grounded?
* Did hallucination occur?
* Was context sufficient?
* Was latency acceptable?

Evaluation is essential for production readiness.

---

# Minimal Reliability Checklist

A practical checklist:

```text
Monitor VRAM
Log retrieval results
Track model versions
Validate ingestion
Inspect prompts
Check context size
Use metadata filtering
Add health checks
Measure latency
Evaluate hallucinations
```

This dramatically improves reliability.

---

# Mental Models

Useful mental models:

```text
RAG failures are often retrieval failures
```

```text
More context can reduce quality
```

```text
AI systems fail probabilistically, not only deterministically
```

```text
Hallucinations are systems problems, not only model problems
```

---

# Relationship with AI Systems Engineering

Failure analysis connects:

* inference
* retrieval
* databases
* prompts
* deployment
* observability
* infrastructure
* human workflows

Understanding failure modes is essential for engineering robust AI systems.

---

# Reflection

Most AI systems work impressively during demonstrations.

The real challenge begins when systems must become:

* reliable
* reproducible
* debuggable
* maintainable
* scientifically trustworthy

Understanding common failure modes is therefore one of the most important steps in moving from:

```text
AI experimentation
```

to:

```text
Production-grade AI systems engineering
```

because robust systems are defined not only by what works, but also by how failures are detected, understood, and controlled.
