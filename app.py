import streamlit as st
import numpy as np
import joblib
from datetime import datetime
# Load the trained model
model = joblib.load("calories_model.pkl")

# Page configuration
st.set_page_config(
    page_title="🔥 Calorie Burn Predictor",
    page_icon="🔥",
    layout="wide"
)

# 🔥 Custom CSS Styling
st.markdown("""
    <style>
    html, body, .stApp {
        height: 100%;
        margin:0;
        padding: 0;
        background: linear-gradient(135deg, #fff3e0, #ffe0b2);
    }
    .block-container {
        padding: 0 2rem !important;
    }
    .main {
        padding: 2rem 4rem;
        border-radius: 12px;
        background-color: #fff;
        box-shadow: 0 0 15px rgba(255, 87, 34, 0.25);
    }
    h1 {
        color: #e53935;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
        margin-bottom: 5px;
    }
    p, label, .stMarkdown {
        font-family: 'Segoe UI', sans-serif;
        color: #333333;
    }
    .stButton>button {
        background-color: #ff5722;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #e64a19;
        transition: 0.3s;
    }
    .prediction-result {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 10px;
        border-left: 6px solid #ff6f00;
        font-size: 22px;
        font-weight: bold;
        color: #d84315;
        margin-top: 1.5rem;
        text-align: center;
    }
    .suggestion {
        font-size: 18px;
        margin-top: 1rem;
        color: #444;
        text-align: center;
    }
    footer, header {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)
# Personalized Greeting
hour = datetime.now().hour
if hour < 12:
    greet = "☀️ Good morning"
elif hour < 17:
    greet = "🌞 Good afternoon"
else:
    greet = "🌙 Good evening"
# 🔥 Title and Header
st.markdown(f"<h1 style = 'text-algin:center;'> {greet}</h1>", unsafe_allow_html=True)
st.markdown("<h1 style = 'text-algin:center;'> Welcome to the 🔥 Calorie Burn Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Enter your body vitals and workout details to estimate your calorie burn!</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# 💪 Input Form
with st.form("calorie_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.radio("Gender", ["Male", "Female"])
        age = st.number_input("Age", 10, 100, 25)
        height = st.slider("Height (cm)", 100, 220, 170)
        weight = st.slider("Weight (kg)", 30, 150, 65)

    with col2:
        duration = st.slider("Workout Duration (minutes)", 5, 180, 30)
        heart_rate = st.slider("Heart Rate (bpm)", 60, 200, 120)
        body_temp = st.slider("Body Temp (°C)", 35.0, 42.0, 37.0)

    submitted = st.form_submit_button("🔥 Predict Calories Burned")

# Prediction Logic + Output
if submitted:
    gender_encoded = 1 if gender == "Male" else 0
    features = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])
    calories = model.predict(features)[0]

    # BMI Calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        bmi_status = "Underweight ❗"
    elif 18.5 <= bmi < 25:
        bmi_status = "Normal ✅"
    elif 25 <= bmi < 30:
        bmi_status = "Overweight ⚠️"
    else:
        bmi_status = "Obese 🚨"

    # Suggestions
    if calories < 150:
        suggestion = "⚠️ Low calorie burn. Try a longer or more intense session."
        emoji = "😓"
    elif 150 <= calories < 300:
        suggestion = "💪 Moderate burn! Keep it consistent and stay hydrated."
        emoji = "😊"
    else:
        suggestion = "🔥 Excellent session! You've burned a lot. Time to refuel and recover."
        emoji = "🏆"

    # Output Section
    st.markdown(f"<div class='prediction-result'>{emoji} Estimated Calories Burned: <strong>{calories:.2f} kcal</strong></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='suggestion'>Your BMI: <strong>{bmi:.2f}</strong> ({bmi_status})</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='suggestion'>{suggestion}</div>", unsafe_allow_html=True)
    st.balloons()

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:13px;'>Made with ❤️ using Streamlit • Interactive Health AI App</p>", unsafe_allow_html=True)