from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/forecast")
def forecast(features: list):
    prediction = model.predict([features])
    return {"forecast": float(prediction[0])}
