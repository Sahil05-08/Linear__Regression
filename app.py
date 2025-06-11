import streamlit as st
import joblib
import numpy as np

model= joblib.load('regression_model.joblib')


st.write("JOB PACKAGE PREDICTION BASED ON CGPA")
st.write("Enter your CGPA to predict the expected job package:")

cgpa= st.number_input("CGPA", min_value=0.0, max_value=10.0,step=0.1)

if st.button("Predict Packages"):
    input_data=np.array([[cgpa]])

    prediction=model.predict(input_data)
    prediction_value=float(prediction[0])

    st.success(f"Predicted Package :{prediction_value: ,.2f}LPA")