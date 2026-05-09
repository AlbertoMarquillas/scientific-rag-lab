# Scientific RAG

---

# What is Scientific RAG?

Scientific RAG is a retrieval-augmented generation system designed for scientific and technical knowledge.

Unlike general-purpose RAG systems, Scientific RAG must work with:

* papers
* experiments
* numerical results
* equations
* plots
* tables
* metadata
* laboratory notes
* datasets
* code outputs

The goal is not only to answer questions, but to support evidence-based scientific reasoning.

---

# Why Scientific RAG is Different

Scientific information is usually:

* dense
* technical
* structured
* multimodal
* numerical
* evidence-dependent
* highly contextual

A scientific RAG system must preserve meaning, precision, and traceability.

This makes it more demanding than a simple document chatbot.

---

# Core Objective

The core objective of Scientific RAG is:

```text
retrieve the right scientific evidence
+
reason over it carefully
+
produce grounded explanations
```

A scientific RAG system should avoid unsupported claims and clearly distinguish between:

* retrieved facts
* calculations
* interpretations
* uncertainty
* hypotheses

---

# Scientific Knowledge Sources

Scientific RAG may use many types of sources:

* research papers
* books
* technical reports
* experiment metadata
* analysis outputs
* plots and figures
* tables
* laboratory notes
* simulation results
* source code
* datasets

---

# Why Papers Alone Are Not Enough

Many RAG demos focus only on papers or PDFs.

Scientific work often requires more than literature retrieval.

A real scientific system may need to connect:

```text
papers
+
experiments
+
measurements
+
figures
+
metadata
+
code
```

This is especially important in experimental research.

---

# Scientific Grounding

Scientific grounding means that answers should be supported by identifiable evidence.

Evidence may come from:

* a paper section
* an experiment result
* a table
* a plot
* a numerical metric
* a code output

The system should ideally show where each claim comes from.

---

# Traceability

Traceability is essential.

A scientific answer should be traceable back to:

```text
source file
experiment ID
analysis module
metric value
figure
paper section
```

Without traceability, scientific outputs become difficult to trust.

---

# Reproducibility

Scientific RAG should support reproducibility.

Important questions:

* Which data was used?
* Which analysis version generated the result?
* Which embedding model was used?
* Which retrieval configuration was used?
* Which prompt produced the answer?

Scientific systems must preserve enough information to reproduce conclusions.

---

# Numerical Precision

Scientific RAG must handle numbers carefully.

Common risks:

* altered values
* rounded incorrectly
* mixed units
* invented metrics
* invalid comparisons

Numerical values should usually come directly from retrieved sources or explicit calculations.

---

# Units

Scientific systems must preserve units.

Examples:

```text
nm
mm
m
m^{-2/3}
frames/s
µs
V
```

Losing or confusing units can make a scientific answer wrong.

---

# Equations

Scientific RAG may retrieve and use equations.

Important concerns:

* equation correctness
* variable definitions
* unit consistency
* validity assumptions
* regime limitations

The system should avoid applying equations outside their valid domain.

---

# Tables

Tables are common in scientific documents.

They require careful handling because:

* row-column relationships matter
* numerical precision matters
* headers are essential
* units may be in captions or column names

Tables may need special parsing or structured representation.

---

# Plots and Figures

Plots often contain essential scientific information.

They may represent:

* trends
* distributions
* comparisons
* temporal evolution
* spatial behavior
* experimental regimes

Scientific RAG should eventually retrieve and reason over figures, not only text.

---

# Multimodal Scientific Evidence

Scientific evidence is often distributed across modalities:

```text
text explanation
+
plot
+
table
+
metadata
+
raw data
```

Scientific RAG should connect these pieces rather than treating them as isolated artifacts.

---

# Scientific Chunking

Chunking is critical in scientific RAG.

Good scientific chunks should preserve:

* section context
* equations and definitions
* figure captions
* table headers
* experiment identifiers
* numerical relationships

Poor chunking may separate evidence from explanation.

---

# Scientific Metadata

Metadata is especially important.

Examples:

```text
paper_title
author
year
experiment_id
run_id
metric_name
unit
analysis_module
instrument
regime
```

Metadata enables structured retrieval and traceability.

---

# Scientific Retrieval

Scientific retrieval often requires combining:

```text
semantic retrieval
+
keyword search
+
metadata filtering
+
numerical filtering
```

Pure vector search is usually not enough.

---

# Numerical Retrieval

Scientific queries often include numerical constraints.

Examples:

```text
r0 < 3 mm
scintillation_index > 0.3
heater_voltage = 16 V
fps = 160
```

These are better handled using metadata or structured databases than pure embeddings.

---

# Hybrid Scientific Search

Scientific RAG usually benefits from hybrid search.

Dense retrieval helps with:

* concepts
* paraphrases
* semantic similarity

Sparse and structured retrieval help with:

* exact terms
* symbols
* IDs
* numerical values
* acronyms

---

# Scientific Reranking

Reranking can consider both semantic and physical relevance.

Example signals:

* textual similarity
* metric similarity
* regime similarity
* same instrument
* same analysis module
* similar experimental conditions

This is especially useful for experiment retrieval.

---

# Scientific Hallucinations

Scientific hallucinations are especially dangerous.

Examples:

* invented papers
* fake citations
* incorrect equations
* altered numerical values
* unsupported causal interpretations
* fabricated experimental conclusions

