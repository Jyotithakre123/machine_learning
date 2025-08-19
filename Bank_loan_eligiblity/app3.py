import streamlit as st
import pickle
import numpy as np

with open("bank_loan_model.pkl", 'rb') as f:
    model = pickle.load(f)

st.title("Bank Loan Eligibility")

Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.number_input("Dependents", step=1, min_value=0)
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])
ApplicantIncome = st.number_input("Applicant Income", step=500)
LoanAmount = st.number_input("Loan Amount", step=10)
Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", step=12)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])

gender_map = {"Male": 0, "Female": 1}
married_map = {"Yes": 1, "No": 0}
education_map = {"Graduate": 1, "Not Graduate": 0}
self_employed_map = {"Yes": 1, "No": 0}

if st.button("Check Eligibility"):
    input_data = np.array([[Gender, Married, Dependents, Education, Self_Employed,
                            ApplicantIncome, LoanAmount,
                            Loan_Amount_Term, Credit_History]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Eligible for Loan")
    else:
        st.error("Not Eligible for Loan")
