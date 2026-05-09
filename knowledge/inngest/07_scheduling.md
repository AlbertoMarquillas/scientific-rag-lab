# Scheduling

---

# What is Scheduling?

Scheduling means:

```text
execute workflows automatically at specific times or intervals
```

Instead of reacting to events:

```text
something happened
```

scheduled workflows react to:

```text
time
```

Examples:

```text
Every hour
Every day
Every Monday
Every month
```

Scheduling is fundamental in production systems.

---

# Why Scheduling Exists

Many workflows must run periodically.

Examples:

* cleanup jobs
* evaluation pipelines
* index refreshes
* monitoring checks
* ingestion scans
* backups
* analytics generation

These workflows are triggered by time rather than external events.

---

# Event-Driven vs Scheduled Workflows

---

# Event-Driven

Triggered because:

```text
something happened
```

Example:

```text
paper.uploaded
```

---

# Scheduled

Triggered because:

```text
a specific time arrived
```

Example:

```text
Every hour
→ scan for new papers
```

Both models are important.

---

# Typical Scheduled Tasks

Examples:

```text
Every night
→ rebuild evaluation dataset
```

```text
Every hour
→ check experiment folders
```

```text
Every week
→ compute retrieval metrics
```

```text
Every day
→ clean temporary files
```

Scheduling enables automation.

---

# Why Scheduling Matters in AI Systems

AI systems often require recurring maintenance.

Examples:

* retraining evaluation
* embedding refresh
* monitoring
* index updates
* cache cleanup
* analytics generation

Scheduling becomes essential for production infrastructure.

---

# Cron Mental Model

Traditional scheduling often uses:

```text
cron jobs
```

Conceptually:

```text
run task at specific times
```

Inngest provides workflow-oriented scheduling integrated with:

* retries
* observability
* durability
* orchestration

---

# Why Simple Cron Jobs Become Limited

Simple cron systems often lack:

* retries
* workflow state
* tracing
* orchestration
* step-level visibility
* durable execution

Modern AI systems often require more advanced workflow behavior.

---

# Scheduled Workflow Example

Example:

```text
Every night at midnight
      ↓
scan experiment folders
      ↓
find new runs
      ↓
run ingestion workflows
      ↓
update vector DB
```

This is a typical AI automation workflow.

---

# Scheduling and Automation

Scheduling transforms systems into:

```text
self-operating infrastructure
```

The system continuously maintains itself.

This is critical in production AI systems.

---

# Periodic Maintenance Workflows

Common maintenance workflows:

* cleanup
* evaluation
* backups
* synchronization
* monitoring
* health checks
* metric aggregation

These are usually scheduled.

---

# Scheduled Ingestion

Example:

```text
Every hour
→ scan uploads folder
→ process new PDFs
→ generate embeddings
→ update index
```

This creates continuous ingestion pipelines.

---

# Scheduled Evaluation

Example:

```text
Every night
→ evaluate retrieval quality
→ compute hallucination metrics
→ generate reports
```

Evaluation is often periodic.

---

# Scheduled Monitoring

Example:

```text
Every 10 minutes
→ check vector DB health
→ measure latency
→ inspect failed workflows
```

Monitoring workflows are common in production systems.

---

# Scheduling and Durability

Scheduled workflows benefit from:

* retries
* observability
* recovery
* workflow history
* step orchestration

These are major advantages over simple cron execution.

---

# Scheduling Reliability

Suppose a scheduled workflow fails.

Example:

```text
nightly indexing workflow
→ embedding API outage
```

Workflow orchestration allows:

* retries
* recovery
* visibility
* partial progress persistence

Reliable scheduling is more than:

```text
run command
```

---

# Time-Based Automation

Scheduling enables:

```text
time-driven orchestration
```

This complements:

```text
event-driven orchestration
```

Modern systems usually use both.

---

# Scheduling Granularity

Schedules may vary in frequency.

Examples:

```text
Every minute
Every hour
Every day
Every week
```

Granularity depends on:

* workload
* latency needs
* cost
* system requirements

---

# High-Frequency Scheduling

Very frequent schedules may create:

* infrastructure load
* API pressure
* overlapping workflows
* higher costs

Concurrency control becomes important.

