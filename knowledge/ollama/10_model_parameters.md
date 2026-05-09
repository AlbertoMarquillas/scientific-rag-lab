# Model Parameters

## Introduction

Large language models do not generate deterministic outputs by default.

Their behavior is controlled through:

```text
Inference parameters
```

These parameters influence:

* randomness
* creativity
* determinism
* repetition
* reasoning behavior
* response diversity
* latency
* memory usage

Understanding model parameters is essential for:

* prompt engineering
* RAG systems
* AI assistants
* scientific AI systems
* production AI deployment
* reproducibility

---

# What Are Model Parameters?

Model parameters are:

```text
Configuration values controlling inference behavior
```

These are NOT the neural network weights.

Instead, they affect:

* token selection
* sampling behavior
* context management
* generation strategy

The same model can behave very differently under different parameter settings.

---

# Core Idea

LLMs generate text by predicting probability distributions over possible next tokens.

Example conceptually:

```text
Next token probabilities:

"the"   → 0.42
"a"     → 0.21
"this"  → 0.09
```

Inference parameters influence:

```text
How the next token is selected
```

---

# Deterministic vs Stochastic Generation

## Deterministic Generation

Always produces the same output.

Advantages:

* reproducibility
* stable outputs
* reliable formatting

Disadvantages:

* repetitive
* less creative

---

## Stochastic Generation

Introduces randomness.

Advantages:

* creative outputs
* diverse responses
* natural language variability

Disadvantages:

* inconsistent outputs
* harder reproducibility

Inference parameters control this balance.

---

# Temperature

One of the most important parameters.

Temperature controls:

```text
Sampling randomness
```

---

## Low Temperature

Examples:

```text
0.0
0.1
0.2
```

Behavior:

* deterministic
* focused
* repetitive
* stable

Useful for:

* RAG
* scientific systems
* coding
* factual tasks

---

## High Temperature

Examples:

```text
0.8
1.0
1.2
```

Behavior:

* creative
* diverse
* less predictable
* exploratory

Useful for:

* brainstorming
* storytelling
* creative writing

---

# Top-K Sampling

Top-k restricts token selection to:

```text
The K most probable tokens
```

Example:

```text
top_k = 40
```

The model only samples among the 40 highest-probability candidates.

---

# Effects of Top-K

## Small Top-K

Behavior:

* focused
* conservative
* repetitive

---

## Large Top-K

Behavior:

* diverse
* exploratory
* less constrained

Top-k controls exploration breadth.

---

# Top-P Sampling

Top-p uses:

```text
Cumulative probability thresholding
```

Instead of fixed token count.

Example:

```text
top_p = 0.9
```

The model selects the smallest token set whose cumulative probability reaches 90%.

---

# Why Top-P Exists

Probability distributions vary dynamically.

Top-p adapts sampling based on:

* confidence
* uncertainty
* distribution shape

This often produces more natural outputs.

---

# Top-K vs Top-P

| Parameter | Restriction Type           |
| --------- | -------------------------- |
| Top-K     | Fixed number of candidates |
| Top-P     | Probability mass threshold |

Both reduce randomness in different ways.

---

# Repeat Penalty

Repeat penalty discourages repetition.

Without repetition control:

Models may:

* loop
* repeat phrases
* generate unstable outputs

Repeat penalty reduces repeated token probability.

---

# Presence Penalty

Presence penalty encourages topic diversity.

Tokens already used become less likely.

Useful for:

* brainstorming
* diverse generation
* long-form writing

---

# Frequency Penalty

Frequency penalty reduces repeated usage frequency.

Difference:

* presence penalty → whether token appeared
* frequency penalty → how often token appeared

---

# Maximum Tokens

This parameter limits:

```text
Maximum generated output length
```

Useful for:

* latency control
* cost control
* preventing runaway generation

---

# Stop Sequences

Stop sequences terminate generation when detected.

Useful for:

* structured outputs
* tool calling
* JSON generation
* agent workflows

---

# Context Size Parameter

Some runtimes expose:

```text
num_ctx
```

This controls:

```text
Maximum active context size
```

Larger contexts:

Advantages:

