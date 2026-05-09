# What is Inngest?

---

# Definition

Inngest is a platform for building:

* event-driven systems
* background jobs
* durable workflows
* scheduled tasks
* asynchronous pipelines
* AI orchestration systems

It provides infrastructure for executing workflows reliably.

Core idea:

```text
send events
→ trigger functions
→ execute reliable workflows
```

---

# The Main Problem Inngest Solves

Modern applications increasingly require:

* asynchronous execution
* retries
* long-running jobs
* orchestration
* scheduling
* observability
* distributed workflows

These workflows become difficult to manage manually.

Example:

```text
new document uploaded
      ↓
parse PDF
      ↓
chunk text
      ↓
generate embeddings
      ↓
store vectors
      ↓
run evaluation
      ↓
notify completion
```

A normal request-response backend is not ideal for this.

---

# Traditional Backend Model

A simple backend often looks like:

```text
Request
   ↓
Backend
   ↓
Response
```

This works well for:

* simple APIs
* CRUD operations
* short synchronous tasks

But complex workflows create problems.

---

# Why Traditional APIs Become Difficult

Suppose an API endpoint must:

* call multiple services
* process large files
* wait for external APIs
* retry failures
* update databases
* trigger downstream tasks

Now the system contains:

* background jobs
* async logic
* failure handling
* orchestration complexity

The architecture becomes harder to maintain.

---

# Event-Driven Thinking

Inngest is built around:

```text
events
```

An event means:

```text
something happened
```

Examples:

```text
user.created
paper.uploaded
experiment.finished
analysis.completed
```

Events trigger workflows.

---

# Example Event Workflow

Example:

```text
experiment.finished
      ↓
extract metadata
      ↓
run analysis
      ↓
generate summaries
      ↓
create embeddings
      ↓
update vector DB
```

Each stage becomes part of a workflow.

---

# Inngest as Workflow Infrastructure

Inngest provides infrastructure for:

* receiving events
* triggering functions
* managing execution
* retrying failures
* tracing workflows
* scheduling jobs
* controlling concurrency

Instead of building this infrastructure manually.

---

# Important Concept: Durable Execution

One of the central concepts:

```text
durable workflows
```

Meaning:

* workflows persist state
* steps can resume after failures
* retries happen safely
* execution history is preserved

This is extremely important in distributed systems.

---

# Why Durable Workflows Matter

Suppose a workflow contains:

```text
Step 1 → success
Step 2 → success
Step 3 → API failure
```

Without durability:

```text
restart everything
```

With durable execution:

```text
resume from Step 3
```

This improves:

* reliability
* efficiency
* fault tolerance

---

# Inngest Functions

Functions define what should happen after an event.

Conceptually:

```text
Event
   ↓
Function
   ↓
Workflow
```

A function contains workflow logic.

---

# Steps

Functions are divided into steps.

Each step:

* can retry independently
* can be traced independently
* can persist independently

Example:

```text
Step 1 → parse file
Step 2 → generate embeddings
Step 3 → store vectors
```

This step-based model is one of the major design ideas.

---

# Retries

Distributed systems fail constantly.

Examples:

* API timeout
* network issue
* database unavailable
* rate limit exceeded

Inngest includes automatic retry handling.

This avoids writing large amounts of retry infrastructure manually.

---

# Observability

Inngest includes built-in workflow observability.

You can inspect:

* events
* workflow runs
* step execution
* retries
* errors
* execution duration
* workflow history

This is extremely useful for debugging.

---

# Why Observability Matters

Suppose an embedding pipeline fails.

Without observability:

```text
something broke
```

With observability:

```text
Step: generate_embeddings
Error: OpenAI timeout
Retry count: 2
Execution duration: 14s
```

This dramatically improves debugging.

---

# Scheduling

Inngest also supports scheduled workflows.

Examples:

```text
Every day
→ rebuild evaluation datasets
```

```text
Every hour
→ scan new experiment folders
```

This replaces many manual cron systems.

---

# Concurrency Control

