# Multimodal Models

## Introduction

Traditional language models process only:

```text
Text
```

Modern AI systems increasingly support:

* images
* audio
* video
* documents
* diagrams
* structured data

Models capable of processing multiple modalities are called:

```text
Multimodal models
```

Multimodal AI is one of the major directions of modern AI systems engineering.

---

# What Is a Modality?

A modality is:

```text
A type of information representation
```

Examples:

| Modality        | Examples         |
| --------------- | ---------------- |
| Text            | Language, code   |
| Image           | Photos, diagrams |
| Audio           | Speech, music    |
| Video           | Motion sequences |
| Structured data | Tables, JSON     |

Multimodal systems combine multiple modalities.

---

# What Is a Multimodal Model?

A multimodal model is:

```text
A model capable of processing multiple modalities simultaneously
```

Examples:

```text
Image + Text
Audio + Text
Video + Text
```

The model learns relationships between modalities.

---

# Core Idea

Traditional LLM:

```text
Text → Text
```

Multimodal model:

```text
Image + Text → Text
```

or:

```text
Audio + Text → Text
```

The model integrates information across modalities.

---

# Why Multimodal AI Matters

Real-world information is multimodal.

Examples:

* scientific figures
* diagrams
* laboratory images
* PDFs
* video streams
* user interfaces

Pure text systems cannot fully understand these environments.

---

# Multimodal Models in Ollama

Ollama supports several multimodal models.

Examples:

* LLaVA
* Qwen-VL
* vision-capable Llama variants

These models can process:

* text prompts
* image inputs

locally.

---

# Vision-Language Models

A common multimodal category:

```text
Vision-Language Models (VLMs)
```

These models combine:

* computer vision
* language modeling

Examples:

```text
Image → Semantic representation → Language reasoning
```

---

# High-Level Architecture

Typical multimodal architecture:

```text
Image Encoder
        ↓
Shared Representation Space
        ↓
Language Model
        ↓
Generated Response
```

The model aligns visual and textual information.

---

# Image Encoding

Images cannot be processed directly as raw pixels.

The image encoder transforms:

```text
Pixels → Embeddings
```

These embeddings become part of the model context.

---

# Shared Embedding Spaces

Multimodal systems often map:

* text
* images
* audio

into compatible embedding spaces.

This enables:

* cross-modal similarity
* image retrieval
* multimodal search
* visual reasoning

---

# Multimodal Prompting

Multimodal prompts combine:

* visual input
* textual instructions

Example conceptually:

```text
[Image]
"Describe the beam deformation visible in this frame"
```

The model reasons across both modalities.

---

# Vision Tasks

Multimodal models support tasks such as:

* image captioning
* visual question answering
* OCR-like reasoning
* diagram interpretation
* object recognition
* scene understanding

---

# Multimodal RAG

RAG systems can become multimodal.

Typical architecture:

```text
Documents
Images
Diagrams
Plots
        ↓
Embeddings
        ↓
Vector Database
        ↓
Retriever
        ↓
Multimodal LLM
```

This enables retrieval across multiple information types.

---

# Multimodal Embeddings

Embeddings can represent:

* text
* images
* audio

inside unified vector spaces.

Applications:

* image similarity
* semantic image search
* multimodal retrieval
* cross-modal search

---

# Cross-Modal Retrieval

Example:

```text
Text query → Retrieve images
```

or:

```text
Image query → Retrieve documents
```

This becomes possible through aligned embeddings.

---

# Multimodal AI and Scientific Systems

Scientific workflows are naturally multimodal.

Examples:

* plots
* microscopy images
* optical beam profiles
* PDFs
* tables
* experiment screenshots

Multimodal AI is particularly important in scientific environments.

---

# Example: Optical Turbulence Systems

Potential multimodal workflow:

```text
Beam Image
        ↓
Vision Model
        ↓
Describe deformation
        ↓
RAG retrieval
        ↓
Scientific reasoning
```

This enables AI-assisted experiment analysis.

---

# OCR and Document Understanding

Multimodal systems can analyze:

* scanned PDFs
* handwritten notes
* figures
* tables
* equations

This extends RAG beyond plain text.

---

# Video Understanding

Advanced multimodal systems may process:

* video frames
* temporal sequences
* motion patterns

Applications:

* surveillance
* robotics
* scientific experiments
* industrial monitoring

Video understanding remains computationally expensive.

---

# Audio Models

Some multimodal systems process:

* speech
* audio signals
* music

Tasks:

* transcription
* speech assistants
* audio retrieval
* multimodal interaction

---

# Context Windows in Multimodal Models

Images and multimodal embeddings consume context.

Consequences:

* higher memory usage
* larger inference cost
* more VRAM pressure

Multimodal inference is generally more expensive.

---

# GPU Requirements

Multimodal models often require:

* more VRAM
* more compute power
* larger context budgets

Vision encoders add additional computational overhead.

---

# Multimodal Models and RAG

Multimodal RAG systems may retrieve:

* text chunks
* images
* plots
* diagrams
* tables

This creates richer AI assistants.

---

# Vector Databases and Multimodal Data

Vector databases increasingly support:

* text embeddings
* image embeddings
* multimodal indexing

This enables unified retrieval architectures.

---

# Multimodal AI and Agents

Agents may interact with:

* screenshots
* GUIs
* visual environments
* cameras
* diagrams

Multimodal perception is essential for advanced autonomous systems.

---

# Multimodal Hallucinations

Multimodal systems may hallucinate:

* nonexistent objects
* incorrect visual relationships
* false interpretations

Grounding and retrieval remain important.

---

# Common Failure Modes

## Weak Visual Understanding

The model misinterprets images.

---

## OCR Errors

Text extraction becomes inaccurate.

---

## Context Saturation

Multimodal inputs consume excessive context.

---

## Hallucinated Visual Details

The model invents image content.

---

## GPU Exhaustion

Multimodal inference exceeds VRAM.

---

# Multimodal Model Trade-Offs

## Smaller Models

Advantages:

* lower VRAM
* faster inference

Disadvantages:

* weaker visual reasoning

---

## Larger Models

Advantages:

* stronger multimodal reasoning
* better visual understanding

Disadvantages:

* high memory usage
* slower inference

---

# Multimodal AI and Local Inference

Running multimodal systems locally enables:

* private image analysis
* offline visual assistants
* local scientific AI
* secure document understanding

This is increasingly important in:

* research
* healthcare
* enterprise systems

---

# Multimodal Infrastructure

Multimodal systems require:

* image pipelines
* embeddings systems
* vector databases
* GPU acceleration
* retrieval orchestration

They are substantially more complex than text-only systems.

---

# Mental Models

Useful mental models:

```text
Multimodal AI = AI that reasons across information types
```

```text
Vision-language models = Computer vision + LLM reasoning
```

```text
Multimodal embeddings = Shared semantic representation space
```

---

# Relationship with AI Systems Engineering

Understanding multimodal systems is essential for:

* advanced RAG systems
* scientific AI
* AI agents
* robotics
* document understanding
* retrieval systems
* autonomous systems

Multimodal AI connects:

```text
Perception
        with
Language reasoning
```

---

# Reflection

Multimodal models represent a major evolution in AI systems.

Instead of reasoning only over:

```text
Text
```

AI systems increasingly reason over:

* images
* documents
* diagrams
* videos
* structured data
* multimodal environments

This transition is critical for building:

* scientific assistants
* autonomous agents
* advanced RAG systems
* AI copilots
* real-world intelligent systems

because real-world information is fundamentally multimodal.
