# Running Models

## Introduction

One of the main goals of Ollama is to simplify local model execution.

Running a model locally involves:

* loading model weights
* allocating memory
* initializing inference
* generating tokens
* serving responses

Although the process appears simple from the command line, many internal systems are involved.

Understanding how models are executed is fundamental for:

* local AI engineering
* performance optimization
* GPU utilization
* RAG deployment
* production AI systems

---

# Basic Execution Workflow

The simplest execution command is:

```bash
ollama run qwen2.5:7b
```

This command triggers multiple internal steps.

---

# High-Level Execution Pipeline

When a model is executed:

```text
User Prompt
    ↓
Ollama Runtime
    ↓
Model Loading
    ↓
Tokenizer
    ↓
GPU/CPU Inference
    ↓
Token Generation
    ↓
Decoded Output
```

Each stage has computational and memory implications.

---

# Step 1 — Model Resolution

Ollama first resolves the requested model tag.

Example:

```bash
ollama run qwen2.5:7b
```

The runtime identifies:

* model family
* quantization
* metadata
* storage location
* runtime configuration

---

# Step 2 — Weight Loading

The model weights are loaded into:

* RAM
* VRAM
* cache structures

Large models may require several gigabytes.

Example:

| Model | Approximate Memory |
| ----- | ------------------ |
| 3B    | Small              |
| 7B    | Moderate           |
| 70B   | Very large         |

Weight loading is often one of the slowest initialization steps.

---

# Step 3 — Runtime Initialization

The runtime initializes:

* tokenizer
* attention cache
* inference graph
* CUDA kernels
* memory buffers

GPU acceleration is configured during this stage.

---

# Step 4 — Prompt Tokenization

Text is converted into tokens.

Example:

```text
"Hello world"
        ↓
[15496, 995]
```

The tokenizer transforms text into numerical representations understood by the neural network.

---

# Step 5 — Inference

The model processes the tokens.

Inference consists of:

```text
Forward passes through the neural network
```

This is the most computationally expensive stage.

Operations include:

* matrix multiplications
* attention computation
* activation functions
* probability estimation

GPUs dramatically accelerate these operations.

---

# Step 6 — Token Generation

The model predicts the next token.

Generation loop:

```text
Input tokens
    ↓
Predict next token
    ↓
Append token
    ↓
Repeat
```

Text generation occurs token by token.

---

# Step 7 — Decoding

Generated tokens are converted back into text.

Example:

```text
[15496, 995]
        ↓
"Hello world"
```

The final response is streamed to the user.

---

# Streaming

Ollama supports streaming generation.

Instead of waiting for the entire response:

```text
Token → Token → Token → Token
```

responses are streamed progressively.

Benefits:

* lower perceived latency
* smoother interaction
* real-time UI updates

Streaming is common in:

* chat systems
* assistants
* AI copilots
* RAG systems

---

# CPU vs GPU Execution

## CPU Execution

Models can run entirely on CPU.

Advantages:

* works on almost any machine
* no GPU required

Disadvantages:

* slow inference
* high latency
* low throughput

---

## GPU Execution

Models can execute on GPUs using:

* CUDA
* Metal
* hardware accelerators

Advantages:

* parallel computation
* faster token generation
* lower latency
* higher throughput

Modern local AI systems rely heavily on GPU acceleration.

---

# VRAM Usage

During execution, VRAM stores:

* model weights
* KV cache
* attention buffers
* temporary tensors

VRAM usage depends on:

* model size
* quantization
* context length
* batch size

---

# KV Cache

The Key-Value cache stores intermediate attention information.

Purpose:

```text
Avoid recomputing previous tokens
```

Benefits:

* faster generation
* lower computation cost

Trade-off:

```text
Larger context → Larger KV cache
```

KV cache memory can become significant for long contexts.

---

# Context Windows

Models operate within finite context windows.

Examples:

* 4K tokens
* 8K tokens
* 32K tokens
* 128K tokens

Larger context windows:

Advantages:

* more retrieval context
* larger conversations

