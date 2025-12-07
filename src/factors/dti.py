import numpy as np
import pandas as pd


# ---------------------------------------------------------
# 1) Monthly mortgage payment (PMT formula)
# ---------------------------------------------------------
def compute_mortgage_payment(price, mortgage_rate, term_years=30):
    """
    Compute monthly mortgage payment using standard PMT formula.

    Parameters
    ----------
    price : float
        Median home price.
    mortgage_rate : float
        Annual mortgage rate (e.g., 0.05 for 5%).
    term_years : int
        Mortgage term in years.

    Returns
    -------
    float
        Monthly payment amount.
    """
    r = mortgage_rate / 12
    n = term_years * 12

    if r == 0:
        return price / n

    pmt = price * (r * (1 + r)**n) / ((1 + r)**n - 1)
    return pmt


# ---------------------------------------------------------
# 2) Compute DTI time series
# ---------------------------------------------------------
def compute_dti_series(price_series, income_series, mortgage_rate_series):
    """
    Compute Debt-to-Income (DTI) ratio over time.

    DTI = monthly mortgage payment / monthly income

    Parameters
    ----------
    price_series : pd.Series
        Median home price series.
    income_series : pd.Series
        Median household income series.
    mortgage_rate_series : pd.Series
        Mortgage rate series.

    Returns
    -------
    pd.Series
        DTI time series.
    """
    monthly_payments = []
    for p, r in zip(price_series, mortgage_rate_series):
        monthly_payments.append(compute_mortgage_payment(p, r))

    monthly_payments = pd.Series(monthly_payments, index=price_series.index)

    income = income_series.replace(0, np.nan)

    dti = monthly_payments / (income / 12)
    return dti


# ---------------------------------------------------------
# 3) Compute DTI shock (z-score)
# ---------------------------------------------------------
def compute_dti_shock(dti_series, window=None):
    """
    Compute standardized DTI shock.

    Parameters
    ----------
    dti_series : pd.Series
        DTI time series.
    window : int, optional
        Rolling window for z-score. If None, use full-sample z-score.

    Returns
    -------
    pd.Series
        Standardized DTI shock series.
    """
    if window is None:
        return (dti_series - dti_series.mean()) / dti_series.std()

    mean = dti_series.rolling(window).mean()
    std = dti_series.rolling(window).std()
    return (dti_series - mean) / std

