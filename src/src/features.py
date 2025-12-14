import pandas as pd
import numpy as np

def add_lag_features(df, col="sales", lags=[1,7,14]):
    for lag in lags:
        df[f"{col}_lag_{lag}"] = df[col].shift(lag)
    return df

def add_rolling_features(df, col="sales", windows=[7,14]):
    for w in windows:
        df[f"{col}_roll_mean_{w}"] = df[col].rolling(w).mean()
    return df

def add_fourier_terms(df, period=7, order=3):
    t = np.arange(len(df))
    for k in range(1, order+1):
        df[f"sin_{k}"] = np.sin(2*np.pi*k*t/period)
        df[f"cos_{k}"] = np.cos(2*np.pi*k*t/period)
    return df
