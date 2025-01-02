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
        data['pH'],
        data['N'],
        data['P'],
        data['K'],
        data['OC'],
        data['Particles'],
        data['Water_holding_content'],
        data['Soil_type']
    ]).reshape(1, -1)
    inputs_scaled = scaler.transform(inputs)
    prediction = model.predict(inputs_scaled)[0]
    return jsonify({'crop_type': prediction})

if __name__ == '__main__':
    app.run(debug=True)
