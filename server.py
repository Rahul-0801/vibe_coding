from fastapi import FastAPI
import joblib
import pandas as pd
app = FastAPI()
model = joblib.load("deploy_predictor.pkl")

@app.get("/")
def root():
    return {"message": "FastAPI server is running"}

@app.post("/predict")
def predict_deploy(data: dict):
   df = pd.DataFrame([data])
   pred = model.predict(df)[0]
   return {"deploy_success_prediction": bool(pred)}