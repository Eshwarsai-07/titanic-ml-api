from pydantic import BaseModel, Field
from typing import Literal

class Passenger(BaseModel):
    Pclass: int = Field(..., ge=1, le=3, example=3)
    Sex: Literal[0, 1] = Field(..., example=0, description="0 = male, 1 = female")
    Age: float = Field(..., ge=0, le=100, example=25.0)
    SibSp: int = Field(..., ge=0, example=0)
    Parch: int = Field(..., ge=0, example=0)
    Fare: float = Field(..., ge=0, example=7.25)
    Embarked_Q: Literal[0, 1] = Field(..., example=0)
    Embarked_S: Literal[0, 1] = Field(..., example=1)

    class Config:
        schema_extra = {
            "example": {
                "Pclass": 3,
                "Sex": 0,
                "Age": 22,
                "SibSp": 0,
                "Parch": 0,
                "Fare": 7.25,
                "Embarked_Q": 0,
                "Embarked_S": 1
            }
        }
