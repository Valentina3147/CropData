import pickle
from fastapi import APIRouter
from schemas import schemas
import numpy as np

router=APIRouter()

pkl_filenamec="RFCropv102.pkl"
with open(pkl_filenamec,'rb') as file:
    model = pickle.load(file)

labels=["Temperatura","Humedad"]



@router.get("/")
async def root():
    return{
        "message":"AI Service"
    }

@router.post("/Predict")
def Predict_diabetes(data:schemas.Cropdata):
    data = data.model_dump()

    N = data["N"]
    P = data["P"]
    K = data["K"]
    Temperatura = data["Temperatura"]
    Humedad = data["Humedad"]
    PH = data["PH"]
    Rainfall = data["Rainfall"]
  
    xin = np.array([

        N,
        P,
        K,
        Temperatura,
        Humedad,
        PH,
        Rainfall]).reshape(1,7)

    prediction = model.predict(xin)
    yout = labels[prediction[0]]

    return{
        'prediction':yout
    }