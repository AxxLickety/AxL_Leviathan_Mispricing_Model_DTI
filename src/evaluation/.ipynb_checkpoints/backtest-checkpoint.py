# src/evaluation/backtest.py

import pandas as pd
import numpy as np


def compute_forward_return(df, horizon=12):
    out = df.copy()
    out["fwd_return"] = (
        out.groupby("region")["price"]
           .shift(-horizon) / out["price"] - 1
    )
    return out


def assign_quintiles(df, signal_col):
    out = df.copy()
    out["quintile"] = (
        out.groupby("date")[signal_col]
           .transform(lambda x: pd.qcut(x, 5, labels=False, duplicates="drop"))
    )
    return out


def directional_backtest(df, signal_col="score_xs", horizon=12):
    df = compute_forward_return(df, horizon=horizon)
    df = df.dropna(subset=["fwd_return", signal_col])
    df = assign_quintiles(df, signal_col)

    summary = (
        df.groupby("quintile")["fwd_return"]
          .mean()
          .to_frame("avg_fwd_return")
    )
    return summary

