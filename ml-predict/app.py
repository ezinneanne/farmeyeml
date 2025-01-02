from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = joblib.load("svm_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = np.array([
        data['nitrogen'],
        data['phosphorus'],
        data['potassium'],
        data['oxygen_content'],
        data['pH'],
        data['particles'],
        data['water_holding_content'],
        data['soil_type']
    ]).reshape(1, -1)
    inputs_scaled = scaler.transform(inputs)
    prediction = model.predict(inputs_scaled)[0]
    return jsonify({'crop_type': prediction})

if __name__ == '__main__':
    app.run(debug=True)
