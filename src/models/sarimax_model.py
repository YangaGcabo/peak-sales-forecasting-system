from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarimax(series, order=(1,1,1), seasonal_order=(1,1,1,52)):
    model = SARIMAX(
        series,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    results = model.fit(disp=False)
    return results
