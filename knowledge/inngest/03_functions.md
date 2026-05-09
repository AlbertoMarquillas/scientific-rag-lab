# Functions

---

# What is an Inngest Function?

An Inngest function defines:

```text
what should happen when an event occurs
```

Functions are the execution units of workflows.

Conceptually:

```text
Event
   ↓
Function
   ↓
Workflow Execution
```

A function reacts to events.

---

# Core Idea

Events represent:

```text
something happened
```

Functions define:

```text
how the system responds
```

Example:

```text
paper.uploaded
      ↓
parse_paper_function
```

---

# Functions as Workflow Definitions

A function is not just a simple callback.

It defines:

* workflow logic
* execution steps
* retries
* concurrency rules
* scheduling behavior
* observability boundaries

Functions are durable workflow units.

---

# Basic Mental Model

A useful mental model:

```text
functions = workflow containers
```

Inside a function:

* steps execute
* retries occur
* state is tracked
* failures are managed

---

# Triggering Functions

Functions are usually triggered by:

* events
* schedules

Example:

```text
experiment.finished
→ run analysis function
```

or:

```text
Every day
→ run cleanup function
```

---

# Event-Triggered Functions

Most functions react to events.

Example:

```text
experiment.detected
      ↓
run_ingestion_function
```

This creates reactive systems.

---

# Scheduled Functions

Functions may also run periodically.

Examples:

```text
Every hour
→ check new experiment folders
```

```text
Every night
→ rebuild evaluation dataset
```

This replaces many cron-based systems.

---

# Function Structure

Conceptually, a function contains:

```text
trigger
+
workflow logic
+
steps
```

Typical workflow:

```text
receive event
      ↓
execute steps
      ↓
retry failures if necessary
      ↓
complete workflow
```

---

# Example Workflow Function

Example:

```text
paper.uploaded
      ↓
extract metadata
      ↓
chunk document
      ↓
generate embeddings
      ↓
store vectors
```

All of this may belong to one function.

---

# Functions and Steps

Functions are divided into:

```text
steps
```

Steps are important because they:

* isolate work
* enable retries
* improve observability
* support durable execution

Functions orchestrate steps.

---

# Why Steps Matter

Suppose a workflow contains:

```text
Step 1 → success
Step 2 → success
Step 3 → API failure
```

Without step-based execution:

```text
restart entire workflow
```

With steps:

```text
retry only Step 3
```

This improves reliability significantly.

---

# Durable Execution

Functions are durable.

Meaning:

* execution state persists
* failures are recoverable
* retries are safe
* workflows can resume

This is critical for long-running pipelines.

---

# Function State

Workflow state can exist across steps.

Example:

```text
Step 1 → retrieve metadata
Step 2 → use metadata
Step 3 → generate summaries
```

Functions coordinate workflow progression.

---

# Retries

Functions support retries automatically.

Failures are expected in distributed systems.

Examples:

* network failure
* API timeout
* database unavailable
* rate limit exceeded

Reliable workflows must tolerate these conditions.

---

# Retry Philosophy

Important mindset:

```text
failures are normal
```

Modern distributed systems are designed around retries.

Workflow systems like Inngest assume:

* APIs fail
* services timeout
* connections break
* workloads restart

Reliability comes from orchestration.

---

# Function Isolation

Functions should ideally represent:

```text
coherent workflow responsibilities
```

Example:

```text
paper ingestion function
```

instead of:

```text
one giant system-wide function
```

Smaller focused workflows are easier to maintain.

---

# Single Responsibility Principle

Good workflow design often follows:

```text
one function = one workflow responsibility
```

Examples:

* paper ingestion
* experiment analysis
* embedding generation
* evaluation pipeline

This improves modularity.

---

# Function Chaining

Functions may emit additional events.

Example:

```text
paper.uploaded
      ↓
parse_paper_function
      ↓
emit paper.parsed
      ↓
embedding_function
```

This creates modular event-driven pipelines.

---

