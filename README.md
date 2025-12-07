# Leviathan Model  
A Structural Affordability Signal for U.S. Housing Mispricing  
Author: Axl Ma  
Status: v0.1 (Research Baseline)

---

## 1. Executive Summary

The **Leviathan Model** is a research-grade factor framework designed to measure  
**structural affordability shocks** in the U.S. housing market and evaluate  
their predictive power for **housing-related asset returns**.

This repository contains the **baseline metro-level model**, which will  
eventually scale into a **ZIP-level cross-sectional alpha signal** capable of  
capturing migration pressure, supply constraints, and sentiment dispersion.

This is a **clean, fund-style codebase** intended for rigorous quant review.

---

## 2. High-Level Architecture

             ┌──────────────────────┐
             │   Raw Housing Data    │
             │  (prices, income,     │
             │   rent, mortgage)     │
             └──────────┬────────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │  Data Cleaning &     │
             │  Frequency Alignment │
             └──────────┬────────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Affordability Factor │
             │ = f(price, income,   │
             │     rates, rent)     │
             └──────────┬────────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │   Z-scoring &        │
             │   Normalization      │
             └──────────┬────────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Merge with ETF Rets  │
             │ (VNQ, IYR, XHB)      │
             └──────────┬────────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │  Backtesting Engine  │
             │  (timing rules, LS)  │
             └──────────┬────────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │ Performance Metrics   │
             │ (Sharpe, t-stat, vol) │
             └──────────────────────┘

---

## 3. Research Goals (What This Repo Delivers)

### 🎯 Short-Term Baseline (This Repo)
- Construct a **metro-level affordability factor**  
- Visualize its behavior over time  
- Test simple **long–short timing strategies**  
- Provide clean scatter/rolling correlation diagnostics  
- Produce summary statistics (Sharpe, t-stat, return, vol)

### 🚀 Medium-Term Extensions (Upcoming)
- Migration shift-share shocks  
- ZIP-level cross-sectional signal  
- Zoning restrictiveness & supply elasticity  
- Developer margins + cost shocks  
- Permit-cycle lag structures  

This baseline is intentionally simple: it’s the foundation for a scalable model.

---

## 4. Repository Structure



---

## 5. Running the Baseline

### Install minimal dependencies:

### Open the main notebook:

You will get:

- factor construction  
- merged return panel  
- backtests  
- visuals  
- summary performance stats  

---

## 6. Design Philosophy

This project is built under the assumption that the reader is a  
**professional quant researcher**.

So the code follows these principles:

- No obscure dependencies  
- Everything reproducible end-to-end  
- Clear function docstrings + modular design  
- Matplotlib only (no seaborn)  
- Consistent naming so later ZIP-level expansion is trivial  

---

## 7. Roadmap

**v0.2**  
- Automate FRED download pipeline  
- Add proper benchmark unified return panel  
- Improve factor refinements (income smoothing, rent trend filters)

**v0.3**  
- ZIP-level data ingestion pipeline  
- Migration shock instrument  
- First cross-sectional prototype  

**v1.0**  
- Full institutional-grade ZIP-level signal  
- Factor orthogonalization  
- Portfolio simulation engine  

---

## 8. Attribution

© Axl Ma  
Independent research project toward a  
**fund-grade structural real estate alpha model**.


