# Setup Guide

## Prerequisites

- **Python**: Version 3.10 or higher.
- **Docker**: Optional, for containerized deployment.
- **Git**: To clone the repository.

## Local Development Setup

1.  **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd titanic-ml-api
    ```

2.  **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\\Scripts\\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

## Docker Setup

1.  **Build the Docker Image**
    ```bash
    docker build -t titanic-ml-api .
    ```

2.  **Run the Container**
    ```bash
    docker run -d -p 8000:8000 titanic-ml-api
    ```
    The API will be accessible at `http://localhost:8000`.

## Testing

You can test the API using `curl` or Postman:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "Pclass": 3,
  "Sex": 0,
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked_Q": 0,
  "Embarked_S": 1
}'
```
