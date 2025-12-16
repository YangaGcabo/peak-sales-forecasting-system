from prophet import Prophet
import pandas as pd

def train_prophet(df):
    df = df.rename(columns={"date": "ds", "sales": "y"})
    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        changepoint_prior_scale=0.1
    )
    model.fit(df)
    return model
