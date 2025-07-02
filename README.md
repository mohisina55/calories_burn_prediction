# 🔥 Calorie Burn Prediction App

A machine learning web app built with **Streamlit** that predicts the number of calories burned during exercise based on user input features like age, gender, weight, duration, heart rate, and body temperature.

---

## 📌 Live Demo

check out here: [Click here to try the app](https://caloriesburnprediction-ugswrbwtgugrkohy2fmcf6.streamlit.app/)

---

## 📁 Project Structure
```bash
├── app.py # Main Streamlit application
├── model.py # Model training and prediction logic
├── calories.csv # Dataset - Calorie labels
├── exercise.csv # Dataset - Exercise features
├── calories_model.pkl # Trained model saved with pickle
├── requirements.txt # List of required Python libraries
├── .env # Optional environment variables (if used)
└── README.md # Project documentation
```

---

## 🧠 Model Overview

This app uses a regression machine learning model to estimate the calories burned during exercise.

### ✅ Features Used:
- Age
- Gender
- Height
- Weight
- Duration (mins)
- Heart Rate
- Body Temperature

### 🎯 Target Variable:
- **Calories Burned**

---

## 📦 Installation & Running Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/calorie-burn-prediction.git
cd calorie-burn-prediction
```
### Step 2: Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Run the Streamlit app
```bash
streamlit run app.py
```
## 🌐 Deployment on Streamlit Cloud
1 .Push all files to your public GitHub repository.

2. Visit https://streamlit.io/cloud

3. Click "New app" and connect your GitHub account.

4. Choose your repo and set the main file to app.py.

5. Click Deploy.

## 🧪 Sample Input & Output
Input:

Age: 28

Gender: Female

Height: 160 cm

Weight: 60 kg

Duration: 45 mins

Heart Rate: 115 bpm

Body Temp: 37.3 °C

## Output:

✅ Predicted Calories Burned: 234.56 kcal