Production systems often need concurrency limits.

Examples:

* max 5 embedding jobs
* only one workflow per experiment
* limit expensive API calls

Inngest supports concurrency management.

---

# Why Inngest is Popular in AI

Modern AI systems naturally contain:

* ingestion pipelines
* embedding generation
* vector indexing
* evaluation workflows
* retries
* long-running tasks
* agentic workflows
* asynchronous processing

These map naturally to event-driven orchestration.

---

# AI Workflow Example

Example:

```text
paper.uploaded
      ↓
parse PDF
      ↓
chunk document
      ↓
generate embeddings
      ↓
store in Qdrant
      ↓
run evaluation
```

This is a typical AI pipeline.

---

# Agentic Workflow Example

Example:

```text
user asks question
      ↓
retrieve experiments
      ↓
retrieve papers
      ↓
compare metrics
      ↓
generate report
      ↓
verify evidence
```

As systems become more agentic, orchestration becomes more important.

---

# Inngest vs Cron Jobs

Cron jobs are useful for simple scheduling.

But they usually lack:

* durable execution
* workflow state
* retries
* tracing
* observability
* orchestration

Inngest provides a more complete workflow model.

---

# Inngest vs Celery

Celery is mainly a task queue.

Inngest provides:

* workflows
* events
* step execution
* retries
* scheduling
* tracing
* observability

with a more integrated developer experience.

---

# Inngest vs Airflow

Airflow is commonly used for:

* ETL pipelines
* batch workflows
* DAG orchestration

Inngest is often more focused on:

* application workflows
* event-driven systems
* backend orchestration
* AI pipelines

---

# Inngest vs Temporal

Temporal is another durable workflow system.

Temporal is often considered:

* very powerful
* highly scalable
* infrastructure-heavy

Inngest aims for a simpler developer experience.

---

# Typical Architecture

Conceptual architecture:

```text
Application
      ↓
Send Event
      ↓
Inngest
      ↓
Trigger Function
      ↓
Execute Workflow Steps
      ↓
Retries / Logging / Tracing
      ↓
Completion
```

---

# Inngest in This Project

Potential workflows:

```text
new_run_detected
      ↓
extract metadata
      ↓
run turbulence analysis
      ↓
generate summaries
      ↓
embed summaries
      ↓
store vectors
```

Another example:

```text
paper.added
      ↓
parse PDF
      ↓
chunk sections
      ↓
embed chunks
      ↓
update retrieval index
```

---

# Why It Fits Scientific Systems

Scientific systems often involve:

* asynchronous processing
* long-running analyses
* derived outputs
* multiple dependent stages
* expensive computations
* reproducibility needs

This naturally creates workflows.

---

# Important Architectural Shift

Inngest encourages a different way of thinking.

Instead of:

```text
call function directly
```

systems become:

```text
emit event
→ trigger workflow
→ orchestrate steps
```

This decouples components.

---

# Decoupling

Event-driven systems are often more decoupled.

Example:

```text
experiment.finished
```

can trigger:

* analysis workflow
* indexing workflow
* notification workflow
* evaluation workflow

without the producer needing to know all consumers.

---

# Reliability Philosophy

A major philosophy behind workflow systems:

```text
failures are normal
```

Distributed systems must expect:

* retries
* partial failures
* API outages
* timeouts
* network instability

Reliable orchestration systems are designed around this reality.

---

# Recommended Learning Order

Best progression:

```text
1. Events
2. Functions
3. Steps
4. Retries
5. Scheduling
6. Concurrency
7. Observability
8. AI workflows
```

Understanding events and steps is the foundation.

---

# Important Insight

Inngest is not:

* an AI model
* a vector DB
* an LLM framework
* a retrieval system

It is:

```text
workflow orchestration infrastructure
```

for modern asynchronous systems.

---

# Key Insight

As AI systems become:

```text
larger
more asynchronous
more agentic
more distributed
```

workflow orchestration becomes increasingly important.

Inngest provides a modern developer-oriented approach for building these systems reliably.
