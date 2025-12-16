import xgboost as xgb

def train_xgboost(X_train, y_train):
    model = xgb.XGBRegressor(
        n_estimators=500,
        max_depth=6,
        learning_rate=0.05
    )
    model.fit(X_train, y_train)
    return model
