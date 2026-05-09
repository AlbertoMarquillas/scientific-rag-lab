# Retries and Failures

---

# Why Failures Matter

Distributed systems fail constantly.

This is not an exception.

It is normal behavior.

Examples:

* API timeout
* network instability
* database unavailable
* rate limits
* server restart
* corrupted file
* malformed payload
* external service outage

Modern workflow systems are designed assuming failures will happen.

---

# Important Mindset

One of the most important concepts in distributed systems:

```text
failure is normal
```

Reliable systems are not systems that never fail.

Reliable systems are systems that:

* detect failures
* recover safely
* retry correctly
* preserve state
* continue execution

---

# What is a Retry?

A retry means:

```text
attempt execution again after failure
```

Example:

```text
generate embeddings
      ↓
OpenAI timeout
      ↓
retry
      ↓
success
```

Retries are fundamental in workflow orchestration.

---

# Why Retries Exist

Many failures are temporary.

Examples:

* transient network issues
* temporary overload
* API rate limiting
* brief infrastructure outages

Retrying later often succeeds.

---

# Workflow Reliability

Without retries:

```text
small temporary failures
→ complete workflow failure
```

With retries:

```text
temporary failure
→ automatic recovery
```

Retries dramatically improve reliability.

---

# Retry Example

Suppose:

```text
Step 1 → parse PDF
Step 2 → generate embeddings
Step 3 → store vectors
```

If Step 2 fails temporarily:

```text
retry Step 2
```

instead of restarting everything.

---

# Durable Execution

Retries become powerful because workflows are durable.

Meaning:

* completed steps persist
* failed steps retry independently
* workflows resume safely

Without durability:

```text
restart entire workflow
```

With durability:

```text
retry only failed step
```

---

# Transient vs Permanent Failures

Important distinction.

---

# Transient Failures

Temporary problems.

Examples:

* timeout
* network issue
* rate limit
* temporary API outage

Retries are useful.

---

# Permanent Failures

Problems unlikely to succeed after retry.

Examples:

* malformed file
* invalid API key
* corrupted payload
* unsupported document

Retries alone will not solve these.

---

# Retry Strategy

Good systems distinguish between:

```text
retryable
vs
non-retryable
```

failures.

This prevents unnecessary retries.

---

# Exponential Backoff

Common retry strategy:

```text
wait longer after each failure
```

Example:

```text
Retry 1 → wait 1s
Retry 2 → wait 2s
Retry 3 → wait 4s
Retry 4 → wait 8s
```

This reduces overload during outages.

---

# Why Backoff Matters

Without backoff:

```text
thousands of retries immediately
```

can overload systems even more.

Backoff improves stability.

---

# Retry Limits

Retries are usually limited.

Otherwise:

```text
infinite retry loops
```

may occur.

Systems often define:

* max retry count
* retry intervals
* timeout limits

---

# Retryable AI Failures

Common retryable failures in AI systems:

* embedding timeout
* LLM rate limit
* vector DB unavailable
* temporary GPU overload
* transient API error

These are very common in production AI systems.

---

# Non-Retryable AI Failures

Examples:

* invalid prompt format
* corrupted document
* unsupported file type
* invalid metadata
* authentication failure

Retries usually waste resources here.

---

# Step-Level Retries

Inngest retries steps independently.

Example:

```text
Step 1 → success
Step 2 → success
Step 3 → failure
```

Only Step 3 retries.

This is one of the core workflow advantages.

---

# Why Step Isolation Matters

Without step isolation:

```text
restart everything
```

This creates:

* wasted compute
* duplicated API calls
* higher costs
* longer workflows

Step isolation improves efficiency.

---

# Idempotency

Retries require:

```text
idempotency
```

Meaning:

```text
re-running the same step
should not corrupt state
```

Examples of bad non-idempotent behavior:

* duplicate embeddings
* repeated emails
* duplicated DB rows
* repeated notifications

---

# Why Idempotency Matters

Retries may occur because of:

* failures
* crashes
* replays
* infrastructure restarts

Reliable systems assume duplicate execution is possible.

---

# Common Idempotency Strategies

Examples:

* unique IDs
* upserts instead of inserts
* deduplication checks
* state validation
* transactional operations

Idempotency is a core distributed systems principle.

---

# Timeouts

