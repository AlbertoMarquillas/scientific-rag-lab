# Models and Tags

## Introduction

One of the most important concepts in Ollama is the relationship between:

* models
* versions
* variants
* quantizations
* tags

Understanding model naming conventions is essential for:

* selecting appropriate models
* managing VRAM usage
* optimizing inference
* reproducing experiments
* deploying stable AI systems

---

# What Is a Model?

A model is a pretrained neural network capable of performing tasks such as:

* text generation
* summarization
* reasoning
* code generation
* embeddings generation
* question answering

Examples:

* Llama
* Qwen
* Mistral
* Gemma
* Phi
* DeepSeek

Models differ in:

* architecture
* parameter count
* training data
* capabilities
* context window
* reasoning quality
* speed

---

# Model Families

A model family is a collection of related models.

Examples:

| Family  | Examples                  |
| ------- | ------------------------- |
| Llama   | llama3.1:8b, llama3.1:70b |
| Qwen    | qwen2.5:3b, qwen2.5:7b    |
| Mistral | mistral:7b                |
| Gemma   | gemma2:9b                 |
| Phi     | phi3:mini                 |

Each family usually contains multiple sizes and variants.

---

# Parameter Count

Models are often identified by parameter count.

Examples:

| Model | Approximate Parameters |
| ----- | ---------------------- |
| 3B    | 3 billion              |
| 7B    | 7 billion              |
| 13B   | 13 billion             |
| 70B   | 70 billion             |

Larger models generally provide:

* better reasoning
* higher accuracy
* improved language understanding

But also require:

* more VRAM
* more RAM
* more storage
* more compute power

---

# Ollama Model Naming

Typical Ollama naming format:

```text
model_name:model_size
```

Examples:

```text
qwen2.5:7b
llama3.1:8b
mistral:7b
phi3:mini
```

The tag after the colon identifies a specific variant.

---

# What Is a Tag?

A tag identifies a specific model variant.

Tags may represent:

* model size
* quantization
* version
* architecture
* specialization
* context length

Example:

```text
qwen2.5:7b
```

Where:

* `qwen2.5` = model family/version
* `7b` = parameter size

---

# Why Tags Matter

Tags are critical because:

```text
Different tags may behave very differently
```

Differences may include:

* memory usage
* speed
* quality
* context size
* reasoning ability
* multilingual support
* instruction tuning

---

# Model Variants

Many models have multiple variants.

Examples:

## Base Models

General pretrained models.

Usually not optimized for conversation.

---

## Instruct Models

Fine-tuned for instruction following.

Better for:

* chat
* assistants
* RAG
* coding assistants

---

## Code Models

Specialized for programming.

Examples:

* codegemma
* codellama
* deepseek-coder

---

## Embeddings Models

Generate vector embeddings instead of text.

Examples:

* bge-m3
* nomic-embed-text
  n
  Embeddings models are fundamental for RAG.

---

# Model Tags and Quantization

Many Ollama tags include quantization information.

Examples:

```text
q4
q5
q8
```

Quantization reduces:

* VRAM usage
* RAM usage
* storage size

Trade-off:

```text
Smaller memory footprint ↔ Potential quality reduction
```

---

# Quantization Types

Common quantization formats:

| Quantization | Characteristics                 |
| ------------ | ------------------------------- |
| Q4           | Small memory usage              |
| Q5           | Balanced                        |
| Q8           | Higher quality                  |
| FP16         | Very high quality, large memory |

More aggressive quantization usually improves speed and memory efficiency.

---

# Example Model Identifiers

Examples:

```text
llama3.1:8b
```

Meaning:

* Family: Llama 3.1
* Size: 8B parameters

---

```text
qwen2.5:7b
```

Meaning:

* Family: Qwen 2.5
* Size: 7B parameters

---

```text
phi3:mini
```

Meaning:

* Family: Phi 3
* Small optimized variant

---

# Pulling Models

Models are downloaded using:

```bash
ollama pull qwen2.5:7b
```

This downloads:

* weights
* quantized files
* metadata
* runtime configuration

The model becomes available locally.

---

# Running Models

Example:

```bash
ollama run qwen2.5:7b
```

The runtime:

* loads weights into memory
* initializes inference
* starts token generation

