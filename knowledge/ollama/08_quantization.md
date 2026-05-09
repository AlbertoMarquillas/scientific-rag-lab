# Quantization

## Introduction

One of the key technologies enabling modern local AI systems is:

```text
Quantization
```

Without quantization, most large language models would be too large to run efficiently on consumer hardware.

Quantization enables:

* reduced VRAM usage
* reduced RAM usage
* smaller storage requirements
* faster inference
* local execution of large models

Quantization is therefore fundamental for:

* Ollama
* local LLMs
* RAG systems
* edge AI
* consumer AI hardware

---

# What Is Quantization?

Quantization is the process of:

```text
Reducing the numerical precision of model weights
```

Neural networks store parameters using numbers.

Example:

```text
32-bit floating point numbers
```

Quantization compresses these values into smaller numerical representations.

---

# Core Idea

Original representation:

```text
High precision → Large memory usage
```

Quantized representation:

```text
Lower precision → Smaller memory usage
```

This allows models to fit inside limited GPU memory.

---

# Why Quantization Matters

Modern LLMs contain billions of parameters.

Example:

```text
7 billion parameters
```

Storing these weights at full precision requires enormous memory.

Quantization dramatically reduces this requirement.

Without quantization:

```text
Most consumer GPUs could not run modern LLMs
```

---

# Floating Point Precision

Neural networks commonly use floating point representations.

Examples:

| Format | Bits   |
| ------ | ------ |
| FP32   | 32-bit |
| FP16   | 16-bit |
| BF16   | 16-bit |

Higher precision:

Advantages:

* better numerical accuracy
* higher model fidelity

Disadvantages:

* larger memory usage
* slower inference

---

# Quantized Precision Levels

Common quantization levels:

| Format | Description        |
| ------ | ------------------ |
| Q8     | 8-bit quantization |
| Q6     | 6-bit quantization |
| Q5     | 5-bit quantization |
| Q4     | 4-bit quantization |

Lower bit-width means:

```text
Smaller model size
```

---

# Memory Reduction

Approximate relationship:

```text
Lower precision → Lower memory usage
```

Example:

| Precision | Relative Memory |
| --------- | --------------- |
| FP16      | Large           |
| Q8        | Medium          |
| Q4        | Small           |

This reduction is critical for local inference.

---

# Example Conceptually

Original weight:

```text
0.483729183
```

Quantized representation:

```text
0.48
```

The representation becomes less precise.

But inference remains usable.

---

# Trade-Offs

Quantization introduces trade-offs.

## Advantages

* lower VRAM usage
* lower RAM usage
* faster loading
* faster inference
* consumer GPU compatibility

---

## Disadvantages

* reduced numerical precision
* possible quality degradation
* reduced reasoning fidelity
* potential instability in extreme compression

Quantization always balances:

```text
Efficiency ↔ Accuracy
```

---

# Why LLMs Tolerate Quantization

Neural networks are highly redundant.

Many weights can lose precision without significantly affecting behavior.

This makes quantization surprisingly effective.

Even aggressively quantized models often remain highly capable.

---

# Quantization in Ollama

Ollama commonly distributes quantized models.

Examples:

```text
Q4
Q5
Q8
```

This allows large models to run on:

* consumer GPUs
* laptops
* personal workstations

without enterprise hardware.

---

# GGUF Format

Many local models use:

```text
GGUF
```

GGUF is a format optimized for:

* quantized inference
* efficient loading
* compatibility with local runtimes

GGUF is heavily used by:

* Ollama
* llama.cpp
* local inference ecosystems

---

# Types of Quantization

## Post-Training Quantization

The model is trained normally.

Quantization occurs afterward.

Most local LLMs use this approach.

---

## Quantization-Aware Training

The model is trained while considering quantization.

This may improve stability.

More complex to implement.

---

# Symmetric vs Asymmetric Quantization

Different mathematical strategies exist.

## Symmetric

Centered around zero.

Simpler computation.

---

## Asymmetric

Allows shifted ranges.

May preserve information more efficiently.

---

# Activation Quantization

Quantization can apply to:

