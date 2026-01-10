# 📌 Mentor Reading Guide — Leviathan Project

> *Suggested reading path (10–15 minutes total)*

This repository documents a research project on **macro-aware decision-making in housing markets**, with a focus on **how and when to allocate exposure under regime uncertainty**, rather than pure return maximization.

Given time constraints, the following reading order is recommended.

---

## 1. Project Overview (Start Here)

📁 `notebooks/00_readme/`  
📄 `00_project_overview.ipynb`

This notebook provides:
- the core research question,
- data scope and region universe,
- high-level methodology,
- and a summary of key findings.

It is designed to be readable without diving into implementation details.

---

## 2. Signal & Mechanism Development (Optional, Context)

📁 `notebooks/02_signal_research/`  
📄 `01–04_phase4_to_phase7_*.ipynb`

These notebooks document the **research evolution**, including:
- construction of affordability-based signals,
- regime definitions,
- robustness across regions,
- and early attempts at adaptive allocation.

They explain *why* the project ultimately moves toward a decision-layer framework, but are not required to understand the final contribution.

---

## 3. Core Contribution: Decision Layer (Recommended)

📁 `notebooks/03_decision_layer/`

- **`phase9_oos_decision.ipynb`**  
  *Out-of-sample decision robustness and stress validation*  
  Demonstrates that macro-aware gating improves decision stability under regime transitions.

- **`phase10_decision_surface.ipynb`**  
  *Decision surface learning*  
  Replaces binary rules with a learned, interpretable decision surface, showing substantial volatility compression and improved risk-adjusted behavior out-of-sample.

These two notebooks represent the **main research contribution**.

---

## 4. Supporting Code (Appendix)

📁 `src/`

The `src/` directory contains reusable loaders, factor construction, and evaluation utilities.  
It is provided for reproducibility rather than primary reading.

---

## One-Sentence Summary

> *Rather than asking “Can we predict returns?”, this project asks  
> “When should we avoid acting under macro stress?”  
> and shows that a learned decision surface can materially improve decision quality out-of-sample.*

