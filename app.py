import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import warnings

# Data columns
feature_names_best = ['Sex', 'Age', 'Height', 'Weight', 'Systolic Blood Pressure','Diastolic Blood Pressure', 'Heart Rate', 'BMI']

gender_dict = {"Laki-laki":1,"Perempuan":0}
feature_dict = {"Ya":1,"Tidak":0}

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 

def get_fvalue(val):
	feature_dict = {"Ya":1,"Tidak":0}
	for key,value in feature_dict.items():
		if val == key:
			return value 

# title
html_temp = """
<div>
<h1 style="color:#FF6E31;text-align:left;">
Prediksi Darah Tinggi</h1>
</div>
"""


st.markdown(html_temp, unsafe_allow_html=True)

if st.checkbox("Deskripsi"):
    	'''
   - Sex: Form Masukkan Jenis Kelamin (Laki-laki atau Perempuan)
	Age	Form Masukkan usia berupa angka bilangan bulat 
	contoh: 35 (untuk yang berusia 35)
	Height	Form Height merupakan tinggi pasien, berupa angka bilangan bulat 
	contoh: 159 (untuk yang memiliki tinggi 159 cm) (contoh: 159).
	Weight	Form Weight merupakan berat pasien, berupa angka bilangan bulat 
	contoh: 64 (untuk yang memiliki berat badan 64 kg) (contoh: 64).
	Systolic Bood Pressure	Form Systolic Bood Pressure merupakan Tekanan darah sistolik berupa angka bilangan bulat.
	contoh: 160
	Diastolic Blood Pressure	Form Diastolik Bood Pressure merupakan Tekanan Darah Diastolik berupa angka bilangan bulat.
	contoh: 87
	Heart Rate	Form Heart Rate merupakan Tekanan Darah, berupa angka bilangan bulat 
	contoh: 79
	BMI	Form BMI merupakan Indeks massa tubuh, berupa bilangan bulat
	Contoh: 27


		'''
# Logo

st.sidebar.title("Form Prediksi")

#['Sex', 'Age', 'Height', 'Weight', 'Systolic Blood Pressure','Diastolic Blood Pressure', 'Heart Rate', 'BMI']

# Male or Female
Sex = st.sidebar.radio("Jenis Kelamin",tuple(gender_dict.keys()))

# Age of the patient
Age = st.sidebar.number_input("Usia", 1,100)

# Height
Height = st.sidebar.number_input("Height", 1,1000)

# Weight
Weight = st.sidebar.number_input("Weight", 1,1000)

# Systolic Blood Pressure
SystolicBloodPressure = st.sidebar.number_input("Systolic Blood Pressure", 1,1000)

# Diastolic Blood Pressure
DiastolicBloodPressure = st.sidebar.number_input("Diastolic Blood Pressure", 1,1000)

# Heart Rate
HeartRate = st.sidebar.number_input("Heart Rate", 1,1000)

# BMI
BMI = st.sidebar.number_input("BMI", 1,1000)


feature_list = [[get_value(Sex,gender_dict), Age, Height, Weight, SystolicBloodPressure,DiastolicBloodPressure, HeartRate, BMI]]
pretty_result = {"Jenis Kelamin":Sex,
                 "Usia":Age,
                 "Tinggi":Height,
                 "Berat":Weight,
                 "Systolic Blood Pressure":SystolicBloodPressure,
                 "Diastolic Blood Pressure":DiastolicBloodPressure,
                 "Detak Jantung":HeartRate,                
                 "BMI":BMI}
'''
## Ini adalah nilai yang Anda masukkan
'''
st.json(pretty_result)
single_sample = np.array(feature_list).reshape(1,-1)

loaded_model = load_model('model_new.pkl')

diagnosis = ''

if st.button('Prediksi Penyakit'):
    pred = loaded_model.predict(feature_list)
    
    if pred == 0:
        diagnosis = 'Normal'
    elif pred == 1:
        diagnosis = 'Prehypertension'
    elif pred == 2:
        diagnosis = 'Stage 1 Hypertension'
    elif pred == 3:
        diagnosis = 'Stage 2 Hypertension'
        
st.success(diagnosis)

# 1 = Stage 2 Hypertension = 3
# 3 = Normal 0
# 4 = Prehypertension 1
# 28 = Stage 1 Hypertension 2
