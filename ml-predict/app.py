import os
import pandas as pd
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Load the model, scaler, and label encoders
MODEL_PATH = os.path.join(os.getcwd(), "logistic_regression_model.pkl")
SCALER_PATH = os.path.join(os.getcwd(), "scaler.pkl")
SOIL_ENCODER_PATH = os.path.join(os.getcwd(), "soil_label_encoder.pkl")
CROP_ENCODER_PATH = os.path.join(os.getcwd(), "crop_label_encoder.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
soil_label_encoder = joblib.load(SOIL_ENCODER_PATH)
crop_label_encoder = joblib.load(CROP_ENCODER_PATH)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON
        data = request.json
        
        # Validate input
        required_fields = [
            "pH", "N", "P", "K", "OC", 
            "Particles", "Water_holding_content", "Soil_type"
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400
        
        # Preprocess input
        input_data = pd.DataFrame([data])
        
        # Encode soil type
        input_data['Soil_type'] = soil_label_encoder.transform(input_data['Soil_type'])
        
        # Scale features
        scaled_data = scaler.transform(input_data)
        
        # Predict crop type
        prediction = model.predict(scaled_data)
        
        # Decode predicted crop type
        predicted_crop = crop_label_encoder.inverse_transform([int(prediction[0])])[0]
        
        # Return the prediction
        return jsonify({"prediction": predicted_crop}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
