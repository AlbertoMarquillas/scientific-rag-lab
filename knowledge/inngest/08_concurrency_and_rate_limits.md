# Concurrency and Rate Limits

---

# Why Concurrency Matters

Modern systems often execute many workflows simultaneously.

Examples:

* multiple users uploading files
* many experiments arriving at once
* concurrent embedding generation
* parallel evaluation pipelines
* multiple AI requests

Without control:

```text
system overload
```

may occur.

Concurrency management is essential for reliable infrastructure.

---

# What is Concurrency?

Concurrency means:

```text
multiple tasks executing at the same time
```

Example:

```text
Workflow A running
Workflow B running
Workflow C running
```

Modern distributed systems are highly concurrent.

---

# Why Unlimited Concurrency is Dangerous

Suppose:

```text
1000 workflows start simultaneously
```

Potential consequences:

* API rate limits exceeded
* database overload
* memory exhaustion
* GPU saturation
* queue congestion
* system instability

Reliable systems control concurrency carefully.

---

# Concurrency Control

Concurrency control means:

```text
limit how much work runs simultaneously
```

Examples:

```text
max 5 embedding workflows
```

```text
only one workflow per experiment
```

This protects infrastructure.

---

# What is a Rate Limit?

A rate limit restricts:

```text
how frequently operations may occur
```

Example:

```text
max 100 API requests per minute
```

Rate limiting protects systems from overload.

---

# Concurrency vs Rate Limits

Important distinction.

---

# Concurrency

Controls:

```text
how many tasks run simultaneously
```

Example:

```text
5 embedding jobs at once
```

---

# Rate Limits

Controls:

```text
how many operations happen over time
```

Example:

```text
100 requests per minute
```

Both mechanisms are important.

---

# Why AI Systems Need Concurrency Control

AI systems often depend on:

* expensive APIs
* GPUs
* vector databases
* embedding providers
* LLM inference

These resources are limited and expensive.

Uncontrolled concurrency can become catastrophic.

---

# Example AI Failure

Suppose:

```text
1000 PDFs uploaded simultaneously
```

Each triggers:

* parsing
* chunking
* embedding generation

Without concurrency control:

```text
1000 embedding requests simultaneously
```

Possible consequences:

* API bans
* rate limits
* huge costs
* infrastructure crashes

---

# Embedding Concurrency Example

Safe configuration:

```text
max 5 embedding workflows
```

This creates:

* controlled throughput
* predictable cost
* infrastructure stability

Controlled systems are more reliable.

---

# Why Throughput Matters

Concurrency creates a tradeoff:

```text
higher throughput
vs
system stability
```

Too little concurrency:

* slow system

Too much concurrency:

* unstable system

Good systems balance both.

---

# Workflow Queues

When concurrency limits are reached:

```text
additional workflows wait
```

This creates queues.

Conceptually:

```text
incoming workflows
      ↓
queue
      ↓
controlled execution
```

Queues stabilize infrastructure.

---

# Why Queues Matter

Queues help absorb bursts of activity.

Example:

```text
sudden upload spike
```

Instead of crashing:

```text
work accumulates safely
```

This is a core distributed systems pattern.

---

# Backpressure

Important concept:

```text
backpressure
```

Meaning:

systems slow incoming work when downstream systems are overloaded.

Without backpressure:

```text
uncontrolled overload propagation
```

may occur.

---

# Resource Bottlenecks

Concurrency limits often protect bottlenecks.

Examples:

* embedding API
* GPU inference
* vector DB writes
* file I/O
* database queries

Workflow systems manage access to these bottlenecks.

---

# API Rate Limits

External APIs often enforce limits.

Examples:

```text
requests per minute
requests per second
tokens per minute
```

AI providers frequently impose strict limits.

---

# Why Rate Limits Exist

Rate limits protect:

* infrastructure stability
* fair resource sharing
* provider reliability
* abuse prevention

Production systems must respect them.

---

# Example OpenAI Constraint

Suppose:

```text
embedding API limit = 300 requests/minute
```

Without rate limiting:

```text
too many requests
→ errors
→ retries
→ cascading failures
```

Concurrency and rate control prevent this.

---

# Cascading Failures

Dangerous distributed systems pattern:

