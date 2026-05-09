# Best Open Models

## Introduction

The open-model ecosystem evolves extremely quickly.

New models appear constantly with improvements in:

* reasoning
* coding
* multilingual support
* efficiency
* long-context handling
* multimodal capabilities
* instruction following

Choosing the right model is one of the most important decisions in local AI systems engineering.

There is no universally best model.

The optimal choice depends on:

* hardware
* VRAM
* latency requirements
* use case
* retrieval architecture
* deployment constraints

---

# What Is an Open Model?

An open model is typically a model whose:

* weights are publicly available
* architecture is known
* inference can run locally
* usage does not require proprietary APIs

Open models enable:

* local AI
* reproducibility
* customization
* offline inference
* research experimentation

---

# Open Models vs Closed Models

| Open Models                 | Closed Models                           |
| --------------------------- | --------------------------------------- |
| Local inference possible    | Usually API-only                        |
| Full infrastructure control | Vendor-controlled                       |
| Lower long-term cost        | Token-based pricing                     |
| Hardware required           | Cloud infrastructure handled externally |
| Customizable                | Limited transparency                    |

Open models are foundational for local AI ecosystems.

---

# Why Model Choice Matters

The model affects:

* reasoning quality
* hallucination rate
* latency
* VRAM usage
* multilingual ability
* coding performance
* retrieval quality
* context handling

The model becomes the reasoning core of the AI system.

---

# Important Evaluation Dimensions

Useful evaluation criteria:

| Dimension             | Meaning                        |
| --------------------- | ------------------------------ |
| Reasoning             | Logical and analytical ability |
| Coding                | Programming performance        |
| Multilingual          | Non-English capability         |
| Efficiency            | Performance per VRAM           |
| Context Window        | Maximum usable context         |
| Instruction Following | Reliability of responses       |
| Quantization Quality  | Performance after compression  |
| Speed                 | Tokens per second              |

Different models optimize different dimensions.

---

# Parameter Count

Models are often categorized by parameter count.

Examples:

| Size    | Typical Use                |
| ------- | -------------------------- |
| 1B–3B   | Lightweight assistants     |
| 7B–8B   | General local AI           |
| 13B–14B | Stronger reasoning         |
| 30B+    | Advanced local systems     |
| 70B+    | High-end inference servers |

Larger models generally require more VRAM.

---

# Small Models

Examples:

* Phi family
* Gemma small variants
* TinyLlama

Advantages:

* low VRAM
* fast inference
* lightweight deployment

Disadvantages:

* weaker reasoning
* more hallucinations
* weaker long-context performance

Useful for:

* lightweight assistants
* edge devices
* experimentation

---

# Mid-Sized Models

The most popular local category.

Typical range:

```text
7B–14B
```

Advantages:

* strong quality
* manageable VRAM
* practical local inference

This category is often the sweet spot for local RAG systems.

---

# Large Models

Examples:

* 32B
* 70B
* MoE architectures

Advantages:

* stronger reasoning
* better coding
* lower hallucination rates

Disadvantages:

* high VRAM requirements
* slower inference
* deployment complexity

Usually require powerful GPUs.

---

# Mixture-of-Experts (MoE)

Some models use:

```text
Mixture-of-Experts architectures
```

Only part of the model activates per token.

Advantages:

* strong capability
* better efficiency scaling

Disadvantages:

* more complex inference
* deployment challenges

MoE models are increasingly important.

---

# Popular Open Model Families

## Llama Family

Developed by Meta.

Known for:

* strong ecosystem
* broad tooling support
* solid general performance

Widely used in local AI.

---

## Qwen Family

Developed by Alibaba.

Known for:

* strong reasoning
* coding performance
* multilingual capability
* excellent local performance

Very popular in local RAG systems.

---

## Mistral Family

Known for:

* efficiency
* strong performance per parameter
* fast inference

Mistral models are common in production local systems.

---

## Gemma Family

Developed by Google.

Known for:

* efficient inference
* smaller deployment footprint
* good instruction following

Useful for lightweight systems.

---

## Phi Family

Developed by Microsoft.

Known for:

* small size
* educational reasoning
* lightweight deployment

Useful for edge devices and experimentation.

---

## DeepSeek Models

Known for:

* coding
* reasoning
* MoE architectures
* competitive open performance

Rapidly growing ecosystem.

---

# Coding Models

Some models specialize in coding.

Examples:

* DeepSeek-Coder
* CodeQwen
* StarCoder
* CodeLlama

Useful for:

* code generation
* debugging
* repositories
* AI development assistants

---

# Embeddings Models

Embeddings models are different from chat models.

Purpose:

```text
Generate semantic vectors
```

Popular local embeddings models:

* bge-m3
* nomic-embed-text
* mxbai-embed-large

These are critical for RAG systems.

---

# Vision Models

Multimodal models support:

* image understanding
* OCR-like reasoning
* diagram analysis
* visual question answering

