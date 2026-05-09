# LLMs and Context

---

# What is an LLM?

LLM stands for:

```text
Large Language Model
```

An LLM is a neural network trained to predict the next token in a sequence.

At a fundamental level, language generation works like this:

```text
previous tokens
        ↓
predict next token
```

This process is repeated iteratively until the response is complete.

---

# Tokens

LLMs do not process raw text directly.

They process:

```text
tokens
```

A token is a small unit of text.

Examples:

```text
"hello"
```

may become:

```text
["hel", "lo"]
```

or:

```text
[15496]
```

depending on the tokenizer.

Tokens can represent:

* words
* parts of words
* punctuation
* symbols
* spaces

---

# Context Window

The context window is the amount of tokens the model can see at once.

The model can only reason using:

* the current prompt
* the tokens inside the context window

Everything outside the context window is invisible to the model.

---

# Why Context Matters

LLMs do not have persistent memory by default.

The model only knows:

```text
what exists inside the current context
```

This is one of the most important concepts in modern AI systems.

If information is not present in the context:

* the model cannot directly reason over it
* the model may hallucinate
* the model may answer incorrectly

---

# Example

Suppose a model has a context window of:

```text
128k tokens
```

If your documents contain:

```text
5 million tokens
```

The model cannot read everything simultaneously.

This creates a major scalability problem.

---

# Why RAG Exists

RAG exists largely because context windows are limited.

Instead of inserting all documents into the prompt:

```text
all knowledge
```

RAG retrieves only:

```text
relevant knowledge
```

for the current query.

---

# LLM Memory is Not Real Memory

A very common misconception:

```text
LLMs do not truly remember information like humans do
```

The model operates using:

* patterns learned during training
* current prompt context

Once the context disappears:

```text
the information disappears too
```

unless external memory systems are used.

---

# Types of Memory in AI Systems

## 1. Parametric Memory

Knowledge stored inside model weights.

Learned during training.

Examples:

* general world knowledge
* language patterns
* reasoning patterns

---

## 2. Contextual Memory

Information temporarily present inside the context window.

Examples:

* retrieved documents
* user instructions
* conversation history

---

## 3. External Memory

Information stored outside the model.

Examples:

* vector databases
* files
* APIs
* retrieval systems
* long-term memory systems

RAG mainly works with external memory.

---

# The Context Bottleneck

One of the biggest limitations of LLMs is:

```text
finite context capacity
```

Even very large models cannot:

* read infinite documents
* process entire databases at once
* load huge scientific datasets fully into memory

This creates the need for:

* retrieval systems
* chunking
* ranking
* context selection

---

# Context Injection

RAG systems work by injecting retrieved information into the prompt.

Typical structure:

```text
System Instructions
        ↓
Retrieved Context
        ↓
User Query
```

The model then reasons using the injected context.

---

# Prompt Construction

Prompt construction is critical in RAG systems.

The prompt must:

* include relevant context
* avoid unnecessary context
* remain within token limits
* preserve important information

Poor prompt construction can degrade performance significantly.

---

# Context Overload

More context is not always better.

If too much irrelevant information is inserted:

* retrieval quality decreases
* reasoning quality decreases
* hallucinations may increase
* latency increases
* costs increase

This problem is called:

```text
context overload
```

Good retrieval systems try to maximize:

```text
signal / noise ratio
```

inside the prompt.

---

# Hallucinations and Missing Context

Hallucinations often happen because:

* the model lacks necessary information
* the retrieval system failed
* context is incomplete
* context is ambiguous

Without grounding, the model may generate plausible but false answers.

---

# Retrieval as Dynamic Context Selection

A useful mental model:

RAG is essentially:

```text
smart context selection
```

The retrieval system decides:

```text
what information deserves to enter the context window
```

---

# Attention Mechanism

Modern LLMs use transformers.

Transformers rely heavily on:

```text
self-attention
```

Self-attention allows tokens to interact with other tokens inside the context window.

Very simplified idea:

```text
which tokens are important for understanding other tokens?
```

This is one reason why context size strongly affects:

* reasoning
* coherence
* retrieval quality

---

# Long Context Models

Modern models support increasingly large context windows.

Examples:

* 8k tokens
* 32k tokens
* 128k tokens
* 1M+ tokens

However:

larger context windows do not eliminate the need for retrieval.

Why?

Because:

* large prompts are expensive
* retrieval is more scalable
* irrelevant context hurts performance
* databases can be much larger than context windows

---

# Context Compression

Many advanced systems use:

```text
context compression
```

instead of inserting raw documents directly.

Examples:

* summarization
* reranking
* filtering
* chunk selection
* compression models

Goal:

```text
maximize useful information density
```

inside the prompt.

---

# Conversation Context

Chat systems also rely on context windows.

Conversation history consumes tokens.

Long conversations may cause:

* forgotten information
* truncated history
* degraded reasoning

This is why many AI systems implement:

* memory systems
* summarization
* retrieval over conversations

---

# Scientific Context Problems

Scientific systems are especially difficult because:

* datasets are large
* documents are dense
* information is fragmented
* numerical details matter
* plots and tables are important

Scientific RAG systems must retrieve:

* precise information
* relevant experiments
* numerical metrics
* contextual evidence

without overwhelming the context window.

---

# Context in This Project

For optical turbulence experiments, context may include:

```text
metadata.json
analysis.json
comparison results
paper excerpts
plots
scientific notes
```

The retrieval system must decide:

* which experiments are relevant
* which metrics matter
* which chunks should enter the prompt

The LLM then reasons over the selected context.

---

# Key Insight

A modern AI system is not only:

```text
an LLM
```

It is often:

```text
LLM
+
retrieval
+
memory
+
context management
```

The quality of the system depends heavily on how context is selected, organized, compressed, and injected into the model.
