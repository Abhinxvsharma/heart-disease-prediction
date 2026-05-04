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

App will be live at: `http://localhost:8501`

---

## 📡 API Endpoints

### `GET /`
Health check endpoint.

**Response:**
```json
{
  "message": "The API is working fine!"
}
```

### `POST /predict`
Accepts patient health data and returns a prediction.

**Request Body:**
```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125.0,
  "chol": 212.0,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168.0,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 3
}
```

**Response:**
```json
{
  "prediction": "The person is likely to have heart disease."
}
```

---

## 📦 Requirements

```
fastapi
uvicorn
streamlit
requests
scikit-learn
pandas
numpy
```

---

## 🔮 Future Enhancements

- [ ] Add model confidence/probability score to predictions
- [ ] Deploy backend to **Render** or **Railway**
- [ ] Deploy frontend to **Streamlit Community Cloud**
- [ ] Add patient history logging to a database
- [ ] Integrate SHAP/LIME for model explainability
- [ ] Dockerize the full application

---

## 👨‍💻 Author

**Abhinav Sharma**  
🔗 [LinkedIn](https://www.linkedin.com/in/abhinav-sharma-a73981382/)  
💻 Passionate about building AI/ML solutions that make a real-world impact.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