Examples:

* LLaVA
* Qwen-VL
* vision-capable Llama variants

Useful for multimodal RAG.

---

# Long-Context Models

Some models support:

* 32K context
* 128K context
* long-document reasoning

Useful for:

* large reports
* scientific papers
* long conversations

Long contexts increase memory requirements.

---

# Quantization Compatibility

Not all models quantize equally well.

Good local models typically:

* retain quality after Q4/Q5 quantization
* remain stable under compression
* maintain reasonable reasoning ability

Quantization quality is critical for consumer GPUs.

---

# VRAM Considerations

Approximate guidance:

| Model Size | Typical VRAM Needs     |
| ---------- | ---------------------- |
| 3B         | ~2–4 GB                |
| 7B         | ~4–8 GB                |
| 14B        | ~10–16 GB              |
| 32B        | ~24+ GB                |
| 70B        | Multi-GPU often needed |

Quantization changes these numbers significantly.

---

# Choosing Models for RTX 3070 (8GB)

A practical configuration:

## Excellent Choices

* Qwen2.5 7B
* Mistral 7B
* Gemma 7B
* Llama 3.1 8B

Typically usable with:

* Q4 quantization
* moderate context windows

---

## Heavy but Possible

* 14B models with aggressive quantization

Trade-offs:

* slower inference
* smaller context
* higher VRAM pressure

---

## Usually Too Large

* 32B+
* 70B+

unless:

* CPU offloading
* multi-GPU setup
* cloud inference

---

# Model Selection for RAG

RAG systems usually prioritize:

* instruction following
* grounded reasoning
* low hallucinations
* context handling

Bigger models are not always necessary.

A strong retriever often matters more.

---

# Model Selection for Scientific AI

Scientific systems benefit from:

* precise reasoning
* uncertainty awareness
* long-context support
* stable formatting
* multilingual capability

Qwen-family models are often strong choices.

---

# Model Selection for Coding

Coding systems prioritize:

* syntax reliability
* repository understanding
* long-context handling
* deterministic outputs

Specialized coding models may outperform general chat models.

---

# Benchmark Limitations

Benchmarks are useful but imperfect.

Problems:

* benchmark overfitting
* synthetic tasks
* weak real-world correlation
* missing retrieval evaluation

Real deployment testing matters more.

---

# Hallucinations and Open Models

All open models hallucinate.

Differences include:

* frequency
* confidence
* reasoning quality
* retrieval grounding ability

RAG reduces hallucinations but does not eliminate them.

---

# Local AI Trade-Offs

Choosing a model involves balancing:

| Goal             | Trade-Off         |
| ---------------- | ----------------- |
| Better reasoning | More VRAM         |
| Faster inference | Smaller models    |
| Larger context   | More memory       |
| Better coding    | Larger deployment |

No model dominates every dimension.

---

# Open Ecosystem Dynamics

The open-model ecosystem evolves rapidly.

Important reality:

```text
The best model today may not be the best model next month
```

Model selection is a moving target.

---

# Practical Recommendation Strategy

A useful progression:

## Step 1

Start with:

```text
7B model + Q4 quantization
```

---

## Step 2

Evaluate:

* latency
* VRAM
* retrieval quality
* hallucinations

---

## Step 3

Upgrade only if necessary.

Bigger models are expensive.

---

# Minimal Practical Local Stack

For an 8GB GPU:

| Role       | Suggested Model     |
| ---------- | ------------------- |
| Chat LLM   | Qwen2.5 7B          |
| Embeddings | bge-m3              |
| Vision     | LLaVA small variant |

This is already powerful enough for serious local RAG experimentation.

---

# Common Failure Modes

## Oversized Model

VRAM exhaustion.

---

## Wrong Model for Task

Poor retrieval-grounded reasoning.

---

## Weak Quantization Choice

Severe quality degradation.

---

## Blind Benchmark Trust

Real-world quality disappoints.

---

## Ignoring Retrieval Quality

Large model but weak RAG pipeline.

---

# Mental Models

Useful mental models:

```text
The model is the reasoning engine, not the entire system
```

```text
Strong retrieval can outperform larger models
```

```text
Efficiency matters as much as raw intelligence
```

```text
Open models are infrastructure components
```

---

# Relationship with AI Systems Engineering

Choosing open models affects:

* deployment architecture
* VRAM requirements
* latency
* retrieval quality
* scalability
* observability
* cost
* reproducibility

Model selection is therefore a systems engineering decision.

---

# Reflection

The open-model ecosystem has transformed AI from a cloud-only capability into something that can run locally on consumer hardware.

Understanding open models means understanding:

* reasoning trade-offs
* hardware constraints
* retrieval interactions
* quantization
* deployment strategy

The best local AI systems are usually not built from the largest possible model.

They are built from:

* the right model
* the right retrieval pipeline
* the right infrastructure
* the right optimization strategy

working together as a coherent AI system.
