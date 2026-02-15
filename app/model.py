import pickle
import numpy as np

try:
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

def predict_survival(features: list):
    """
    Predict survival using trained model.
    Returns prediction and probability.
    """
    features_array = np.array(features).reshape(1, -1)

    prediction = model.predict(features_array)[0]
    probability = model.predict_proba(features_array)[0][1]

    return int(prediction), float(probability)
