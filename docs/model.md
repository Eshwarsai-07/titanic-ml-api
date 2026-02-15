# Model Information

## Overview

The model predicts the survival of Titanic passengers based on their demographic and travel information.

## Model Details

- **Algorithm**: Logistic Regression (assumed based on implementation details).
- **Framework**: Scikit-Learn.
- **Input Features**: 8 Features.
- **Output**: Binary classification (0: Not Survived, 1: Survived) and probability score.

## Input Features

The specific input features expected by the model, in order, are:

1.  **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd). A proxy for socio-economic status.
2.  **Sex**: Sex (0 = Male, 1 = Female).
3.  **Age**: Age in years.
4.  **SibSp**: # of siblings / spouses aboard the Titanic.
5.  **Parch**: # of parents / children aboard the Titanic.
6.  **Fare**: Passenger fare.
7.  **Embarked_Q**: Port of Embarkation - Queenstown (1 = Yes, 0 = No).
8.  **Embarked_S**: Port of Embarkation - Southampton (1 = Yes, 0 = No). (Note: Cherbourg is implied if both Q and S are 0).

## Artifacts

The trained model is serialized using `pickle` and stored at:
- `model/model.pkl`

## Usage in Code

The model is loaded in `app/model.py` and used via `model.predict()` and `model.predict_proba()`.
