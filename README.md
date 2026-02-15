# Titanic Survival Prediction API

This project provides a Machine Learning API for predicting the survival of Titanic passengers. It is built using **FastAPI** and serves a pre-trained **Logistic Regression** model.

## Features

- **Predict Survival**: Endpoint to predict if a passenger would survive based on their details.
- **Health Check**: Endpoint to check if the API is running.
- **Dockerized**: specific `Dockerfile` for easy deployment.
- **Type Safety**: Uses `Pydantic` for request validation.

## Quick Start

### 1. Run with Docker

```bash
# Build the image
docker build -t titanic-ml-api .

# Run the container
docker run -p 8000:8000 titanic-ml-api
```

### 2. Run Locally

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Usage

### Predict Survival

**Endpoint**: `POST /predict`

**Request Body**:
```json
{
  "Pclass": 3,
  "Sex": 0,
  "Age": 22,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked_Q": 0,
  "Embarked_S": 1
}
```

**Response**:
```json
{
  "prediction": 0,
  "survival_probability": 0.123
}
```

## Documentation

For more detailed documentation, see the `docs/` directory:

- [API Documentation](docs/api.md)
- [Model Information](docs/model.md)
- [Setup Guide](docs/setup.md)
