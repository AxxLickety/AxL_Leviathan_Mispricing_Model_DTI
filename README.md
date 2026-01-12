# Leviathan — Phase 1  
## Regime-Dependent Housing Affordability Risk

**Leviathan** is a research project exploring **mispricing and risk dynamics in housing markets** using regime-aware factor analysis.

This repository contains **Phase 1**, which focuses on **diagnostics and validation**, not trading or deployment.

---

## Phase 1 Objective

Phase 1 is designed to answer a single question:

> **Does an affordability-based housing risk signal behave differently across macro regimes?**

Rather than assuming a factor works universally, this phase tests **when the signal is informative and when it should be ignored**.

---

## Key Finding (Phase 1)

- The affordability risk factor shows **strong explanatory power in down regimes**
- Signal strength becomes **weak or near-zero in up regimes**
- This indicates clear **regime dependence**, not a stable unconditional alpha

**Interpretation:**  
The factor is better suited as a **risk filter in contractionary environments**, rather than a general-purpose return signal.

---

## 📊 Phase 1 Report (HTML)

👉 **Open the full Phase 1 summary:**  
**https://axxlickety.github.io/AxL_Leviathan_Mispricing_Model_DTI/**

The report includes:
- Factor construction overview  
- Regime-based IC analysis  
- Rolling IC diagnostics  
- Cross-region robustness checks  

---

## What This Is / Is Not

**This is:**
- A validated **diagnostic stage** for regime-aware modeling  
- An empirical study of **signal stability and failure modes**

**This is not:**
- A finished trading strategy  
- A production-ready model  
- An optimized alpha signal  

Phase 1 deliberately avoids overfitting or deployment claims.

---

## Repository Structure

- `docs/`  
  - `PHASE1_SUMMARY.html` — Full HTML report  
  - `index.html` — Redirect entry point for GitHub Pages

Model development, data pipelines, and experiments are maintained separately in a private research repository.

---

## Next Steps (Phase 2)

Planned extensions include:
- Regime-conditioned factor construction  
- Cross-regional stability testing  
- Controlled out-of-sample evaluation  
- Explicit separation of risk filtering vs. return forecasting roles

---

## Status

Phase 1 is **complete**.  
This repository is intended as a **clean, public research artifact** for review and discussion.
