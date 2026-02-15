# API Documentation

The API is built using [FastAPI](https://fastapi.tiangolo.com/), which provides automatic documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc).

## Endpoints

### 1. Root

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.
- **Response**:
    ```json
    {
      "message": "Welcome to Titanic ML Prediction API"
    }
    ```

### 2. Health Check

- **URL**: `/health`
- **Method**: `GET`
- **Description**: Checks the health status of the API.
- **Response**:
    ```json
    {
      "status": "API is running successfully"
    }
    ```

### 3. Predict Survival

- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Predicts survival probability for a passenger.
- **Request Body**:
    - `Pclass` (int): Passenger Class (1, 2, or 3).
    - `Sex` (int): 0 for Male, 1 for Female.
    - `Age` (float): Age of the passenger.
    - `SibSp` (int): Number of siblings/spouses aboard.
    - `Parch` (int): Number of parents/children aboard.
    - `Fare` (float): Passenger fare.
    - `Embarked_Q` (int): 1 if embarked from Queenstown, else 0.
    - `Embarked_S` (int): 1 if embarked from Southampton, else 0.

- **Example Request**:
    ```json
    {
      "Pclass": 3,
      "Sex": 0,
      "Age": 22.0,
      "SibSp": 1,
      "Parch": 0,
      "Fare": 7.25,
      "Embarked_Q": 0,
      "Embarked_S": 1
    }
    ```

- **Example Response**:
    ```json
    {
      "prediction": 0,
      "survival_probability": 0.105
    }
    ```
    - `prediction`: 0 (Not Survived) or 1 (Survived).
    - `survival_probability`: Probability of survival (0.0 to 1.0).

## Error Handling

The API returns standard HTTP error codes:
- `200`: Success
- `422`: Validation Error (Invalid input data)
- `500`: Internal Server Error (Model loading or prediction failure)