* more retrieval context
* longer conversations

Disadvantages:

* more VRAM usage
* slower inference

---

# Seed

The seed controls pseudo-random generation.

Using the same:

* model
* prompt
* parameters
* seed

may improve reproducibility.

Useful for:

* scientific workflows
* benchmarking
* evaluation

---

# Streaming Parameters

Streaming affects:

```text
How tokens are returned during generation
```

Streaming improves:

* responsiveness
* user experience
* real-time interaction

---

# System Prompts

System prompts strongly shape behavior.

Examples:

* assistant personality
* formatting rules
* role definitions
* safety instructions
* scientific constraints

System prompts are often as important as inference parameters.

---

# Parameter Interactions

Parameters interact with each other.

Example:

```text
High temperature + high top_k
```

may produce:

* chaotic outputs
* hallucinations
* unstable reasoning

Inference tuning is multidimensional.

---

# Parameter Tuning for RAG

RAG systems usually prefer:

* low temperature
* moderate top_p
* low randomness
* deterministic outputs

Reason:

```text
RAG prioritizes factual retrieval over creativity
```

---

# Parameter Tuning for Coding

Coding assistants often prefer:

* low temperature
* stable sampling
* reduced randomness

This improves:

* syntax stability
* reproducibility
* deterministic behavior

---

# Parameter Tuning for Creative Tasks

Creative systems may prefer:

* higher temperature
* larger top_k
* larger top_p

This increases output diversity.

---

# Parameter Tuning for Scientific AI

Scientific systems usually prioritize:

* factual stability
* reproducibility
* deterministic outputs
* controlled hallucinations

Typical settings:

* low temperature
* constrained sampling
* strong retrieval grounding

---

# Parameter Tuning and Hallucinations

High randomness may increase hallucinations.

Examples:

* high temperature
* large sampling spaces
* unrestricted generation

Controlled sampling often improves factual reliability.

---

# Parameter Tuning and Latency

Some parameters influence:

* generation length
* throughput
* inference cost

Long outputs increase:

* latency
* memory usage
* token processing time

---

# Parameter Presets

Different applications often use presets.

## Chat Assistant

Balanced randomness.

---

## Coding Assistant

Low randomness.

---

## Scientific Assistant

Highly constrained generation.

---

## Creative Writer

High diversity.

---

# Reproducibility Challenges

Even with fixed parameters:

* hardware differences
* runtime changes
* quantization
* parallel execution

may slightly alter outputs.

Scientific reproducibility remains difficult.

---

# Common Failure Modes

## Temperature Too High

Outputs become unstable.

---

## Temperature Too Low

Outputs become repetitive.

---

## Excessive Max Tokens

Long, unfocused responses.

---

## Weak Repetition Control

Looping behavior.

---

## Oversized Context

Latency and VRAM issues.

---

# Parameters and AI Agents

Agents often require:

* deterministic reasoning
* stable formatting
* tool-call consistency

This usually favors:

* lower temperature
* constrained sampling

Agent reliability strongly depends on parameter tuning.

---

# Parameters and Structured Outputs

Structured generation requires:

* controlled randomness
* stable formatting
* predictable outputs

Important for:

* JSON outputs
* APIs
* automation
* pipelines

---

# Mental Models

Useful mental models:

```text
Temperature = Creativity control
```

```text
Top-K / Top-P = Exploration boundaries
```

```text
Inference parameters = Behavioral configuration layer
```

---

# Relationship with AI Systems Engineering

Understanding model parameters is essential for:

* RAG engineering
* AI deployment
* scientific AI systems
* prompt engineering
* AI agents
* inference optimization
* reproducibility

Parameter tuning bridges:

```text
Neural network probabilities
        with
Application behavior
```

---

# Reflection

Inference parameters are one of the key mechanisms through which developers shape AI behavior.

The same underlying model can behave as:

* a deterministic scientific assistant
* a coding copilot
* a creative storyteller
* a structured API generator
* a retrieval-grounded RAG system

simply by changing inference configuration.

Understanding parameters is therefore essential for moving from:

```text
Using models
```

to:

```text
Engineering AI behavior
```

inside real AI systems.
