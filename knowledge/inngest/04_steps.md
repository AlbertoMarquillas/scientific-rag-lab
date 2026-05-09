# Steps

---

# What is a Step?

A step is a smaller execution unit inside a workflow function.

Conceptually:

```text
Function
   ↓
Step 1
Step 2
Step 3
```

Steps divide workflows into manageable, durable, retryable units.

---

# Core Idea

Instead of executing an entire workflow as one block:

```text
one giant execution
```

Inngest workflows are split into:

```text
independent steps
```

This is one of the most important ideas in durable workflow systems.

---

# Why Steps Exist

Distributed systems fail constantly.

Examples:

* API timeout
* network issue
* database unavailable
* embedding provider failure
* vector DB outage
* server restart

Without steps:

```text
restart entire workflow
```

With steps:

```text
retry only failed step
```

---

# Example Workflow Without Steps

Suppose a workflow:

```text
1. Parse PDF
2. Generate embeddings
3. Store vectors
4. Update metadata
```

If step 4 fails:

```text
restart everything
```

This wastes time and resources.

---

# Example Workflow With Steps

Now split into steps:

```text
Step 1 → Parse PDF
Step 2 → Generate embeddings
Step 3 → Store vectors
Step 4 → Update metadata
```

If Step 4 fails:

```text
retry only Step 4
```

Earlier steps remain completed.

---

# Durable Execution

Steps enable:

```text
durable execution
```

Meaning:

* progress persists
* completed steps remain completed
* failures do not restart entire workflows
* execution can resume safely

This is critical for long-running pipelines.

---

# Step Persistence

Workflow systems track:

* completed steps
* failed steps
* retries
* outputs
* execution state

This persistence allows reliable recovery.

---

# Step Isolation

Each step should ideally represent:

```text
one coherent unit of work
```

Examples:

```text
extract_metadata
chunk_document
generate_embeddings
store_vectors
```

This improves:

* readability
* observability
* retries
* maintainability

---

# Step Boundaries

Good workflow design often depends on choosing good step boundaries.

Bad boundary:

```text
one giant ingestion step
```

Better boundary:

```text
parse
chunk
embed
store
```

Smaller logical steps improve orchestration.

---

# Step Retry Behavior

Each step can retry independently.

Example:

```text
Step 1 → success
Step 2 → success
Step 3 → API timeout
```

Only Step 3 retries.

This is one of the major advantages of workflow systems.

---

# Retry Philosophy

Workflow systems assume:

```text
failures are normal
```

Retries are expected behavior.

Distributed systems must tolerate:

* transient failures
* temporary outages
* rate limits
* unstable connections

Reliable systems are designed around retries.

---

# Step Idempotency

Important concept:

```text
idempotency
```

A step should ideally be safe to run multiple times.

Example:

```text
storing vectors twice
```

should not corrupt the system.

Without idempotency:

* duplicated embeddings
* duplicated rows
* duplicated notifications

may occur.

---

# Why Idempotency Matters

Steps may rerun because of:

* retries
* crashes
* workflow replay
* infrastructure failures

Reliable workflows assume duplicate execution is possible.

---

# Step Inputs and Outputs

Steps usually:

* receive data
* process data
* return outputs

Example:

```text
Step 1 → extract text
Output → parsed text

Step 2 → chunk text
Input → parsed text
Output → chunks
```

Steps form execution chains.

---

# Step Dependencies

Some steps depend on previous outputs.

Example:

```text
chunk_document
```

requires:

```text
parsed_text
```

Workflow systems coordinate these dependencies.

---

# Sequential Steps

Many workflows are sequential.

Example:

```text
parse PDF
      ↓
chunk document
      ↓
embed chunks
      ↓
store vectors
```

Each step depends on earlier steps.

---

# Parallel Steps

Some steps can execute independently.

Example:

```text
extract metadata
extract figures
extract references
```

These may run in parallel.

Parallel execution improves scalability.

---

# Long-Running Steps

Some steps may take:

* minutes
* hours
* large API calls
* heavy scientific computation