---

# Listing Installed Models

Installed models can be inspected using:

```bash
ollama list
```

Example output:

```text
NAME            SIZE
qwen2.5:7b      4.7 GB
bge-m3          1.2 GB
```

---

# Model Storage

Downloaded models occupy local disk space.

Large models may require:

* tens of gigabytes
* fast SSD storage
* significant cache space

Managing storage becomes important in large AI systems.

---

# Model Updates

Models can evolve over time.

Updates may include:

* bug fixes
* improved weights
* better quantizations
* larger context windows
* instruction tuning improvements

Reproducibility requires tracking exact model versions.

---

# Reproducibility and Tags

Tags are extremely important for reproducibility.

Example:

```text
Using "qwen2.5:7b" today may produce different results than another model variant tomorrow.
```

Scientific and production systems should track:

* exact model name
* exact tag
* quantization
* runtime version

---

# Context Window Differences

Different tags may support different context windows.

Examples:

* 4K tokens
* 8K tokens
* 32K tokens
* 128K tokens

Larger context windows require:

* more memory
* larger KV cache
* slower inference

---

# Specialized Models

Some models are specialized for particular domains.

Examples:

| Domain      | Examples                   |
| ----------- | -------------------------- |
| Coding      | Code Llama, DeepSeek-Coder |
| Mathematics | DeepSeek-Math              |
| Embeddings  | bge-m3                     |
| Vision      | LLaVA                      |
| Multimodal  | Qwen-VL                    |

Selecting the right specialization is important.

---

# Choosing a Model

Model selection depends on:

* available VRAM
* latency requirements
* reasoning quality
* context requirements
* multilingual support
* coding capability
* deployment constraints

---

# Typical Trade-Offs

## Small Models

Advantages:

* fast
* low VRAM
* low latency

Disadvantages:

* weaker reasoning
* lower accuracy

---

## Large Models

Advantages:

* stronger reasoning
* higher quality
* better instruction following

Disadvantages:

* high VRAM
* slower inference
* larger storage

---

# Popular Local Models

## Qwen

Strong:

* reasoning
* coding
* multilingual support

Popular for RAG systems.

---

## Llama

General-purpose family.

Large ecosystem and tooling support.

---

## Mistral

Known for:

* efficiency
* speed
* compact architectures

---

## Phi

Small but efficient models.

Good for lightweight systems.

---

# Embeddings Models

Embeddings models differ from chat models.

Purpose:

```text
Text → Vector representation
```

Examples:

| Model            | Purpose             |
| ---------------- | ------------------- |
| bge-m3           | Semantic embeddings |
| nomic-embed-text | Semantic retrieval  |

Embeddings models are essential for:

* semantic search
* vector databases
* RAG pipelines

---

# Relationship with RAG

Typical RAG architecture:

```text
Documents
    ↓
Embeddings model
    ↓
Vector DB
    ↓
Retriever
    ↓
Generative LLM
```

Different models play different roles.

---

# Local Model Ecosystem Complexity

Modern local AI ecosystems are rapidly evolving.

New models appear frequently.

Developers must evaluate:

* benchmarks
* latency
* VRAM usage
* multilingual quality
* coding performance
* retrieval quality

There is no universally best model.

---

# Common Misconceptions

## Misconception 1

```text
Bigger models are always better
```

Reality:

Deployment constraints matter.

---

## Misconception 2

```text
All model tags behave similarly
```

Reality:

Different tags may produce very different behavior.

---

## Misconception 3

```text
Embeddings models and chat models are interchangeable
```

Reality:

They solve different tasks.

---

# Importance in AI Engineering

Understanding models and tags is fundamental for:

* local AI deployment
* RAG engineering
* reproducibility
* performance optimization
* GPU planning
* infrastructure design
* scientific AI systems

It connects:

```text
Model architecture
        with
Real deployment constraints
```

---

# Reflection

Models and tags are not simple labels.

They encode:

* architecture choices
* deployment trade-offs
* memory requirements
* reasoning capability
* inference behavior
* quantization strategies

Understanding them is essential for moving from:

```text
"running AI"
```

to:

```text
engineering AI systems
```

where model selection becomes a critical architectural decision.
