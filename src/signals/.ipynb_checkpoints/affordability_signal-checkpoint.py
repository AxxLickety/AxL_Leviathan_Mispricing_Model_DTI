import pandas as pd
import numpy as np


def build_affordability_signal(
    df: pd.DataFrame,
    weights: dict | None = None
) -> pd.DataFrame:
    """
    Build cross-sectional affordability signal.

    Higher score_xs = more affordable (expected higher future return)

    Required columns:
        dti
        pti
        rent_burden
        supply_pressure
        migration_pressure
    """

    out = df.copy()

    # -----------------------------
    # 1. Cross-sectional ranks (by date)
    # -----------------------------
    out["dti_z"] = out.groupby("date")["dti"].rank(pct=True)
    out["pti_z"] = out.groupby("date")["pti"].rank(pct=True)
    out["rent_burden_z"] = out.groupby("date")["rent_burden"].rank(pct=True)

    out["supply_pressure_z"] = out.groupby("date")["supply_pressure"].rank(pct=True)
    out["migration_pressure_z"] = out.groupby("date")["migration_pressure"].rank(pct=True)

    # -----------------------------
    # 2. Default weights (fund-style, interpretable)
    # -----------------------------
    if weights is None:
        weights = {
            "dti_z": -0.30,
            "pti_z": -0.25,
            "rent_burden_z": -0.20,
            "supply_pressure_z": +0.15,
            "migration_pressure_z": -0.10,
        }

    # -----------------------------
    # 3. Composite affordability score
    # -----------------------------
    out["score_xs"] = 0.0
    for k, w in weights.items():
        out["score_xs"] += w * out[k]

    return out