* weights
* activations
* intermediate tensors

Activation quantization is often more difficult.

---

# Quantization and VRAM

Quantization directly affects:

```text
Model memory footprint
```

Example:

| Quantization | Approximate VRAM Usage |
| ------------ | ---------------------- |
| FP16         | Very high              |
| Q8           | High                   |
| Q5           | Moderate               |
| Q4           | Lower                  |

This determines which models fit on a GPU.

---

# Quantization and Speed

Quantization may improve:

* inference speed
* loading time
* throughput

Smaller tensors move through memory faster.

However, speed improvements depend on:

* runtime implementation
* hardware
* CUDA kernels
* memory bandwidth

---

# Quantization and Quality

Excessive compression can reduce:

* reasoning quality
* factual accuracy
* instruction following
* coding performance

But moderate quantization often preserves surprisingly strong performance.

---

# Why Q4 Is Popular

Q4 quantization is extremely common because it provides:

* good memory efficiency
* acceptable quality
* consumer GPU compatibility

Many local AI systems use Q4 models by default.

---

# Quantization and Context Windows

Quantization reduces weight memory.

However:

```text
KV cache memory still grows with context length
```

Large contexts may still exhaust VRAM.

Quantization does not solve every memory constraint.

---

# Quantization and RAG Systems

RAG systems commonly use quantized models because:

* retrieval already supplies context
* extreme frontier-level reasoning may not be necessary
* inference efficiency becomes important

This enables:

* local document assistants
* scientific retrieval systems
* offline AI pipelines

---

# Quantization and Scientific AI

Scientific systems often prioritize:

* reproducibility
* local execution
* offline operation
* hardware efficiency

Quantization enables large-scale experimentation on personal hardware.

---

# Quantization and Deployment

Deployment constraints strongly influence quantization choices.

Example trade-offs:

| Scenario         | Preferred Quantization  |
| ---------------- | ----------------------- |
| High quality     | Q8 / FP16               |
| Consumer GPU     | Q4 / Q5                 |
| Edge devices     | Aggressive quantization |
| Research systems | Balanced                |

There is no universally optimal quantization level.

---

# Model Selection and Quantization

Two versions of the same model may behave differently.

Example:

```text
qwen2.5:7b-q4
vs
qwen2.5:7b-q8
```

Possible differences:

* VRAM usage
* speed
* reasoning quality
* latency
* stability

Quantization is therefore a deployment decision.

---

# Common Quantization Failure Modes

## Excessive Compression

The model becomes unstable.

---

## Hallucinations Increase

Reasoning fidelity decreases.

---

## Instruction Following Weakens

The model becomes less reliable.

---

## Numerical Precision Loss

Sensitive reasoning tasks degrade.

---

# Quantization and Benchmarking

Quantized models should be evaluated using:

* reasoning benchmarks
* retrieval tasks
* latency tests
* VRAM measurements
* domain-specific evaluations

Deployment quality depends on real-world testing.

---

# Quantization in Modern AI Infrastructure

Quantization is one of the key reasons why:

```text
Local AI became practical
```

Without it:

* consumer GPUs would be insufficient
* edge AI would be impractical
* local RAG systems would be much harder

Quantization fundamentally changed AI deployment.

---

# Mental Models

Useful mental models:

```text
Quantization = Compressing neural network precision
```

```text
Quantization = Trading numerical fidelity for efficiency
```

```text
Quantized models = Memory-optimized neural networks
```

---

# Relationship with AI Systems Engineering

Understanding quantization is essential for:

* local AI deployment
* GPU optimization
* inference engineering
* edge AI
* RAG systems
* production AI infrastructure

Quantization connects:

```text
Neural network mathematics
        with
Real hardware constraints
```

---

# Reflection

Quantization is one of the foundational technologies behind modern local AI.

It enables:

* powerful local assistants
* consumer GPU inference
* private RAG systems
* scientific AI workflows
* offline intelligent systems

by making massive neural networks:

* smaller
* faster
* cheaper
* deployable

Understanding quantization is therefore essential for understanding how advanced AI systems became accessible outside large cloud infrastructure providers.
