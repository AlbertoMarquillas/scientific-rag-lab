# Streaming and Generation

## Introduction

Large language models generate text progressively.

Instead of producing an entire response instantly:

```text
Token → Token → Token → Token
```

Modern AI systems stream generated text incrementally.

Streaming and generation mechanisms are fundamental for:

* chat systems
* AI assistants
* RAG applications
* coding copilots
* AI agents
* real-time interfaces
* production AI infrastructure

Understanding generation and streaming is essential for modern AI systems engineering.

---

# What Is Text Generation?

Text generation is the process of:

```text
Predicting the next token repeatedly
```

The model receives:

* prompts
* context
* conversation history
* retrieved information

and iteratively predicts the most probable next token.

---

# Core Generation Loop

Conceptually:

```text
Input Tokens
    ↓
Neural Network Inference
    ↓
Probability Distribution
    ↓
Next Token Selection
    ↓
Append Token
    ↓
Repeat
```

Generation continues until:

* stop condition
* maximum tokens
* stop sequence
* end-of-sequence token

---

# Tokens and Generation

LLMs do not generate full sentences directly.

They generate:

```text
Discrete tokens
```

Examples:

| Text         | Possible Tokens |
| ------------ | --------------- |
| hello        | 1 token         |
| turbulence   | multiple tokens |
| code snippet | many tokens     |

Generation speed is often measured in:

```text
Tokens per second
```

---

# Autoregressive Generation

Most modern LLMs are:

```text
Autoregressive models
```

Meaning:

Each generated token becomes part of the next input.

Example:

```text
Prompt
    ↓
Generate token 1
    ↓
Prompt + token 1
    ↓
Generate token 2
```

The process is recursive.

---

# Probability Distributions

At every step, the model predicts probabilities.

Example conceptually:

```text
"the"   → 0.41
"a"     → 0.19
"this"  → 0.11
```

Sampling algorithms select the next token.

Generation parameters strongly affect this process.

---

# Deterministic Generation

Low randomness.

Behavior:

* stable
* predictable
* reproducible

Useful for:

* RAG
* coding
* scientific systems
* structured outputs

---

# Stochastic Generation

Higher randomness.

Behavior:

* creative
* diverse
* exploratory

Useful for:

* brainstorming
* storytelling
* creative writing

---

# Sampling

Sampling determines how tokens are selected.

Common strategies:

| Strategy        | Purpose                           |
| --------------- | --------------------------------- |
| Greedy decoding | Always choose highest probability |
| Top-k           | Restrict candidate count          |
| Top-p           | Restrict cumulative probability   |
| Temperature     | Control randomness                |

Sampling strongly shapes generation behavior.

---

# Greedy Decoding

Greedy decoding selects:

```text
Highest-probability token only
```

Advantages:

* deterministic
* stable

Disadvantages:

* repetitive
* low diversity

---

# Temperature

Temperature scales probability distributions.

Low temperature:

* focused
* deterministic

High temperature:

* diverse
* unpredictable

Temperature strongly affects generation quality.

---

# Top-K Sampling

Top-k limits sampling to:

```text
K highest-probability tokens
```

Smaller values:

* focused outputs

Larger values:

* exploratory outputs

---

# Top-P Sampling

Top-p uses cumulative probability thresholds.

Example:

```text
top_p = 0.9
```

The model samples only from tokens covering 90% probability mass.

This adapts dynamically to uncertainty.

---

# Streaming

Streaming means:

```text
Returning generated tokens progressively
```

instead of waiting for the complete response.

Example:

```text
T
Th
The
The model
```

Streaming improves responsiveness.

---

# Why Streaming Matters

Without streaming:

Users must wait for complete inference.

With streaming:

* lower perceived latency
* real-time interaction
* smoother user experience

Streaming is now standard in modern AI systems.

---

# Time to First Token

A critical metric:

```text
TTFT = Time To First Token
```

TTFT includes:

* model loading
* prompt processing
* initial inference
* KV cache initialization

Users perceive TTFT strongly.

---

# Tokens Per Second

Another critical metric:

```text
TPS = Tokens Per Second
```

Higher TPS means:

* faster responses
* smoother streaming
* better UX

TPS depends on:

* GPU power
* quantization
* context length
* runtime optimization

---

# Streaming and User Experience