# Why Function Chaining is Powerful

It enables:

* decoupling
* modularity
* independent scaling
* independent retries
* cleaner workflows

Large systems often become chains of smaller workflows.

---

# Function Concurrency

Production systems often limit concurrency.

Examples:

```text
max 5 embedding workflows
```

```text
only one analysis workflow per experiment
```

Functions can define concurrency rules.

---

# Function Idempotency

Functions should ideally be idempotent.

Meaning:

```text
re-running the same workflow
should not corrupt the system
```

Examples of bad non-idempotent behavior:

* duplicated embeddings
* duplicate DB rows
* repeated notifications

Reliable workflows must tolerate retries.

---

# Function Observability

Functions are observable.

You can inspect:

* execution history
* retries
* failures
* timing
* step progression
* input payloads
* outputs

This is one of the strongest advantages of workflow systems.

---

# Function Execution Timeline

Conceptually:

```text
Event Received
      ↓
Workflow Started
      ↓
Step 1
      ↓
Step 2
      ↓
Retry Step 3
      ↓
Workflow Completed
```

This timeline is useful for debugging.

---

# Long-Running Functions

Some workflows may run for:

* minutes
* hours
* days

Examples:

* large ingestion pipelines
* scientific analysis
* evaluation workflows
* multi-agent pipelines

Durable execution becomes critical.

---

# Functions and AI Systems

Modern AI systems naturally contain workflow functions.

Examples:

```text
new_document
→ ingestion function
```

```text
embedding.failed
→ retry workflow
```

```text
evaluation.completed
→ reporting workflow
```

AI infrastructure is heavily workflow-oriented.

---

# Example AI Workflow Function

Example:

```text
paper.uploaded
      ↓
extract text
      ↓
chunk sections
      ↓
generate embeddings
      ↓
store vectors
      ↓
emit indexing.completed
```

This is a typical AI ingestion function.

---

# Functions in This Project

Potential functions:

```text
experiment_ingestion_function
analysis_function
comparison_function
embedding_function
plot_generation_function
scientific_summary_function
```

Possible workflow:

```text
experiment.detected
      ↓
extract metadata
      ↓
run turbulence analysis
      ↓
generate scientific summary
      ↓
store retrieval artifacts
```

---

# Scientific Workflow Example

```text
analysis.completed
      ↓
extract turbulence metrics
      ↓
compute summaries
      ↓
generate embeddings
      ↓
update vector index
```

This becomes a scientific AI pipeline.

---

# Functions vs APIs

An API endpoint usually focuses on:

```text
short request-response interaction
```

A workflow function focuses on:

```text
durable asynchronous orchestration
```

These are different architectural roles.

---

# Functions vs Background Jobs

Simple background jobs often:

* run independently
* lack orchestration
* lack tracing
* lack durable state

Workflow functions add:

* orchestration
* retries
* observability
* durable execution
* step management

---

# Functions and Microservices

Event-driven functions work well with microservice architectures.

Services communicate through:

```text
events
```

rather than direct coupling.

This improves scalability and modularity.

---

# Common Mistakes

## Giant Workflow Functions

Functions become difficult to maintain.

---

## No Idempotency

Retries create duplicated operations.

---

## Too Many Responsibilities

One workflow doing unrelated tasks.

---

## No Observability

Failures become difficult to debug.

---

## Tight Coupling

Functions depending heavily on internal implementation details.

---

# Recommended Function Design

Good functions are usually:

* focused
* modular
* idempotent
* observable
* retry-safe
* event-driven

Useful philosophy:

```text
small workflows composed together
```

rather than one giant orchestration.

---

# Important Insight

Functions are the execution layer of event-driven systems.

Events describe:

```text
what happened
```

Functions define:

```text
how the system reacts
```

This separation is fundamental.

---

# Key Insight

Inngest functions are not merely:

```text
callbacks
```

They are:

```text
durable workflow orchestrators
```

designed for modern asynchronous distributed systems and AI pipelines.
