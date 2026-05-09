# Events

---

# What is an Event?

An event represents:

```text
something that happened
```

Events are the foundation of event-driven systems.

Examples:

```text
user.created
paper.uploaded
experiment.finished
analysis.completed
embedding.generated
```

An event is not a function call.

It is a signal describing a state change or action.

---

# Core Idea

Instead of directly calling workflows:

```text
call function
```

an event-driven system works like:

```text
emit event
      ↓
trigger workflows
```

This decouples systems.

---

# Why Events Matter

Events allow systems to become:

* asynchronous
* modular
* scalable
* loosely coupled
* extensible

Different workflows can react to the same event independently.

---

# Traditional Direct Call

Traditional backend logic often looks like:

```text
Upload File
      ↓
Parse File
      ↓
Generate Embeddings
      ↓
Store Vectors
```

Everything is tightly connected.

---

# Event-Driven Version

An event-driven version may look like:

```text
file.uploaded
      ↓
parse workflow
      ↓
emit parsed.completed
      ↓
embedding workflow
      ↓
emit embeddings.generated
      ↓
indexing workflow
```

Each stage becomes independent.

---

# Event Producers

An event producer is the component that emits events.

Examples:

* frontend
* backend API
* workflow
* ingestion service
* scheduled task

Example:

```text
experiment detector
→ emits experiment.detected
```

---

# Event Consumers

An event consumer listens for events.

When an event appears:

```text
consumer workflow executes
```

Multiple consumers may react to the same event.

---

# Example

One event:

```text
experiment.finished
```

may trigger:

```text
analysis workflow
comparison workflow
embedding workflow
notification workflow
```

without the producer knowing about them.

---

# Decoupling

One of the most important advantages:

```text
decoupling
```

The event producer does not need to know:

* who consumes the event
* how many workflows exist
* what downstream logic runs

This simplifies architectures.

---

# Event Naming

Event names are usually descriptive.

Common convention:

```text
entity.action
```

Examples:

```text
user.created
paper.uploaded
analysis.completed
experiment.failed
```

Good naming improves readability and maintainability.

---

# Event Payloads

Events usually contain:

* event name
* payload data
* metadata
* timestamp

Example:

```json
{
  "name": "experiment.finished",
  "data": {
    "run_id": "2026-05-04_143509",
    "heater_voltage": 16,
    "fps": 160
  }
}
```

The payload contains information needed by workflows.

---

# Events as Immutable Facts

A useful mental model:

```text
events describe facts that already happened
```

Examples:

```text
paper.uploaded
```

means:

```text
the upload already occurred
```

This is different from commands.

---

# Events vs Commands

Important distinction.

## Event

Describes:

```text
something that happened
```

Example:

```text
experiment.finished
```

---

## Command

Requests:

```text
something should happen
```

Example:

```text
run.analysis
```

Event-driven systems usually prefer event semantics.

---

# Why Events Improve Scalability

New workflows can be added without modifying producers.

Example:

Initially:

```text
experiment.finished
→ analysis workflow
```

Later:

```text
experiment.finished
→ analysis workflow
→ embedding workflow
→ evaluation workflow
→ visualization workflow
```

The producer remains unchanged.

---

# Event Streams

A system may generate many events continuously.

Conceptually:

```text
event stream
```

Examples:

```text
user.created
user.logged_in
paper.uploaded
analysis.started
analysis.completed
```

Modern distributed systems often operate as streams of events.

---

# Event Chaining

Workflows can emit additional events.

Example:

```text
paper.uploaded
      ↓
parse workflow
      ↓
emit paper.parsed
      ↓
embedding workflow
```

This creates event chains.

---

# Why Event Chains are Powerful

They allow:

* modular workflows
* independent scaling
* separation of concerns
* asynchronous processing
* distributed orchestration

Large systems are often composed of many event chains.

---

# Event Replay

Some event systems allow replaying events.

Meaning:

```text
re-run workflows from previous events
```

Useful for:

* debugging
* rebuilding indexes
* reprocessing data
* recovering failures

---

# Event Idempotency

Very important concept.

A workflow should ideally behave safely if the same event is processed multiple times.

Example:

```text
processing same event twice
```

should not corrupt the system.

This property is called:

```text
idempotency
```

---

# Why Idempotency Matters

Distributed systems may:

* retry events
* duplicate messages
* replay workflows
* recover after crashes

Without idempotency:

* duplicate embeddings
* duplicated database rows
* repeated notifications

may occur.

---

# Event Ordering

Event ordering can become complex.

Example:

```text
analysis.completed
```

arrives before:

```text
analysis.started
```

because of delays or retries.

Distributed systems cannot always assume perfect ordering.

---

# Eventual Consistency

Many event-driven systems become:

```text
eventually consistent
```

Meaning:

systems may temporarily differ but eventually converge.

This is common in distributed architectures.

---

# Events and AI Pipelines

AI systems naturally generate events.

Examples:

```text
paper.uploaded
embedding.generated
retrieval.completed
experiment.analyzed
model.evaluated
```

AI workflows are highly event-oriented.

---

# Example AI Workflow

```text
new_paper_uploaded
      ↓
parse PDF
      ↓
emit paper.parsed
      ↓
chunk workflow
      ↓
emit chunks.generated
      ↓
embedding workflow
      ↓
emit embeddings.created
```

This creates a modular ingestion pipeline.

---

# Events in This Project

Potential events:

```text
experiment.detected
experiment.analyzed
comparison.completed
paper.added
embedding.generated
plots.created
retrieval.index.updated
```

Potential workflows:

```text
experiment.detected
      ↓
extract metadata
      ↓
run optical analysis
      ↓
emit analysis.completed
```

---

# Event-Driven Scientific Systems

Scientific systems often involve:

* asynchronous acquisition
* long analyses
* derived outputs
* multiple processing stages
* independent modules

This naturally fits event-driven architecture.

---

# Event Persistence

Reliable systems usually persist events.

This enables:

* retries
* recovery
* observability
* auditability
* replay

Persistent events improve reliability.

---

# Event Observability

Good event systems allow inspection of:

* emitted events
* payloads
* timestamps
* workflow triggers
* retries
* failures

This is essential for debugging.

---

# Common Mistakes

## Poor Event Naming

Makes systems difficult to understand.

---

## Overloaded Events

One event containing too much unrelated information.

---

## Tight Coupling

Workflows depending too strongly on internal implementation details.

---

## Ignoring Idempotency

Can create duplicate processing.

---

## Assuming Perfect Ordering

Distributed systems rarely guarantee this completely.

---

# Recommended Event Design

Good events should usually be:

* descriptive
* focused
* immutable
* traceable
* idempotent-friendly

A useful philosophy:

```text
events describe facts
```

not commands.

---

# Important Insight

Events transform systems from:

```text
direct procedural execution
```

into:

```text
reactive distributed workflows
```

This architectural shift is fundamental in modern AI infrastructure.

---

# Key Insight

In event-driven systems:

```text
components communicate through facts
```

rather than tightly coupled direct execution.

This enables:

* scalability
* modularity
* asynchronous processing
* workflow orchestration
* distributed AI pipelines