---

# Workflow Overlap

Suppose:

```text
workflow duration = 20 minutes
schedule interval = 10 minutes
```

Now workflows overlap.

This may create:

* duplicated work
* race conditions
* resource exhaustion

Scheduling systems must consider overlap.

---

# Concurrency and Scheduling

Scheduling often interacts with concurrency limits.

Examples:

```text
only one indexing workflow at a time
```

```text
max 3 embedding workflows concurrently
```

Concurrency protects infrastructure stability.

---

# Idempotency in Scheduled Workflows

Scheduled workflows should usually be idempotent.

Reason:

* retries may happen
* workflows may overlap
* workflows may rerun

Example:

```text
rebuilding embeddings twice
```

should not corrupt state.

---

# Scheduling and Backfills

Sometimes systems need:

```text
backfills
```

Meaning:

```text
re-run historical scheduled tasks
```

Examples:

* recompute old embeddings
* rebuild indexes
* rerun evaluations

Backfills are common in production systems.

---

# Scheduling and AI Costs

Scheduled AI workflows may become expensive.

Examples:

* repeated embedding generation
* large evaluation pipelines
* multimodal processing
* expensive LLM inference

Scheduling should consider:

* compute usage
* API costs
* infrastructure limits

---

# Scheduling and Observability

Scheduled workflows should be observable.

Important visibility:

* execution time
* failures
* retries
* skipped runs
* overlapping runs
* latency

Without observability, automation becomes dangerous.

---

# Scheduled Failures

Example:

```text
nightly evaluation workflow failed
```

Good workflow systems provide:

* alerts
* logs
* traces
* retry visibility
* failure history

Automation must remain inspectable.

---

# Scheduling in AI Pipelines

Common AI scheduling examples:

```text
Every hour
→ ingest new documents
```

```text
Every day
→ evaluate retrieval quality
```

```text
Every week
→ rebuild ranking datasets
```

Production AI systems rely heavily on scheduling.

---

# Scheduling in RAG Systems

Typical scheduled RAG tasks:

* refresh indexes
* scan new data
* rerun evaluations
* clean caches
* regenerate summaries
* recompute embeddings

RAG infrastructure often becomes highly automated.

---

# Scheduling in Agentic Systems

Agentic systems may schedule:

* periodic reasoning
* monitoring workflows
* maintenance tasks
* report generation
* autonomous evaluations

Scheduling becomes part of autonomous system behavior.

---

# Scheduling in This Project

Potential scheduled workflows:

```text
Every hour
→ scan experiment folders
```

```text
Every night
→ generate retrieval summaries
```

```text
Every week
→ evaluate scientific retrieval quality
```

```text
Every day
→ recompute experiment similarity metrics
```

---

# Scientific Workflow Scheduling

Scientific systems often require recurring workflows.

Examples:

* automated analysis
* periodic comparisons
* metric aggregation
* report generation
* dataset synchronization

Scheduling enables continuous scientific infrastructure.

---

# Scheduling vs Manual Execution

Manual workflows:

* error-prone
* inconsistent
* difficult to scale

Scheduling enables:

* consistency
* automation
* reproducibility
* continuous operation

This is important for production systems.

---

# Common Mistakes

## Overlapping Workflows

Creates duplicated execution.

---

## No Concurrency Limits

Infrastructure overload.

---

## No Observability

Failed automation becomes invisible.

---

## Non-Idempotent Workflows

Retries corrupt state.

---

## Excessive Scheduling Frequency

Creates unnecessary costs.

---

# Recommended Scheduling Design

Good scheduled workflows are usually:

* observable
* retry-safe
* idempotent
* concurrency-aware
* resource-aware
* durable

Useful philosophy:

```text
automation should be reliable and inspectable
```

---

# Important Insight

Scheduling transforms systems from:

```text
manually operated workflows
```

into:

```text
continuous autonomous infrastructure
```

This is a core capability of modern AI systems engineering.

---

# Key Insight

Modern AI systems increasingly require:

```text
continuous automated workflows
```

for:

* ingestion
* evaluation
* monitoring
* indexing
* synchronization
* maintenance

Scheduling is one of the foundational mechanisms enabling production-grade AI infrastructure.