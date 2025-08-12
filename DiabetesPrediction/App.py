import streamlit as st 
import pickle
import numpy as np
import pandas as pd 

with open("diabetes_model.pkl",'rb') as f:
    model = pickle.load(f)

st.title("Diabetes Predictor")


Pregnancies = st.number_input("Pregnencies", step=1)
Glucose = st.number_input("Glocose",step=5)
BloodPressure = st.number_input("BloodPressure", step= 10)
SkinThickness = st.number_input('Skin Thickness', step=5)
Insulin = st.number_input("Insulin", step=10)
BMI = st.number_input("BMI", step=1)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", step=0.1)
Age = st.slider("Age", min_value=21, max_value=81)


if st.button("Predict"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) 
    prediction = model.predict(input_data)[0]

    if prediction==1:
        st.success("This person has Diabetes")
    else:
        st.error("No Diabetes")
