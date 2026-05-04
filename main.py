from fastapi import FastAPI
from pydantic import BaseModel

import pickle

model=pickle.load(open("model.pkl","rb"))


app=FastAPI()


class HeartData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int



@app.get("/")
def greet():
    return {"message":"The API is working fine!"}


@app.post("/predict")
def predict(data: HeartData):
    data = [[
        data.age,
        data.sex,
        data.cp,
        data.trestbps,
        data.chol,
        data.fbs,
        data.restecg,
        data.thalach,
        data.exang,
        data.oldpeak,
        data.slope,
        data.ca,
        data.thal
    ]]

    output = model.predict(data)

    if output[0] == 1:
        return {"prediction": "The person is likely to have heart disease."}
    else:
        return {"prediction": "The person is unlikely to have heart disease."}