Workflows often define timeouts.

Examples:

* API call timeout
* workflow timeout
* step timeout

Timeouts prevent workflows from hanging forever.

---

# Dead Letter Queues

Some systems move permanently failing workflows into:

```text
dead letter queues
```

Meaning:

```text
failed workflows needing inspection
```

Useful for:

* debugging
* manual recovery
* auditing

---

# Failure Visibility

Good workflow systems provide observability.

You should be able to inspect:

* failed steps
* retry count
* error messages
* timing
* workflow history

Without observability, debugging becomes extremely difficult.

---

# Example Debugging Scenario

Without observability:

```text
workflow failed
```

With observability:

```text
Step: generate_embeddings
Error: rate limit exceeded
Retries: 3
Duration: 18s
```

This is dramatically more useful.

---

# Failure Propagation

Failures may propagate through workflows.

Example:

```text
embedding generation fails
      ↓
indexing cannot proceed
      ↓
retrieval update fails
```

Workflow orchestration helps manage these dependencies.

---

# Partial Failures

Distributed systems often experience:

```text
partial failures
```

Meaning:

some components fail while others continue working.

Example:

```text
vector DB unavailable
but metadata DB still operational
```

Modern systems must tolerate partial failure.

---

# Workflow Recovery

Good workflow systems support recovery after:

* crashes
* infrastructure restarts
* temporary outages
* interrupted execution

Durability enables safe recovery.

---

# Failure Handling Strategies

Common approaches:

* retries
* backoff
* fallback logic
* circuit breakers
* dead letter queues
* graceful degradation

Reliable systems combine multiple strategies.

---

# Circuit Breakers

A circuit breaker prevents repeated requests to failing services.

Example:

```text
service failing repeatedly
→ temporarily stop requests
```

This prevents cascading overload.

---

# Graceful Degradation

Instead of complete failure:

```text
reduced functionality
```

Example:

```text
retrieval works
but reranking disabled temporarily
```

Graceful degradation improves resilience.

---

# Failures in AI Systems

AI systems are especially failure-prone because they depend on:

* external APIs
* large models
* GPUs
* vector DBs
* asynchronous pipelines
* expensive inference

Workflow orchestration becomes essential.

---

# RAG Failure Examples

Possible RAG failures:

* embedding generation timeout
* vector DB unavailable
* chunking error
* malformed PDF
* reranker failure
* retrieval latency spike

Reliable RAG systems require robust failure handling.

---

# Agentic Failure Examples

Agentic systems introduce additional risks:

* infinite loops
* invalid tool calls
* hallucinated tool outputs
* dependency failures
* multi-step reasoning collapse

Agent workflows require strong orchestration.

---

# Failures in This Project

Potential failures:

* HDF5 read failure
* analysis module crash
* embedding API timeout
* Qdrant unavailable
* malformed metadata
* invalid plot generation

Potential retries:

```text
retry embedding generation
retry vector storage
retry summary generation
```

---

# Scientific Workflow Reliability

Scientific systems require strong reliability because:

* experiments are expensive
* analyses are long-running
* reproducibility matters
* data loss is dangerous

Workflow durability becomes especially important.

---

# Workflow Replay

Some systems allow replaying workflows.

Useful for:

* rebuilding indexes
* regenerating embeddings
* rerunning analyses
* debugging failures

Replay requires idempotent workflows.

---

# Common Mistakes

## No Idempotency

Retries create corrupted state.

---

## Infinite Retries

Systems waste resources indefinitely.

---

## Retrying Permanent Failures

Unnecessary retries increase costs.

---

## Weak Observability

Failures become impossible to diagnose.

---

## Giant Non-Isolated Steps

Small failures restart huge workflows.

---

# Recommended Failure Philosophy

Good systems assume:

* failures will happen
* retries are necessary
* recovery is essential
* duplicate execution is possible
* observability is critical

This mindset is central to distributed systems engineering.

---

# Important Insight

Retries are not:

```text
optional extras
```

They are a foundational mechanism of reliable distributed systems.

Modern AI infrastructure depends heavily on retry-safe orchestration.

---

# Key Insight

Reliable workflow systems are not designed around:

```text
perfect execution
```

They are designed around:

```text
safe recovery from failure
```

This philosophy is one of the foundations of modern event-driven and AI workflow infrastructure.
