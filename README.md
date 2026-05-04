❤️ Heart Disease Prediction System

🚀 Overview

This project is a **Machine Learning-based Heart Disease Prediction System** that predicts whether a person is likely to have heart disease based on clinical parameters.

It is built using:

* 🔹 FastAPI (Backend API)
* 🔹 Streamlit (Frontend UI)
* 🔹 Scikit-learn (ML Model)

---

🎯 Features

* Real-time heart disease prediction
* Interactive UI using Streamlit
* FastAPI backend for model serving
* End-to-end ML pipeline (Model → API → UI)

---

 🛠️ Tech Stack

* Python
* Scikit-learn
* FastAPI
* Streamlit
* NumPy & Pandas

---

📂 Project Structure

```
Heart-Disease-prediction/
│── main.py
│── predict_streamlit.py
│── model.pkl
│── requirements.txt
│── README.md
│── .gitignore
```

---
⚙️ Installation & Setup

1. Clone Repository

```
git clone https://github.com/Abhinxvsharma/heart-disease-prediction.git
cd heart-disease-prediction
```

2. Create Virtual Environment

```
python -m venv myenv
myenv\Scripts\activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

 Start FastAPI Backend

```
uvicorn main:app --reload
```

👉 Open: http://127.0.0.1:8000/docs

# Start Streamlit Frontend

```
streamlit run predict_streamlit.py
```

👉 Open: http://localhost:8501

---

 📊 Input Features

* Age
* Sex
* Chest Pain Type (cp)
* Resting Blood Pressure (trestbps)
* Cholesterol (chol)
* Fasting Blood Sugar (fbs)
* Rest ECG (restecg)
* Max Heart Rate (thalach)
* Exercise Induced Angina (exang)
* Oldpeak
* Slope
* CA (vessels)
* Thal

---

 📈 Output

* ✔️ Heart Disease Likely
* ❌ No Heart Disease

---

 📸 Screenshots
 
🔹 Streamlit UI

Given in files


🔹 FastAPI Swagger

Given in files

---

📌 Future Improvements

* Deploy project online (Render / AWS)
* Improve UI/UX
* Add model performance metrics

---

🔗 Connect with Me

👤 Abhinav Sharma
👉 https://www.linkedin.com/in/abhinav-sharma-a73981382/

---

⭐ Support

If you like this project, give it a ⭐ on GitHub!
