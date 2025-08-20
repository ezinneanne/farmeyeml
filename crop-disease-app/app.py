import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
MODEL_PATH = "crop_pest_disease_classifier.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Class names (replace with your actual labels in correct order!)
CLASS_NAMES = [
    "Maize Diseases",
    "Maize Pests",
    "Maize Pests Activities",
    "Onion Diseases",
    "Onion Pests",
    "Tomato Diseases"
    "Tomato Pests"
    "Healthy Leaves"
]

# Dictionary of info + treatment
DISEASE_INFO = {
    "Healthy Maize": {
        "description": "No signs of pest or disease detected.",
        "treatment": "No treatment required. Continue good farm practices."
    },
    "Maize Leaf Blight": {
        "description": "A fungal disease causing brown lesions on leaves.",
        "treatment": "Use resistant varieties, crop rotation, and fungicides if severe."
    },
    "Maize Stem Borer": {
        "description": "Insect larvae that tunnel into maize stems.",
        "treatment": "Apply biological control (Trichogramma) or insecticides early."
    },
    "Onion Purple Blotch": {
        "description": "Fungal disease causing purple lesions on onion leaves.",
        "treatment": "Apply fungicides and avoid overhead irrigation."
    },
    "Onion Thrips": {
        "description": "Tiny insects that suck sap, causing silver patches on leaves.",
        "treatment": "Use insecticidal soap, neem oil, or thrip-resistant varieties."
    },
    "Tomato Leaf Curl Virus": {
        "description": "Virus spread by whiteflies, causing curling and yellowing leaves.",
        "treatment": "Control whiteflies with sticky traps and insecticides."
    },
    "Tomato Hornworm": {
        "description": "Large caterpillars feeding on tomato leaves and fruits.",
        "treatment": "Handpick hornworms or apply Bt-based insecticides."
    },
    "Healthy Tomato": {
        "description": "No signs of pest or disease detected.",
        "treatment": "Maintain regular crop monitoring and good practices."
    }
}

# Preprocess image
def preprocess_image(image: Image.Image):
    img = image.resize((224, 224))  # adjust if your model uses another size
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

# Streamlit UI
st.set_page_config(page_title="Crop Pest & Disease Classifier", layout="wide")
st.title("🌱 Crop Pest & Disease Classifier")
st.write("Upload a crop image to identify possible pest or disease and get treatment suggestions.")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Prediction
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # Show results
    st.subheader(f"✅ Prediction: {predicted_class}")
    st.write(f"**Confidence:** {confidence:.2f}%")

    # Show info + treatment
    info = DISEASE_INFO.get(predicted_class, {"description": "Info not available", "treatment": "N/A"})
    st.markdown(f"**ℹ️ About:** {info['description']}")
    st.markdown(f"**💊 Suggested Treatment:** {info['treatment']}")
