# backend/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Allow Vue frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your model once when server starts
model = tf.keras.models.load_model("crop-pest-disease-classifier.keras")

# Map class indices to diseases/pests and treatments
class_info = {
    0: {"name": "Maize Leaf Blight", "treatment": "Apply fungicide and rotate crops."},
    1: {"name": "Armyworm", "treatment": "Use biocontrol agents or insecticides."},
    2: {"name": "Healthy", "treatment": "No action needed."},
    # extend with your dataset classes...
}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))  # resize to model input size
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions[0])
    confidence = float(np.max(predictions[0]))

    # Get class details
    result = class_info.get(class_idx, {"name": "Unknown", "treatment": "No info"})
    
    return {
        "class": result["name"],
        "confidence": round(confidence, 2),
        "treatment": result["treatment"]
    }