Disadvantages:

* more VRAM
* slower inference
* larger KV cache

---

# Generation Parameters

Execution behavior can be controlled using parameters.

Examples:

| Parameter      | Purpose               |
| -------------- | --------------------- |
| temperature    | randomness            |
| top_p          | token sampling        |
| top_k          | candidate restriction |
| repeat_penalty | repetition control    |
| num_ctx        | context size          |

These parameters affect:

* creativity
* determinism
* reasoning stability
* hallucinations
* response diversity

---

# Running Interactive Sessions

Example:

```bash
ollama run qwen2.5:7b
```

This launches an interactive terminal session.

The model remains loaded during the conversation.

Benefits:

* reduced reload times
* persistent context
* lower latency between prompts

---

# Running Models Through APIs

Ollama exposes a local HTTP API.

Applications can send requests programmatically.

Typical architecture:

```text
Frontend
    ↓
FastAPI Backend
    ↓
Ollama API
    ↓
Local Model
```

This enables:

* chat applications
* RAG systems
* AI agents
* automation pipelines

---

# Running Embeddings Models

Embeddings models are executed differently.

Purpose:

```text
Text → Vector embedding
```

Example:

```bash
ollama run bge-m3
```

Embeddings models do not generate conversational text.

They generate numerical representations.

---

# Running Multiple Models

Ollama can manage multiple installed models.

Example:

```text
qwen2.5:7b
bge-m3
llama3.1:8b
```

Different models may be used for:

* chat
* embeddings
* coding
* vision
* reasoning

Memory management becomes important when switching between models.

---

# Cold Start vs Warm Execution

## Cold Start

First execution after loading weights.

Includes:

* model loading
* cache initialization
* runtime setup

Usually slower.

---

## Warm Execution

Model already loaded in memory.

Benefits:

* lower latency
* faster responses
* reduced initialization overhead

---

# Throughput and Latency

Two important performance metrics:

## Latency

```text
Time until first token
```

---

## Throughput

```text
Tokens generated per second
```

Performance depends on:

* GPU power
* quantization
* model architecture
* context size
* runtime optimization

---

# Running Models in RAG Systems

Typical RAG workflow:

```text
User Question
    ↓
Retriever
    ↓
Retrieved Context
    ↓
Prompt Assembly
    ↓
LLM Execution
    ↓
Generated Response
```

The model uses retrieved context during inference.

---

# Resource Constraints

Running local models introduces practical constraints.

Examples:

* VRAM exhaustion
* RAM pressure
* thermal throttling
* storage usage
* context overflow

System engineering decisions become important.

---

# Common Failure Modes

## Out-of-Memory Errors

The model exceeds available VRAM.

---

## Slow Generation

Possible causes:

* CPU inference
* insufficient GPU
* large context windows
* large models

---

## Context Overflow

Prompt exceeds context window.

---

## Model Unloading Delays

Switching between models may require reloading weights.

---

# Monitoring Execution

Important metrics:

* VRAM usage
* GPU utilization
* token throughput
* latency
* temperature
* memory allocation

Tools:

* nvidia-smi
* Ollama logs
* profiling tools

---

# Relationship with AI Systems Engineering

Running models is not merely a user interaction problem.

It is fundamentally:

```text
A systems engineering problem
```

It involves:

* memory management
* GPU scheduling
* inference optimization
* latency engineering
* runtime orchestration
* deployment architecture

---

# Mental Model

Useful mental model:

```text
Running an LLM ≈ Running a GPU-intensive inference server
```

The chatbot interface is only the visible layer.

The underlying system is a complex inference pipeline.

---

# Reflection

Executing local AI models appears deceptively simple:

```bash
ollama run model
```

However, this command activates:

* large neural networks
* GPU acceleration
* memory orchestration
* token streaming
* probabilistic generation
* runtime optimization

Understanding model execution is therefore essential for building:

* efficient RAG systems
* local AI infrastructure
* scientific AI assistants
* scalable AI applications
* production-ready intelligent systems
