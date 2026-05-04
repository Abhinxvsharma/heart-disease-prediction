import streamlit as st
import requests


url = "http://localhost:8000"



st.title("Heart Disease Prediction")

st.write("This app predicts the likelihood of heart disease based on various health parameters.")


st.write("Please enter the following details:")

age = st.number_input("Age", 1, 120, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (cp)", [0,1,2,3])
trestbps = st.number_input("Resting BP", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar >120", [0,1])
restecg = st.selectbox("Rest ECG", [0,1,2])
thalach = st.number_input("Max Heart Rate", 60, 220, 150)
exang = st.selectbox("Exercise Angina", [0,1])
oldpeak = st.number_input("Oldpeak", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope", [0,1,2])
ca = st.selectbox("CA (vessels)", [0,1,2,3])
thal = st.selectbox("Thal", [1,2,3])



if st.button("Predict"):
    data = {
        "age": age,
        "sex": 1 if sex == "Male" else 0,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }

    response = requests.post(url + "/predict", json=data)
    result = response.json()
    st.write(f"Prediction: {result['prediction']}")