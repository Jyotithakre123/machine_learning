import streamlit as st
import pickle
import numpy as np

with open("SVM_Poly_Model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Statlog German Credit Prediction App")

status = st.selectbox("Status of existing checking account",)
duration = st.slider("Duration",)
credit_history = st.selectbox("Credit history",)
purpose = st.selectbox("Purpose",)
credit_amount = st.number_input("Credit amount",)
savings = st.selectbox("Savings account/bonds",)
employment = st.selectbox("Present employment since",)
installment_rate = st.slider("Installment rate",)
personal_status = st.selectbox("Personal status and sex",)
other_debtors = st.selectbox("Other debtors / guarantors",)
residence_since = st.slider("Present residence since",)
property = st.selectbox("Property",)
age = st.slider("Age",)
other_installments = st.selectbox("Other installment plans",)
housing = st.selectbox("Housing",)
credits_at_bank = st.slider("Number of existing credits at this bank",)
job = st.selectbox("Job")
people_liable = st.slider("No. of people being liable to provide maintenance for",)
telephone = st.selectbox("Telephone",)
foreign_worker = st.selectbox("foreign worker",)



if st.button("Predict"):
    arr = np.array([])
    pred = model.predict(arr)
    st.success(f"Prediction: {pred[0]}")

    if pred[0] == 1:
        st.success("Good Credit Risk")
    else:
        st.error("Bad Credit Risk")



