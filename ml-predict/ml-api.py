import os
import pandas as pd
import joblib
import sys
import json

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the model and scaler using absolute paths
model_path = os.path.join(script_dir, "svm_model.pkl")
scaler_path = os.path.join(script_dir, "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Get input data from Node.js
input_data = json.loads(sys.argv[1])

# Preprocess and make predictions
X = pd.DataFrame([input_data])

# Rename the columns to match those used during training
X.rename(columns={
    "Nitrogen": "N",
    "Phosphorus": "P",
    "Potassium": "K"
}, inplace=True)

print(X)

# Scale and predict
X_scaled = scaler.transform(X)
prediction = model.predict(X_scaled)

# Return the result
print(json.dumps({"prediction": int(prediction[0])}))
