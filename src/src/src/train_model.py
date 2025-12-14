import lightgbm as lgb

def train_model(X_train, y_train):
    model = lgb.LGBMRegressor(
        n_estimators=300,
        learning_rate=0.05
    )
    model.fit(X_train, y_train)
    return model