Streaming creates the illusion of:

```text
Real-time reasoning
```

Even though the model performs probabilistic token prediction.

Streaming dramatically improves perceived intelligence.

---

# Streaming in Ollama

Ollama supports streaming generation through:

* CLI
* API
* integrations

Applications receive tokens progressively.

This enables:

* live chat interfaces
* streaming APIs
* real-time assistants

---

# Streaming and APIs

Typical architecture:

```text
Frontend
    ↓
Backend
    ↓
Streaming API
    ↓
Ollama
    ↓
Model
```

Streaming data flows continuously through the pipeline.

---

# Streaming and RAG

RAG systems frequently stream responses.

Workflow:

```text
Retrieve Context
    ↓
Assemble Prompt
    ↓
Start Generation
    ↓
Stream Tokens
```

Streaming improves responsiveness even when retrieval is expensive.

---

# Generation Latency

Generation latency includes:

* prompt processing
* retrieval
* model inference
* token decoding
* streaming overhead

Longer contexts increase latency.

---

# Context Length and Generation

Long contexts increase:

* attention computation
* KV cache size
* memory transfers
* latency

Relationship:

```text
Longer context → Slower generation
```

---

# KV Cache and Streaming

The KV cache stores attention information for previous tokens.

Benefits:

* avoids recomputation
* accelerates generation

Without KV cache:

Generation would become prohibitively slow.

---

# Batch Generation

Some systems process multiple requests simultaneously.

Benefits:

* improved GPU utilization
* higher throughput

Trade-offs:

* higher latency per request
* scheduling complexity

---

# Streaming and Concurrency

Production systems may stream to many users simultaneously.

Challenges:

* GPU contention
* scheduling
* memory allocation
* latency balancing

Concurrency becomes an infrastructure problem.

---

# Stop Conditions

Generation usually stops when:

* EOS token appears
* stop sequence detected
* token limit reached
* application interrupt occurs

Proper stopping behavior is important.

---

# Hallucinations During Generation

Generation is probabilistic.

Without grounding:

Models may:

* invent facts
* generate unsupported claims
* drift from context

RAG systems reduce hallucinations through retrieval grounding.

---

# Streaming and Structured Outputs

Structured outputs require careful generation control.

Examples:

* JSON
* XML
* markdown tables
* tool calls

Streaming malformed structures can become problematic.

---

# Streaming and AI Agents

Agents often stream:

* reasoning traces
* tool outputs
* intermediate steps
* planning information

Streaming improves transparency and interactivity.

---

# Generation and Scientific AI

Scientific systems often prioritize:

* factual grounding
* deterministic behavior
* reproducibility
* stable formatting

Streaming remains useful for:

* large reports
* long analyses
* retrieval-heavy workflows

---

# Common Failure Modes

## Slow Time To First Token

Possible causes:

* model loading
* cold starts
* large prompts

---

## Low Tokens Per Second

Possible causes:

* weak GPU
* oversized models
* long contexts

---

## Repetition Loops

Poor sampling configuration.

---

## Hallucinations

Weak grounding or excessive randomness.

---

## Broken Structured Outputs

Streaming interrupts formatting consistency.

---

# Streaming and Infrastructure

Streaming changes backend architecture.

Requirements may include:

* asynchronous APIs
* websocket support
* chunked responses
* buffering
* concurrency management

Modern AI systems are increasingly real-time systems.

---

# Mental Models

Useful mental models:

```text
Generation = Iterative probabilistic token prediction
```

```text
Streaming = Real-time incremental output delivery
```

```text
LLM responses = Sequential token sampling process
```

---

# Relationship with AI Systems Engineering

Understanding streaming and generation is essential for:

* AI assistants
* RAG systems
* AI agents
* inference optimization
* real-time AI systems
* production deployment

Generation mechanics connect:

```text
Neural network inference
        with
Interactive AI applications
```

---

# Reflection

Streaming and generation are fundamental mechanisms underlying modern AI systems.

Although users experience:

```text
Conversational interaction
```

internally, the system performs:

* iterative probabilistic inference
* token-by-token prediction
* real-time streaming
* GPU-accelerated computation

Understanding these mechanisms is essential for building:

* responsive AI assistants
* scalable RAG systems
* reliable scientific AI tools
* production-grade local AI infrastructure
