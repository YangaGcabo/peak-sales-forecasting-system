from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarimax(train):
    model = SARIMAX(
        train["sales"],
        order=(1,1,1),
        seasonal_order=(1,1,1,7),
        enforce_stationarity=False
    )
    return model.fit(disp=False)

def forecast_sarimax(model, steps):
    return model.forecast(steps)
