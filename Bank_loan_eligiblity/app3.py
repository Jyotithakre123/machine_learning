import streamlit as st
import pickle
import numpy as np

with open("bank_loan_model.pkl", 'rb') as f:
    model = pickle.load(f)

st.title("Bank Loan Eligibility Predictor")

Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.number_input("Dependents", step=1, min_value=0)
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", step=500)
CoapplicantIncome = st.number_input("Coapplicant Income", step=500)
LoanAmount = st.number_input("Loan Amount", step=10)
Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", step=12)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])
Property_Area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

if st.button("Check Eligibility"):
    input_data = np.array([[Gender, Married, Dependents, Education, Self_Employed,
                            ApplicantIncome, CoapplicantIncome, LoanAmount,
                            Loan_Amount_Term, Credit_History, Property_Area]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Eligible for Loan")
    else:
        st.error("Not Eligible for Loan")