Durable workflows become especially important in these situations.

---

# Step Observability

One major advantage:

```text
step-level observability
```

You can inspect:

* execution time
* retries
* failures
* inputs
* outputs
* execution history

This dramatically improves debugging.

---

# Example Debugging Scenario

Without step observability:

```text
workflow failed
```

With step observability:

```text
Step: generate_embeddings
Error: rate limit exceeded
Retry count: 3
Duration: 12s
```

This is much easier to debug.

---

# Step Timeouts

Some steps may timeout.

Examples:

* slow API
* stalled computation
* overloaded service

Workflow systems often manage:

* timeout handling
* retries
* cancellation

---

# Step Concurrency

Some steps may require concurrency limits.

Examples:

```text
max 5 embedding steps
```

```text
one analysis step per experiment
```

Concurrency management prevents overload.

---

# Step Granularity

Important design tradeoff:

```text
too large
vs
too small
```

---

## Steps Too Large

Problems:

* difficult retries
* weak observability
* hard debugging
* expensive reruns

---

## Steps Too Small

Problems:

* excessive orchestration complexity
* harder reasoning
* unnecessary overhead

Good workflows choose reasonable granularity.

---

# Step Naming

Step names should be:

* descriptive
* focused
* action-oriented

Examples:

```text
extract_metadata
generate_embeddings
store_vectors
compute_statistics
```

Good naming improves readability.

---

# Steps and AI Pipelines

Modern AI pipelines naturally decompose into steps.

Example:

```text
upload paper
      ↓
extract text
      ↓
chunk sections
      ↓
embed chunks
      ↓
store vectors
      ↓
run evaluation
```

Each stage is a natural workflow step.

---

# Steps in RAG Systems

Typical RAG ingestion pipeline:

```text
parse document
      ↓
clean text
      ↓
chunk text
      ↓
generate embeddings
      ↓
store vectors
```

These are ideal step boundaries.

---

# Steps in Agentic Systems

Agent workflows may contain:

```text
retrieve documents
      ↓
analyze evidence
      ↓
generate summary
      ↓
verify claims
      ↓
produce answer
```

Agentic systems are naturally step-oriented.

---

# Steps in This Project

Potential workflow:

```text
experiment.detected
      ↓
Step 1 → extract metadata
Step 2 → run optical analysis
Step 3 → generate summaries
Step 4 → generate embeddings
Step 5 → store vectors
Step 6 → update retrieval index
```

Each stage becomes independently observable and retryable.

---

# Scientific Workflow Example

```text
analysis.completed
      ↓
extract turbulence metrics
      ↓
generate scientific summary
      ↓
compute retrieval metadata
      ↓
embed summary
```

Scientific pipelines naturally decompose into steps.

---

# Steps vs Functions

Functions are:

```text
workflow containers
```

Steps are:

```text
execution units inside workflows
```

Conceptually:

```text
Event
   ↓
Function
   ↓
Steps
```

---

# Steps vs Traditional Functions

Traditional code often executes linearly.

Workflow steps add:

* durability
* retries
* persistence
* observability
* orchestration

This is a different execution model.

---

# Common Mistakes

## Giant Steps

Difficult retries and debugging.

---

## No Idempotency

Retries corrupt system state.

---

## Weak Naming

Workflow logic becomes confusing.

---

## Too Many Tiny Steps

Creates orchestration overhead.

---

## Hidden Dependencies

Steps relying implicitly on unrelated state.

---

# Recommended Step Design

Good steps are usually:

* focused
* observable
* retry-safe
* idempotent
* logically coherent
* independently meaningful

Useful philosophy:

```text
one step = one meaningful unit of work
```

---

# Important Insight

Steps transform workflows from:

```text
fragile linear execution
```

into:

```text
durable recoverable orchestration
```

This is one of the core ideas behind modern workflow systems.

---

# Key Insight

Steps are the mechanism that enables:

* retries
* durability
* observability
* recovery
* reliable orchestration

inside distributed AI workflows and event-driven systems.
