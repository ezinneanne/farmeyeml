import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

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

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the Logistic Regression model
model = LogisticRegression(
    C=1.0,               # Regularization strength (higher values = less regularization)
    solver='lbfgs',      # Optimization algorithm
    max_iter=1000,       # Maximum number of iterations
    random_state=42      # Ensures reproducibility
)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model and scaler
joblib.dump(model, "logistic_regression_model.pkl")
joblib.dump(scaler, "scaler.pkl")

# Save LabelEncoders
joblib.dump(label_encoder_soil, "soil_label_encoder.pkl")
joblib.dump(label_encoder_crop, "crop_label_encoder.pkl")

print("Model, scaler, and label encoders saved!")
