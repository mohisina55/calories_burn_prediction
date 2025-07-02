import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load and preprocess data
calories_data = pd.read_csv("C:\Users\mohis\OneDrive\Desktop\chatbots\calorie_prediction\calories.csv")
exercise_data = pd.read_csv("C:\Users\mohis\OneDrive\Desktop\chatbots\calorie_prediction\exercise.csv")


# Encode 'Gender'
exercise_data['Gender'] =exercise_data['Gender'].map({'male': 1, 'female': 0})
calories_data = pd.concat([exercise_data,calories_data['Calories']],axis = 1)
# Features and label
X = calories_data.drop(['User_ID', 'Calories'], axis=1)
y = calories_data['Calories']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = XGBRegressor()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "calories_model.pkl")
