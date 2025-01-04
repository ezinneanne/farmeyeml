import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
from sklearn.metrics import accuracy_score


# Load the dataset
data = pd.read_csv("final_data.csv")

# Encode categorical columns
label_encoder_soil = LabelEncoder()
data['Soil_type'] = label_encoder_soil.fit_transform(data['Soil_type'])

label_encoder_crop = LabelEncoder()
data['crop_type'] = label_encoder_crop.fit_transform(data['crop_type'])


# Split features and target
X = data.drop(columns=['crop_type'])  # Features
y = data['crop_type']  # Target


# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = SVC(
    C=1.0,              # Regularization parameter
    kernel='rbf',       # Kernel type ('linear', 'poly', 'rbf', 'sigmoid')
    gamma='scale',      # Kernel coefficient ('scale', 'auto', or a float value)
    coef0=0.0,          # Coefficient for 'poly' and 'sigmoid' kernels
    tol=1e-3            # Tolerance for stopping criterion
)
model.fit(X_train, y_train)


# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model and scaler
joblib.dump(model, "svm_model.pkl")
joblib.dump(scaler, "scaler.pkl")
# Save LabelEncoders
joblib.dump(label_encoder_soil, "soil_label_encoder.pkl")
joblib.dump(label_encoder_crop, "crop_label_encoder.pkl")
print("Soil and crop label encoders saved too!")
print("Model and scaler saved!")
