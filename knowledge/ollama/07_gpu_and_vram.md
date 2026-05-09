# GPU and VRAM

## Introduction

Modern local AI systems depend heavily on GPUs.

Although large language models appear to behave like conversational software systems, internally they are:

```text
Massive numerical computation systems
```

The GPU is therefore one of the most important components in local AI inference.

Understanding GPUs and VRAM is fundamental for:

* local AI deployment
* model selection
* performance optimization
* RAG systems
* inference engineering
* production AI infrastructure

---

# What Is a GPU?

GPU stands for:

```text
Graphics Processing Unit
```

Originally designed for graphics rendering, GPUs are highly optimized for:

```text
Massively parallel computation
```

This makes them ideal for neural network inference.

---

# Why GPUs Matter for AI

Large language models rely heavily on:

* matrix multiplications
* tensor operations
* attention mechanisms
* vectorized computation

These operations are extremely parallel.

GPUs can execute thousands of operations simultaneously.

CPUs cannot match this level of parallel throughput.

---

# CPU vs GPU

## CPU

Optimized for:

* sequential operations
* low-latency logic
* operating systems
* branching tasks

Characteristics:

* few powerful cores
* general-purpose processing

---

## GPU

Optimized for:

* parallel computation
* tensor math
* neural networks
* large matrix operations

Characteristics:

* thousands of smaller cores
* high throughput
* specialized memory systems

---

# AI Inference Pipeline

Typical local inference workflow:

```text
Prompt
    ↓
Tokenization
    ↓
GPU Inference
    ↓
Token Generation
    ↓
Decoded Response
```

The GPU accelerates the inference stage.

---

# What Is VRAM?

VRAM stands for:

```text
Video Random Access Memory
```

VRAM is memory located directly on the GPU.

It stores:

* model weights
* attention cache
* intermediate tensors
* activation buffers
* KV cache

VRAM is one of the primary constraints in local AI systems.

---

# Why VRAM Matters

A model must fit into memory to execute efficiently.

Approximate relationship:

```text
Larger model → More VRAM required
```

If VRAM is insufficient:

* inference slows dramatically
* memory swapping occurs
* execution may fail entirely

---

# Model Size and VRAM

Approximate relationships:

| Model Size | Typical VRAM Requirement |
| ---------- | ------------------------ |
| 3B         | Small                    |
| 7B         | Moderate                 |
| 13B        | Large                    |
| 70B        | Very large               |

Quantization can significantly reduce requirements.

---

# Example: Consumer GPUs

Examples:

| GPU      | Approximate VRAM |
| -------- | ---------------- |
| RTX 3060 | 12 GB            |
| RTX 3070 | 8 GB             |
| RTX 4090 | 24 GB            |

Available VRAM strongly affects which models can run locally.

---

# VRAM Usage Components

VRAM is consumed by multiple components.

## 1. Model Weights

The largest memory consumer.

Weights contain learned neural network parameters.

---

## 2. KV Cache

Stores attention information for previous tokens.

Larger context windows increase KV cache size.

---

## 3. Activations

Intermediate tensors produced during inference.

---

## 4. Runtime Buffers

Temporary memory structures used by CUDA kernels.

---

# Quantization and VRAM

Quantization compresses weights.

Examples:

* FP16
* Q8
* Q5
* Q4

Benefits:

* reduced VRAM usage
* reduced storage size
* faster loading

Trade-off:

```text
More compression ↔ Possible quality loss
```

Quantization is essential for consumer hardware.

---

# FP16 vs Quantized Models

## FP16

Advantages:

* higher numerical precision
* better quality

Disadvantages:

* very large memory usage

---

## Quantized Models

Advantages:

* smaller memory footprint
* faster execution
* consumer GPU compatibility

Disadvantages:

* slight quality degradation

Most local AI systems rely on quantized models.

---

# GPU Acceleration Frameworks

Modern AI inference depends on specialized acceleration frameworks.

Examples:

| Framework | Hardware      |
| --------- | ------------- |
| CUDA      | NVIDIA GPUs   |
| Metal     | Apple Silicon |
| ROCm      | AMD GPUs      |

Ollama commonly uses CUDA for NVIDIA hardware.

---

# CUDA

CUDA is NVIDIA's GPU computing platform.

CUDA enables:

* tensor computation
* GPU kernels
* neural network acceleration
* parallel inference

Most modern local AI tooling is heavily optimized for CUDA.

---

# GPU Utilization

GPU utilization measures how actively the GPU is working.

High utilization usually indicates:

* active inference
* tensor computation
* attention processing

