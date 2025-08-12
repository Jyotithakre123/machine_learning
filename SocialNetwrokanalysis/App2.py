import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# load model 
with open("dtc_model.pkl",'rb') as f:
    model = pickle.load(f)

# Load Encoder
with open("Gender_enc.pkl",'rb') as f:
    Gender_enc = pickle.load(f)

st.title("Social Network Advertisement Model")

Gender_option = list(Gender_enc.classes_)

Age = st.slider("Age",min_value=0,max_value=60)
Gender = st.selectbox("Gender",options=Gender_option)
Salary = st.number_input("Salary",min_value=10000)

Gender_enc = Gender_enc.transform([Gender])[0]

