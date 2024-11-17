# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Importing the models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

#Create a sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',[ 
                           'Diabetics Prediiction System',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],icons=['activity', 'heart', 'lungs'], default_index=0 )
# Handle selections
if selected == 'Diabetics Prediiction System':
    
    #Tittle
    st.title('Diabetes Prediction System')
    
    #Creating columns with inputfields 
    #Creating input fields    
    col1, col2, col3 = st.columns(3)
    
    with col1:   
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the person')
    
    # Code for prediction
    diab_prediction = ' '
    
    # Creating predicting system 
    if st.button('Diabetic Prediction System'):
        diabetic_result = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if diabetic_result[0] == 1:
            diab_prediction = 'The person is diabetic'
        else:
            diab_prediction = 'The person is Non diabetic'
    
    st.success(diab_prediction)
    
if selected == 'Heart Disease Prediction':
    
    #Tittle
    st.title('Heart Disease Prediction')
    
    #Creating columns with inputfields 
    #Creating input fields    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age of the person')
    with col2:
        Sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Types ')
    with col1:
        trestbps = st.text_input('Resting blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    
    #Code for prediction
    heart_prediction = ' '
    
    #Creating predicting system 
    if st.button('Heart Disease Test Result'):
        heart_disease_result = heart_model.predict([[Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_attack_result[0] == 1:
            heart_prediction = 'The person have heart disease'
        else:
            heart_prediction = 'The person dont have heart disease'

    st.success(heart_prediction)
if selected == 'Parkinsons Prediction':
    #Tittle
    st.title('Parkinsons Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    #Creating input fields
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        RAP = st.text_input('MDVP:RAP')
    with col1:
        PPQ = st.text_input('MDVP:PPQ')
    with col2:
        DDP = st.text_input('Jitter:DDP')
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        APQ = st.text_input('MDVP:APQ')
    with col2:
        DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')     
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')
  
    
    #Code for prediction
    parkinsons_prediction = ' '
    
    #Creating predicting system 
    if st.button('Parkinsons Prediction System'):
        parkinsons_result = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if parkinsons_result[0] == 1:
            parkinsons_prediction = 'The person have parkinsons'
        else:
            parkinsons_prediction = "The person don't have parkinsons"
            
    st.success(parkinsons_prediction)