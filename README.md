# 🧠 Mental Health Score Prediction

A machine learning web application that predicts a user's **mental health score** based on their digital habits, academic routine, lifestyle factors, and stress level.

The project uses **Scikit-learn** for machine learning, **FastAPI** for the backend API, and **Streamlit** for the frontend.

> **Note:** This project is for educational and demonstration purposes only. The predicted score is not a medical diagnosis.

## 🚀 Live Demo

### 🌐 Streamlit Frontend
[Open Mental Health Score Predictor](https://mental-health-score-predictor-qv1d.onrender.com)

### ⚡ FastAPI Backend
[Open API](https://mental-health-score-predictor-api.onrender.com)

### 📖 API Documentation
[Open Swagger API Docs](https://mental-health-score-predictor-api.onrender.com/docs)

## 🚀 Features

- 🧠 Predicts a user's mental health score using a trained machine learning model
- 📱 Uses digital behaviour such as social media usage and phone unlocks
- 📚 Considers academic routine such as study hours and academic level
- 😴 Considers lifestyle factors such as sleep and physical activity
- 🧘 Includes stress level as a prediction feature
- ⚡ FastAPI backend for real-time predictions
- ✅ Input validation using Pydantic
- 💾 Trained model saved using Joblib

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Frontend
- Streamlit
- Plotly

### Development
- Google Colab
- VS Code
- Git & GitHub

## 📊 Input Features

The model uses the following features to predict the mental health score:

| Feature | Description |
|---|---|
| Age | User's age |
| Gender | User's gender |
| Country | User's country |
| Academic Level | User's current academic level |
| Most Used Platform | Social media platform used most frequently |
| Purpose of Use | Main purpose of using social media |
| Average Daily Usage | Average social media usage per day in hours |
| Daily Unlocks | Number of times the phone is unlocked per day |
| Study Hours | Average study hours per day |
| Physical Activity | Average physical activity hours per day |
| Sleep Hours | Average sleep duration per night |
| Stress Level | User's reported stress level |

## 🧠 Machine Learning Pipeline

The final model follows this training workflow:

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Transformation
   ↓
Train-Test Split
   ↓
Random Forest Regressor
   ↓
Model Evaluation
   ↓
Save Trained Model (.pkl)
   ↓
FastAPI Prediction API
```

## 🏗️ Project Architecture

The application follows a simple **Frontend → Backend → Machine Learning Model** architecture.

```text
User
 │
 ▼
Streamlit Frontend
 │
 │  JSON Request
 ▼
FastAPI Backend
 │
 ▼
Trained Random Forest Model
 │
 ▼
Mental Health Score Prediction
 │
 ▼
Streamlit Frontend
 │
 ▼
Prediction Result
```

## 📁 Project Structure

```text
Mental_Health_Score_Pred/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── model/
│   └── Mental_Health_Pred_Model.pkl
│
├── training/
│   └── train.py
│
├── data/
│   └── mental_health_data.csv
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
└── README.md
```

## 🚀 Deployment

The application is deployed on **Render** using two separate services:

- **FastAPI Backend** – Handles API requests and machine learning predictions.
- **Streamlit Frontend** – Provides the user interface.

### Deployment Architecture

```text
                    Render
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Streamlit Frontend       FastAPI Backend
          │                       │
          │   POST /predict       │
          └──────────────────────►│
                                  │
                                  ▼
                         Random Forest Model
                                  │
                                  ▼
                         Mental Health Score
                                  │
                                  ▼
                          Prediction Response
                                  │
          ◄───────────────────────┘
          │
          ▼
   Display Prediction
```

## 🤖 Model

The application uses a **Random Forest Regressor** to predict the mental health score.

### Model Details

- **Model:** Random Forest Regressor
- **Task:** Regression
- **Target:** Mental Health Score
- **Training Library:** Scikit-learn
- **Model Serialization:** Joblib
- **Saved Model:** `Mental_Health_Pred_Model.pkl`

### Model Selection

During development, multiple approaches were experimented with, including:

- Linear Regression
- Random Forest Regressor
- Random Forest with hyperparameter tuning using `RandomizedSearchCV`

After evaluating the models, the **standard Random Forest Regressor** was selected as the final model because it achieved better performance than the other tested approaches.

### Model File

The trained model is stored in:

```text
model/
└── Mental_Health_Pred_Model.pkl
```

## 📚 Data Attribution

The dataset used for this project was obtained from **Kaggle** and was used for training and evaluating the machine learning model.

The dataset contains information related to:

- Demographic characteristics
- Social media usage
- Academic routine
- Physical activity
- Sleep patterns
- Stress levels
- Mental health scores

Dataset source:

**Kaggle:** [Mental Health and Social Media Dataset](https://www.kaggle.com/datasets/shivasingh4945/student-social-media-and-mental-health-impact)

> Please refer to the original Kaggle dataset page for the dataset license, usage conditions, and attribution requirements.

---

## ⚠️ Disclaimer

This project is created for **educational and demonstration purposes only**.

The predicted mental health score is generated by a machine learning model and **should not be considered a medical diagnosis, clinical assessment, or professional mental health advice**.

Users should consult a qualified healthcare or mental health professional for actual medical or psychological concerns.

---

## 🔮 Future Improvements

Possible future improvements include:

- Improve model performance with larger and more diverse datasets
- Add model explainability and feature importance
- Add prediction history
- Improve input validation
- Add authentication and API security
- Implement automated model retraining
- Add more detailed data visualizations
- Improve deployment scalability
