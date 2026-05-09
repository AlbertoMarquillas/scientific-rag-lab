# Evaluation

---

# What is Evaluation?

Evaluation is the process of measuring how well a RAG system performs.

A RAG system may appear convincing while still being:

* incorrect
* hallucinated
* poorly grounded
* semantically weak
* unreliable

Evaluation is essential because:

```text
good-looking answers are not necessarily good answers
```

---

# Why Evaluation Matters

RAG systems are complex pipelines.

Many stages can fail:

* chunking
* embeddings
* retrieval
* reranking
* prompt construction
* generation

Evaluation helps identify:

```text
where failures occur
```

inside the pipeline.

---

# What Should Be Evaluated?

A modern RAG system usually requires evaluation of:

* retrieval quality
* grounding quality
* factual correctness
* reasoning quality
* hallucinations
* latency
* robustness
* scalability
* user usefulness

---

# Evaluation Levels

RAG evaluation is usually divided into:

## 1. Retrieval Evaluation

Measures:

```text
Did the system retrieve the correct information?
```

---

## 2. Generation Evaluation

Measures:

```text
Did the model generate a correct grounded answer?
```

---

## 3. End-to-End Evaluation

Measures:

```text
Did the full system solve the task correctly?
```

---

# Retrieval Evaluation

Retrieval quality is fundamental.

Even excellent LLMs fail if retrieval fails.

Typical retrieval metrics:

* Precision@K
* Recall@K
* MRR
* NDCG

---

# Precision@K

Measures:

```text
how many retrieved results are relevant
```

Example:

```text
Top-5 retrieval
```

If:

```text
4 of 5 chunks are relevant
```

then:

genui{"math_block_widget_always_prefetch_v2":{"content":"Precision@5=\frac{4}{5}=0.8"}}

High precision means:

* low retrieval noise
* cleaner prompts

---

# Recall@K

Measures:

```text
how much relevant information was retrieved
```

Example:

If:

```text
8 relevant chunks exist
```

and the system retrieves:

```text
6
```

then:

genui{"math_block_widget_always_prefetch_v2":{"content":"Recall=\frac{6}{8}=0.75"}}

High recall reduces:

* missing information
* incomplete answers

---

# Precision vs Recall

There is usually a tradeoff.

High precision:

* less noise
* more focused retrieval

High recall:

* lower risk of missing information

Good systems balance both.

---

# MRR — Mean Reciprocal Rank

Measures:

```text
how early the first relevant result appears
```

Formula:

genui{"math_block_widget_always_prefetch_v2":{"content":"MRR=\frac{1}{N}\sum_{i=1}^{N}\frac{1}{rank_i}"}}

Higher MRR means:

* relevant chunks appear earlier
* retrieval ranking is stronger

---

# NDCG

NDCG stands for:

```text
Normalized Discounted Cumulative Gain
```

Measures:

```text
ranking quality considering relevance order
```

Useful for:

* graded relevance
* ranking optimization
* retrieval quality analysis

---

# Generation Evaluation

Generation evaluation focuses on:

```text
answer quality
```

Important questions:

* Is the answer correct?
* Is it grounded?
* Does it hallucinate?
* Does it use retrieved context properly?
* Is reasoning coherent?

---

# Groundedness

Groundedness measures:

```text
how strongly the answer is supported by retrieved evidence
```

A grounded answer should:

* rely on retrieved context
* avoid unsupported claims
* avoid fabricated information

---

# Faithfulness

Faithfulness measures:

```text
whether the answer remains faithful to retrieved information
```

A response may sound convincing while:

* distorting evidence
* inventing relationships
* exaggerating conclusions

Faithfulness is critical in scientific systems.

---

# Hallucination Evaluation

Hallucinations are one of the biggest challenges in RAG systems.

Evaluation should measure:

* fabricated claims
* unsupported reasoning
* invented citations
* false numerical values

Hallucinations may occur because of:

* weak retrieval
* poor prompting
* ambiguous context
* incomplete evidence

---

# Context Usage Evaluation

Important question:

```text
Did the model actually use the retrieved context?
```

Some systems retrieve correct information but:

* ignore it
* misuse it
* partially use it

This reduces grounding quality.

---

# Human Evaluation

Many RAG systems still require:

```text
human evaluation
```

Humans may assess:

* correctness
* usefulness
* clarity
* grounding
* scientific validity

Human evaluation is expensive but very valuable.

---

# Automatic Evaluation

Automatic evaluation uses:

* metrics
* scoring systems
* LLM judges
* benchmark datasets

Advantages:

* scalable
* repeatable
* fast

Disadvantages:

* imperfect
* may miss subtle failures

---

# LLM-as-a-Judge

Modern systems sometimes use:

```text
one LLM to evaluate another LLM
```

Possible evaluations:

* factuality
* relevance
* faithfulness
* coherence
* grounding

This approach is increasingly common.

---

# Benchmark Datasets

Some systems are evaluated using benchmark tasks.

Examples:

* question answering
* retrieval benchmarks
* scientific QA
* domain-specific datasets

Benchmarks help compare systems objectively.

---

# Latency Evaluation

Evaluation is not only about correctness.

Performance matters too.

Important metrics:

* retrieval latency
* embedding latency
* generation latency
* total response time

Production systems often require:

```text
low-latency retrieval
```

---

# Cost Evaluation

Modern RAG systems may be expensive.

Costs include:

* embedding generation
* vector storage
* retrieval
* LLM inference
* reranking

Evaluation should consider:

```text
quality vs cost
```

---

# Robustness Evaluation

Good systems should remain stable under:

* ambiguous queries
* noisy documents
* missing context
* adversarial prompts
* retrieval failures

Robustness is especially important in production.

---

# End-to-End Evaluation

Ultimately, users care about:

```text
whether the full system works
```

End-to-end evaluation measures:

* task success
* answer usefulness
* retrieval quality
* generation quality
* overall user experience

---

# Scientific RAG Evaluation

Scientific systems require especially strict evaluation.

Important criteria:

* factual accuracy
* numerical correctness
* grounding
* citation quality
* evidence consistency
* scientific reliability

Small hallucinations may become very dangerous.

---

# Evaluation in This Project

Potential evaluation targets:

* retrieval of correct experiments
* turbulence regime identification
* similarity search quality
* metadata filtering accuracy
* grounding quality
* numerical consistency
* scientific usefulness

Potential future evaluation tasks:

```text
"Did the system retrieve experiments
with actually similar turbulence behavior?"
```

---

# Common Evaluation Failures

## Evaluating Only Generation

Good responses may hide retrieval failures.

---

## Ignoring Retrieval Quality

Weak retrieval causes poor grounding.

---

## Evaluating Only Accuracy

Useful systems also require:

* robustness
* latency
* scalability
* interpretability

---

## Ignoring Hallucinations

A fluent answer is not necessarily trustworthy.

---

# Observability and Evaluation

Modern AI systems often integrate:

* tracing
* retrieval logs
* prompt inspection
* context analysis
* response scoring

This improves debugging and optimization.

---

# Continuous Evaluation

Production systems often require:

```text
continuous evaluation
```

Why?

Because:

* embeddings change
* documents evolve
* retrieval behavior shifts
* prompts change
* models update

Evaluation is not a one-time process.

---

# Key Insight

Evaluation is fundamentally:

```text
measurement of reliability
```

A RAG system should not only:

* sound convincing

It should also be:

* grounded
* correct
* robust
* explainable
* scientifically reliable

Modern RAG systems require evaluating:

```text
retrieval
+
generation
+
full pipeline behavior
```

rather than only the final answer.