Low utilization may indicate:

* CPU bottlenecks
* I/O delays
* inefficient pipelines

---

# Monitoring GPU Usage

Common monitoring tool:

```bash
nvidia-smi
```

Typical metrics:

* VRAM usage
* GPU utilization
* temperature
* power usage
* active processes

Monitoring is important for:

* debugging
* optimization
* deployment engineering

---

# Throughput and Latency

GPU performance affects:

## Throughput

```text
Tokens generated per second
```

---

## Latency

```text
Time until first token
```

More powerful GPUs generally improve both.

---

# Batch Processing

GPUs perform best with parallel workloads.

Batching multiple requests can improve:

* throughput
* hardware utilization
* efficiency

Trade-off:

```text
Larger batches → Higher latency per request
```

---

# Context Window and VRAM

Context length strongly affects memory usage.

Relationship:

```text
Longer context → Larger KV cache → More VRAM
```

Large-context inference can become memory-intensive.

---

# Thermal Constraints

AI inference can heavily stress GPUs.

Potential issues:

* overheating
* thermal throttling
* reduced clock speeds
* instability

Cooling becomes important in sustained inference workloads.

---

# Power Consumption

Modern GPUs consume substantial power during inference.

Large local AI systems may require:

* high-capacity power supplies
* thermal management
* efficient cooling

AI infrastructure has physical hardware constraints.

---

# Multi-GPU Systems

Advanced systems may use multiple GPUs.

Benefits:

* larger models
* distributed inference
* higher throughput

Challenges:

* synchronization
* communication overhead
* memory partitioning
* orchestration complexity

Most consumer systems use a single GPU.

---

# VRAM Exhaustion

A common failure mode:

```text
Out-of-memory error
```

Possible causes:

* oversized models
* excessive context windows
* insufficient quantization
* concurrent workloads

Solutions:

* smaller models
* more aggressive quantization
* reduced context size

---

# CPU Offloading

Some runtimes offload part of the model to CPU RAM.

Benefits:

* allows larger models

Disadvantages:

* slower inference
* PCIe bottlenecks
* increased latency

GPU-resident inference is much faster.

---

# Consumer vs Enterprise GPUs

## Consumer GPUs

Examples:

* RTX 3070
* RTX 4090

Advantages:

* affordable
* accessible
* strong local AI performance

Disadvantages:

* limited VRAM
* weaker reliability guarantees

---

## Enterprise GPUs

Examples:

* A100
* H100

Advantages:

* massive VRAM
* high throughput
* optimized for AI infrastructure

Disadvantages:

* extremely expensive

---

# GPUs and RAG Systems

In RAG systems, GPUs accelerate:

* embeddings generation
* LLM inference
* reranking models
* retrieval pipelines

Efficient RAG systems require careful GPU planning.

---

# GPUs and Scientific AI

Scientific AI systems often process:

* large datasets
* long documents
* multimodal data
* retrieval pipelines
* simulations

GPU constraints directly influence system design.

---

# GPU Bottlenecks in AI Systems

Common bottlenecks:

* insufficient VRAM
* memory bandwidth
* PCIe transfer overhead
* thermal throttling
* oversized context windows

AI engineering frequently becomes:

```text
Memory engineering
```

rather than pure algorithm design.

---

# Common Misconceptions

## Misconception 1

```text
Only model size matters
```

Reality:

Context windows and KV cache also consume memory.

---

## Misconception 2

```text
VRAM equals RAM
```

Reality:

VRAM is GPU memory.

RAM is system memory.

---

## Misconception 3

```text
More GPU utilization is always better
```

Reality:

Workload characteristics matter.

---

# Mental Models

Useful mental models:

```text
GPU = AI computation engine
```

```text
VRAM = Workspace where the model lives during inference
```

```text
Local AI ≈ Real-time GPU numerical simulation
```

---

# Relationship with AI Systems Engineering

Understanding GPUs and VRAM is essential for:

* inference optimization
* AI infrastructure
* deployment engineering
* RAG systems
* local AI architecture
* production AI services

Hardware constraints shape software architecture.

---

# Reflection

Modern local AI systems are fundamentally constrained by hardware.

Even though users interact with:

```text
Natural language interfaces
```

underneath, these systems rely on:

* tensor computation
* memory orchestration
* GPU acceleration
* high-throughput numerical pipelines

Understanding GPUs and VRAM is therefore essential for understanding:

* why models behave differently
* why inference speeds vary
* why deployment constraints exist
* why quantization matters
* why local AI engineering is fundamentally a systems problem