```text
overload
→ retries
→ more overload
→ more failures
→ system collapse
```

Concurrency limits help prevent cascading failure.

---

# Retry Storms

Retries themselves can become dangerous.

Suppose many workflows fail simultaneously.

If all retry immediately:

```text
retry storm
```

may occur.

Systems use:

* backoff
* queues
* concurrency limits

for protection.

---

# Exponential Backoff

Common retry strategy:

```text
wait longer after each retry
```

Example:

```text
Retry 1 → wait 1s
Retry 2 → wait 2s
Retry 3 → wait 4s
```

Backoff reduces overload.

---

# Per-Entity Concurrency

Some workflows should serialize execution per entity.

Example:

```text
only one workflow per experiment
```

This prevents:

* duplicated indexing
* race conditions
* conflicting updates

Entity-level concurrency is common.

---

# Race Conditions

A race condition occurs when:

```text
multiple workflows modify the same state simultaneously
```

Example:

```text
two workflows updating same experiment metadata
```

This may corrupt state.

Concurrency control helps prevent this.

---

# Distributed Locks

Some systems use:

```text
distributed locks
```

Meaning:

```text
only one workflow may access resource at a time
```

Useful for:

* shared resources
* database consistency
* critical updates

---

# Concurrency and Cost

AI systems are expensive.

High concurrency may create:

* massive API costs
* GPU overload
* large cloud bills

Concurrency control is also:

```text
cost control
```

---

# Throughput vs Cost

Important tradeoff:

```text
faster processing
vs
lower infrastructure cost
```

Higher concurrency usually increases:

* speed
* infrastructure pressure
* spending

Production systems optimize this balance.

---

# Concurrency and Observability

Systems should monitor:

* queue sizes
* active workflows
* failed workflows
* retry rates
* API usage
* rate limit errors

Without observability, overload becomes invisible.

---

# Queue Monitoring

Example warning signs:

```text
queue growing continuously
```

This may indicate:

* insufficient workers
* bottlenecks
* downstream failures
* overload

Queue observability is important.

---

# Concurrency in AI Pipelines

Typical AI bottlenecks:

* embeddings
* LLM inference
* reranking
* image processing
* multimodal analysis

Workflow orchestration systems protect these resources.

---

# Concurrency in RAG Systems

Examples:

```text
max 5 ingestion workflows
```

```text
max 10 embedding requests
```

```text
max 2 reranking pipelines
```

RAG systems often require careful resource orchestration.

---

# Concurrency in Agentic Systems

Agent systems may generate:

* recursive workflows
* tool calls
* retrieval chains
* verification pipelines

Without limits:

```text
explosive workflow growth
```

may occur.

Concurrency management becomes critical.

---

# Concurrency in This Project

Potential constraints:

```text
only one analysis workflow per run
```

```text
max 3 embedding workflows
```

```text
limit Qdrant indexing concurrency
```

Potential bottlenecks:

* HDF5 reading
* optical analysis
* embedding generation
* plot generation
* vector indexing

---

# Scientific Infrastructure

Scientific systems often contain:

* expensive computations
* long analyses
* shared datasets
* heavy I/O

Concurrency control improves:

* reproducibility
* stability
* resource management

---

# Common Mistakes

## Unlimited Concurrency

Infrastructure overload.

---

## Ignoring Rate Limits

APIs start rejecting requests.

---

## No Backoff

Retries amplify failures.

---

## No Queue Monitoring

System overload becomes invisible.

---

## Weak Entity Isolation

Race conditions corrupt state.

---

# Recommended Concurrency Philosophy

Good systems are:

* resource-aware
* queue-aware
* retry-aware
* cost-aware
* bottleneck-aware
* observable

Useful mindset:

```text
controlled throughput is better than uncontrolled speed
```

---

# Important Insight

Concurrency is not only:

```text
running many things simultaneously
```

It is:

```text
managing shared resources safely
```

This is fundamental in distributed systems engineering.

---

# Key Insight

Modern AI systems require careful control over:

* concurrency
* retries
* queues
* rate limits
* resource usage

because AI infrastructure is often:

```text
expensive
+
distributed
+
failure-prone
```

Reliable workflow orchestration depends heavily on these controls.
