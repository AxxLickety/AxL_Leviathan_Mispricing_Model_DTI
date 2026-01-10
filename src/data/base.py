# src/base.py
import pandas as pd

def validate_schema(df: pd.DataFrame, required_cols):
    """
    Ensure loader output has all required standardized columns.
    Raise ValueError if any required column is missing.
    """
    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df
