import pickle
import pandas as pd
from data_preprocessing import preprocess_data
from feature_engineering import add_engineered_features

def detect():
    
    df = pd.read_csv("../data/employee_logs.csv")
    df = add_engineered_features(df)
    
    X_scaled, scaler = preprocess_data(df)
    
    with open("../models/anomaly_model.pkl", "rb") as f:
        anomaly_model = pickle.load(f)
    
    predictions = anomaly_model.predict(X_scaled)
    
    df["Anomaly"] = predictions
    df["Anomaly"] = df["Anomaly"].apply(lambda x: "Threat" if x == -1 else "Normal")
    
    return df