Scientific RAG must prioritize factual grounding over fluency.

---

# Uncertainty

Scientific systems should communicate uncertainty clearly.

Examples:

```text
The retrieved data supports this trend.
```

```text
The available evidence is insufficient to confirm this.
```

```text
This interpretation depends on the selected estimator.
```

Uncertainty is part of honest scientific reasoning.

---

# Evidence-Based Answers

A strong scientific answer should usually include:

* what was retrieved
* what the evidence says
* what can be concluded
* what cannot be concluded
* relevant limitations

This improves trust and reproducibility.

---

# Scientific Evaluation

Scientific RAG evaluation should measure:

* retrieval relevance
* numerical correctness
* faithfulness
* citation quality
* unit consistency
* hallucination rate
* usefulness for scientific tasks

Generic answer quality is not enough.

---

# Possible Scientific RAG Tasks

Examples:

```text
Find experiments showing strong scintillation.
```

```text
Retrieve papers related to beam wander.
```

```text
Compare turbulence regimes across experiments.
```

```text
Find runs with similar Rytov variance and beam morphology.
```

```text
Explain which metrics support a strong turbulence classification.
```

---

# Scientific RAG in This Project

This project is a natural Scientific RAG use case because it contains:

* optical turbulence experiments
* structured metadata
* HDF5 raw data
* analysis results
* physical metrics
* plots
* papers
* notes

The system can eventually connect experimental data with scientific interpretation.

---

# Data Sources in This Project

Potential sources:

```text
metadata.json
analysis.json
comparison results
results.json
scientific notes
paper PDFs
plots
preview videos
HDF5-derived descriptors
```

The first practical version should focus on processed and textual information before raw multimodal data.

---

# Recommended First Representation

A good starting point:

```text
metadata.json
+
analysis.json
+
scientific summary per experiment
```

This creates retrievable scientific summaries without directly embedding huge raw datasets.

---

# Experiment-Level Chunks

One useful chunk type:

```text
one experiment summary
```

Example content:

```text
Run ID, acquisition parameters, control voltages, main turbulence metrics, regime label, key observations.
```

Useful for:

* experiment retrieval
* regime search
* similarity search

---

# Module-Level Chunks

Another useful chunk type:

```text
one analysis module per experiment
```

Example:

```text
Module 40 — Optical Turbulence results for run X
```

Useful when users ask about specific metrics.

---

# Plot-Level Chunks

Future chunk type:

```text
one plot + caption + metadata + source path
```

Useful for:

* figure retrieval
* report generation
* visual evidence tracing

---

# HDF5 Data

Raw HDF5 files should usually not be embedded directly at the beginning.

Better pipeline:

```text
HDF5 raw frames
      ↓
feature extraction
      ↓
scientific descriptors
      ↓
summary + metadata
      ↓
retrieval
```

Raw data remains the source of truth, but retrieval operates over processed representations.

---

# Example Scientific Retrieval Pipeline

```text
Experiment Folder
      ↓
metadata.json + analysis.json
      ↓
Scientific Summary Builder
      ↓
Chunking
      ↓
Embeddings
      ↓
Qdrant Payloads
      ↓
Hybrid Retrieval
      ↓
Reranking
      ↓
Grounded Scientific Answer
```

---

# Example Query

```text
"Find experiments with high scintillation and large beam wander."
```

Possible retrieval logic:

```text
semantic query:
strong turbulence, scintillation, beam wander

metadata filters:
scintillation_index > threshold
beam_wander_rms > threshold
```

---

# Example Answer Structure

A scientific RAG answer could include:

```text
1. Retrieved experiments
2. Supporting metrics
3. Interpretation
4. Limitations
5. Source references
```

This keeps the response grounded and auditable.

---

# Scientific Assistant Vision

Long term, the system could act as a scientific assistant capable of:

* searching experiments
* comparing runs
* explaining metrics
* finding similar regimes
* connecting papers and experiments
* retrieving plots
* generating evidence-based summaries

---

# Limitations

Scientific RAG has important limitations:

* embeddings may miss numerical meaning
* figures require special handling
* equations may be misapplied
* retrieval can be incomplete
* scientific reasoning still needs validation
* human review remains important

Scientific RAG should assist researchers, not replace scientific judgment.

---

# Common Mistakes

## Treating Scientific RAG as PDF Chat

Scientific knowledge is broader than PDFs.

---

## Ignoring Units

Numerical answers become unreliable.

---

## Embedding Raw Data Too Early

Raw data often needs feature extraction first.

---

## No Traceability

Scientific claims become hard to verify.

---

## No Evaluation

The system may sound useful while being scientifically wrong.

---

# Recommended Development Path

Practical progression:

```text
1. Text RAG over notes and papers
2. Retrieval over metadata and analysis summaries
3. Experiment similarity search
4. Hybrid search with metric filters
5. Plot and figure retrieval
6. Multimodal retrieval
7. Agentic scientific workflows
```

This avoids unnecessary complexity at the start.

---

# Key Insight

Scientific RAG is not just:

```text
chat with papers
```

It is a system for connecting:

```text
scientific evidence
+
experimental data
+
retrieval
+
reasoning
+
traceability
```

For experimental research, its value comes from turning many fragmented artifacts into a searchable, interpretable, and evidence-grounded scientific knowledge system.
