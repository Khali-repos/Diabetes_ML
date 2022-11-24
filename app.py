# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:31:47 2022

@author: Iyama
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#saved models

diabetes_model = pickle.load(open('C:/Users/Iyama/Desktop/ML/MLdiabetes/diabetes_model.sav', 'rb'))


def diabetes_prediction(input_data):
    
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = diabetes_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
     return'No diabetes has been predicted'
    else:
      return'ATTENTION Diabetes has been predicted'


def main():
    
    
    # App title
    st.title('Diabetes Prediction')
    
    
    # Required 'user' input data
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # Prediction code 
    diagnosis = ''
    
    # Prediction button
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
