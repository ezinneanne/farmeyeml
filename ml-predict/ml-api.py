import pandas as pd
import joblib
import sys
import json


# Load the model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Get input data from Node.js
input_data = json.loads(sys.argv[1])

# Preprocess and make predictions
X = pd.DataFrame([input_data])
X_scaled = scaler.transform(X)
prediction = model.predict(X_scaled)

# Return the result
print(json.dumps({"prediction": int(prediction[0])}))