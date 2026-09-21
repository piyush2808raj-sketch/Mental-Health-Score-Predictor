import streamlit as st
import requests
import time
import plotly.graph_objects as go

# 1. Page Setup
st.set_page_config(page_title="Mind Score Predictor", page_icon="🧠", layout="wide")

# 2. Custom CSS to fix text colors and center things perfectly
st.markdown("""
    <style>
    /* Soft dark background */
    .stApp {
        background-color: #1e212b; 
    }
    
    /* Make ALL labels white and bold so they are easy to read */
    label, .st-cb p {
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }

    h1, h2, h3 {
        color: #00e5ff !important; 
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Style for the button */
    .stButton>button {
        background-color: #ff0055; 
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 22px;
        box-shadow: 0 0 15px #ff0055;
        margin-top: 20px;
    }
    
    .stButton>button:hover {
        background-color: transparent;
        border: 2px solid #ff0055;
        box-shadow: 0 0 25px #ff0055;
        color: #ff0055;
    }
    
    .big-score-box {
        font-size: 60px !important;
        color: #00e5ff; 
        text-align: center;
        font-weight: bold;
        text-shadow: 0 0 15px #00e5ff;
        padding: 30px;
        border: 2px solid #303645;
        border-radius: 20px;
        background-color: #262a35;
        margin-bottom: 20px;
    }
    /* Fix popup notification text visibility */
    div[data-testid="stToast"] {
        background-color: #262a35 !important;
        color: #ffffff !important;
    }
    /* Make the loading text a bit darker */
    [data-testid="stProgress"] p {
        color: #8892b0 !important; 
        font-weight: normal !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Mental Health Score Predictor 🧠")
st.markdown("<p style='text-align: center; color: #ffffff; font-size: 18px;'>Find out your mental health score using AI.</p>", unsafe_allow_html=True)
st.divider()

# 3. Create three columns for inputs
col1, col2, col3 = st.columns(3)

with col1:
    st.header("👤 Who Are You?")
    age = st.number_input("Age", min_value=10, max_value=100, value=20)
    gender = st.selectbox("Gender", ['Male', 'Female'])
    country = st.selectbox("Country", ['India', 'USA', 'Canada', 'Australia', 'UK', 'Germany', 'Mexico', 'Turkey', 'France', 'Spain', 'Other'])
    academic_level = st.selectbox("Study Level", ['High School', 'Undergraduate', 'Graduate'])

with col2:
    st.header("📱 Tech Habits")
    platform = st.selectbox("Most Used App", ['Facebook', 'LinkedIn', 'Instagram', 'Snapchat','Twitter','YouTube', 'TikTok', 'LINE', 'KakaoTalk', 'VKontakte', 'WhatsApp','WeChat'])
    purpose = st.selectbox("Why do you use it?", ['Networking', 'Education', 'Entertainment', 'News'])
    usage_hours = st.slider("Average Daily Social Media Usage", 0.0, 24.0, 3.0)
    unlocks = st.number_input("Phone Unlocks / Day", min_value=0, value=50)

with col3:
    st.header("🏃 Lifestyle")
    study_hours = st.slider("Study Hours / Day", 0.0, 24.0, 4.0)
    physical_hours = st.slider("Exercise Hours / Day", 0.0, 24.0, 1.0)
    sleep_hours = st.slider("Sleep Hours / Night", 0.0, 24.0, 7.0)
    stress = st.select_slider("Current Stress", options=['Low', 'Medium', 'High', 'Very High'])

st.divider()

# 4. Center the Button properly using exact columns
btn_space1, btn_col, btn_space2 = st.columns([1, 2, 1])

with btn_col:
    # use_container_width=True forces it to fill this center space perfectly
    button_clicked = st.button("🚀 PREDICT MY SCORE NOW 🚀", use_container_width=True)

# 5. Handle the Prediction
if button_clicked:
    payload = {
        "age": age,
        "gender": gender,
        "country": country,
        "academic_level": academic_level,
        "most_used_platform": platform,
        "purpose_of_use": purpose,
        "avg_daily_usage_hours": usage_hours,
        "daily_unlocks": unlocks,
        "study_hours": study_hours,
        "physical_activity_hours": physical_hours,
        "sleep_hours_per_night": sleep_hours,
        "stress_level": stress
    }
    
    try:
        progress_text = "Analyzing your habits..."
        my_bar = st.progress(0, text=progress_text)
        
        for percent_complete in range(100):
            time.sleep(0.01) 
            my_bar.progress(percent_complete + 1, text=progress_text)
            
        my_bar.empty() 
        
        response = requests.post("https://mental-health-score-predictor-api.onrender.com/predict", json=payload)
            
        if response.status_code == 200:
            result = response.json()
            score = result["predicted_mental_health_score"]
            
            st.toast("Prediction Complete! 🧠", icon='✅')
            
            spacer1, center_col, spacer2 = st.columns([1, 2, 1])
            
            with center_col:
                st.markdown(f"<div class='big-score-box'>Score: {score}</div>", unsafe_allow_html=True)
                
            
        else:
            st.error(f"Oops! The backend sent an error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Cannot find the backend! Make sure your FastAPI server is running on http://127.0.0.1:8000")