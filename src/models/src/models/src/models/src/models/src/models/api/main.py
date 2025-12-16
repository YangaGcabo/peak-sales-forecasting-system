from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ForecastRequest(BaseModel):
    features: list

@app.post("/predict")
def predict(req: ForecastRequest):
    prediction = sum(req.features) / len(req.features)
    return {"forecast": prediction}
