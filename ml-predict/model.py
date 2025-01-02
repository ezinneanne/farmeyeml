import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
data = pd.read_csv("final_data.csv")

# Feature and target separation
X = data[['pH', 'N', 'P', 'K', 'OC', 'Particles', 'Water_holding_content', 'Soil_type']]
y = data['crop_type']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
model = SVC()
model.fit(X_train, y_train)

# Save the model and scaler
joblib.dump(model, "svm_model.pkl")
joblib.dump(scaler, "scaler.pkl")
print("Model and scaler saved!")
