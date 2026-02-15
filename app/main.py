from fastapi import FastAPI, HTTPException
from app.schemas import Passenger
from app.model import predict_survival


app = FastAPI(
    title="Titanic Survival Prediction API",
    description="ML API built with FastAPI for predicting Titanic survival",
    version="1.0.0"
)

# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.get("/health")
def health():
    return {"status": "API is running successfully"}


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "Welcome to Titanic ML Prediction API"}


# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(passenger: Passenger):
    try:
        features = [
            passenger.Pclass,
            passenger.Sex,
            passenger.Age,
            passenger.SibSp,
            passenger.Parch,
            passenger.Fare,
            passenger.Embarked_Q,
            passenger.Embarked_S
        ]

        prediction, probability = predict_survival(features)

        return {
            "prediction": prediction,
            "survival_probability": round(probability, 3)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


