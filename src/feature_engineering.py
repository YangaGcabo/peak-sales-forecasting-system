import numpy as np
import pandas as pd

def add_time_features(df):
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["dow"] = df["date"].dt.weekday
    return df

def add_lag_features(df, lags=[1,7,14]):
    for lag in lags:
        df[f"lag_{lag}"] = df["sales"].shift(lag)
    return df

def add_rolling_features(df):
    df["rolling_mean_7"] = df["sales"].rolling(7).mean()
    df["rolling_std_7"] = df["sales"].rolling(7).std()
    return df

def build_features(df):
    df = add_time_features(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    return df.dropna()
