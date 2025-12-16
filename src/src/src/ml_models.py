import lightgbm as lgb
import xgboost as xgb

def train_lightgbm(X, y):
    model = lgb.LGBMRegressor(
        n_estimators=500,
        learning_rate=0.05
    )
    model.fit(X, y)
    return model

def train_xgboost(X, y):
    model = xgb.XGBRegressor(
        n_estimators=500,
        learning_rate=0.05
    )
    model.fit(X, y)
    return model
