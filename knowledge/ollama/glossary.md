# Glossary

## AI Agent

A software system that uses AI models together with tools, memory, retrieval, and decision-making workflows to perform tasks autonomously or semi-autonomously.

---

## ANN (Approximate Nearest Neighbor)

A retrieval technique used in vector databases to perform fast similarity search over high-dimensional embeddings.

ANN trades exact accuracy for retrieval speed and scalability.

---

## API

Application Programming Interface.

A mechanism that allows software systems to communicate with each other.

Example:

```text
FastAPI → Ollama API → Local Model
```

---

## Attention

The mechanism used by transformers to relate tokens to each other.

Attention enables LLMs to reason over context.

---

## Autoregressive Generation

Generation process where each generated token becomes part of the next input.

LLMs typically generate text token-by-token autoregressively.

---

## Backend

The server-side part of an application.

In local AI systems, the backend often orchestrates:

* retrieval
* prompts
* APIs
* model inference

---

## Batch Processing

Processing multiple requests simultaneously to improve throughput and GPU utilization.

---

## Chunk

A smaller piece of a document used for embeddings and retrieval.

Chunking is fundamental in RAG systems.

---

## Chunking

The process of splitting documents into smaller semantic units for embeddings and retrieval.

---

## Collection

A vector storage structure in Qdrant.

A collection contains:

* vectors
* payloads
* indexes
* metadata

---

## Context Window

The maximum number of tokens a model can process simultaneously.

The context window acts as the model's temporary working memory.

---

## Context Engineering

The process of optimizing how information is assembled into the model context.

Includes:

* retrieval
* reranking
* chunk selection
* summarization
* prompt assembly

---

## CPU Offloading

Moving part of the model computation or tensors from GPU VRAM to CPU RAM.

Allows larger models to run but reduces performance.

---

## Embedding

A numerical vector representation of semantic meaning.

Embeddings enable semantic search and vector retrieval.

---

## Embeddings Model

A model specialized in generating embeddings instead of conversational text.

Examples:

* bge-m3
* nomic-embed-text
* mxbai-embed-large

---

## Fine-Tuning

Training a pretrained model further on specialized data.

Fine-tuning modifies model weights.

---

## Frontend

The user-facing part of an application.

Example:

```text
Streamlit UI
```

---

## GPU

Graphics Processing Unit.

The primary hardware used for accelerating AI inference and training.

---

## Grounding

Constraining model outputs using retrieved or verified information.

RAG systems improve grounding.

---

## Hallucination

A generated statement unsupported by evidence or reality.

Hallucinations are one of the central reliability problems in AI systems.

---

## Health Check

A mechanism for verifying whether a service is operational.

Example:

```text
GET /health
```

---

## Hybrid Search

Combining:

* vector search
* keyword search
* metadata filtering

to improve retrieval quality.

---

## Inference

The process of running a model to generate outputs.

Inference is different from training.

---

## Ingestion Pipeline

The system responsible for:

* loading documents
* chunking
* embedding generation
* vector storage

before retrieval becomes possible.

---

## Instruction Following

The ability of a model to obey prompts and behavioral constraints.

---

## KV Cache

Memory structure storing attention states from previous tokens.

Improves generation efficiency.

KV cache size grows with context length.

---

## Latency

The delay between a request and a response.

Important latency metrics include:

* TTFT
* retrieval latency
* API response time

---

## LLM (Large Language Model)

A transformer-based neural network trained on massive text corpora to generate and understand language.

---

## Local AI

AI systems running on local hardware rather than external cloud APIs.

---

## Localhost

The local machine network address.

Typically:

```text
127.0.0.1
```

---

## LoRA

Low-Rank Adaptation.

A lightweight fine-tuning method that modifies only small adapter layers.

---

## Metadata

Additional structured information attached to documents or vectors.

Examples:

* experiment ID
* source file
* timestamp
* document type

---

## Model Serving

Exposing a model through an interface such as an API.

---

## Modelfile

An Ollama configuration file describing:

* base model
* prompts
* templates
* parameters
* adapters

---

## MoE (Mixture of Experts)

A neural architecture where only subsets of the model activate for each token.

Improves efficiency scaling.

---

## Multimodal Model

A model capable of processing multiple modalities.

Examples:

* text + image
* audio + text

---

## Observability

The ability to inspect and understand internal system behavior.

---

## Ollama

A local AI runtime for downloading, managing, and serving language models locally.

---

## Payload

Metadata and associated content attached to a vector inside a vector database.

---

## Prompt

The input provided to a language model.

May include:

* instructions
* retrieved context
* user query
* conversation history

---

## Prompt Engineering

Designing prompts to shape model behavior.

---

## Prompt Injection

An attack where malicious instructions attempt to override intended model behavior.

---

## Prompt Leakage

Exposure of hidden prompts or internal instructions.

---

## Quantization

Reducing numerical precision of model weights to reduce memory usage and improve efficiency.

Examples:

* Q4
* Q5
* Q8

---

## Qdrant

A vector database optimized for semantic search and RAG systems.

---

## RAG (Retrieval-Augmented Generation)

An architecture combining:

* retrieval
* language generation

The model retrieves external context before generating responses.

---

## Reranking

Reordering retrieved chunks to improve relevance.

Usually performed after initial vector retrieval.

---

## Retrieval

The process of finding relevant information from external memory systems.

---

## Semantic Search

Searching based on meaning rather than exact keyword matching.

---

## Similarity Search

Retrieving vectors close to a query vector in embedding space.

---

## Streaming

Returning generated tokens incrementally instead of waiting for the full response.

---

## Structured Output

A response following a predefined structure.

Examples:

* JSON
* XML
* markdown tables

---

## System Prompt

A high-priority instruction controlling model behavior.

---

## Temperature

A parameter controlling sampling randomness during generation.

Lower temperature:

* more deterministic

Higher temperature:

* more creative

---

## Token

A unit of text processed by language models.

Tokens are not necessarily words.

---

## Tokens Per Second (TPS)

A performance metric measuring generation speed.

---

## Top-K Sampling

Sampling method restricting generation to the K most probable tokens.

---

## Top-P Sampling

Sampling method restricting generation to tokens whose cumulative probability reaches a threshold.

---

## Tracing

Following a request across multiple system components.

---

## Transformer

The neural architecture underlying most modern language models.

Based heavily on self-attention mechanisms.

---

## Vector Database

A database optimized for storing and retrieving embeddings vectors.

---

## Vector Search

Searching embeddings space using similarity metrics.

---

## VRAM

Video RAM.

GPU memory used for storing:

* model weights
* KV cache
* tensors
* activations

VRAM is often the main constraint in local AI systems.

---

## WebSocket

A protocol enabling real-time bidirectional communication between frontend and backend systems.

Useful for streaming AI responses.

---

## Zero-Shot

Performing tasks without task-specific training examples.

LLMs often exhibit strong zero-shot capabilities.
