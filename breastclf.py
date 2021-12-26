import streamlit as st
import numpy as np 
import pickle

st.subheader('Complete the following')
st.subheader('The mean : Radius, Texture, Perimeter, Area, Smoothness, Comapactness, Concavity, Symmetry, Fractal dimension')

radius_mean = st.number_input('What is the radius mean of the patiets cells?')
texture_mean = st.number_input('What is the texture mean of the patiets cells?')
perimeter_mean = st.number_input('What is the perimeter mean of the patiets cells?')
area_mean = st.number_input('What is the area mean of the patiets cells?')
smoothness_mean = st.number_input('What is the smothness mean of the patiets cells?')
compactness_mean = st.number_input('What is the comapactness mean of the patiets cells?')
concavity_mean = st.number_input('What is the concavity mean of the patiets cells?')
concave_points_mean = st.number_input('What is the concave points mean of the patiets cells?')
symmetry_mean = st.number_input('What is the symmetry mean of the patients cells?')
fractal_dimension_mean = st.number_input('What is the fractal dimension mean of the patients cells?')

st.subheader('The Squred Error : Radius, Texture, Perimeter, Area, Smoothness, Comapactness, Concavity, Symmetry, Fractal dimension')

radius_se = st.number_input('What is the radius squared error of the patients cells?')
texture_se = st.number_input('What is the texture squared error of the patients cells?')
perimeter_se = st.number_input('What is the perimeter squared error of the patients cells?')
area_se = st.number_input('What is the area squared error of the patients cells?')
smoothness_se = st.number_input('What is the smothness squared error of the patients cells?')
compactness_se = st.number_input('What is the comapactness squared error of the patients cells?')
concavity_se = st.number_input('What is the concavity squared error of the patients cells?')
concave_points_se = st.number_input('What is the concave points squared error of the patients cells?')
symmetry_se = st.number_input('What is the symmetry squared error of the patients cells?')
fractal_dimension_se = st.number_input('What is the fractal dimension squared error of the patients cells?')

st.subheader('The worst : Radius, Texture, Perimeter, Area, Smoothness, Comapactness, Concavity, Symmetry, Fractal dimension')

radius_worst = st.number_input('what is the radius worst number of the patients cells?')
texture_worst = st.number_input('what is the texture worst number of the patients cells?')
perimeter_worst = st.number_input('what is the perimeter worst number of the patients cells?')
area_worst = st.number_input('what is the area worst number of the patients cells?')
smoothness_worst = st.number_input('what is the smoothness worst number of the patients cells?')
compactness_worst = st.number_input('what is the comapactness worst number of the patients cells?')
concavity_worst = st.number_input('what is the concavity worst number of the patients cells?')
concave_points_worst = st.number_input('what is the concave points worst number of the patients cells?')
symmetry_worst = st.number_input('what is the symmetry worst number of the patients cells?')
fractal_dimension_worst = st.number_input('what is the fractal dimension worst number of the patients cells?')

submit = st.button('Submit Cell Features')

if submit:
	doctor_input = np.array([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,
							radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se,fractal_dimension_se,
							radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst])


	pickle_in = open('Breast-Cancer-KNN.pickle' , 'rb')
	clf = pickle.load(pickle_in)
	prediction = clf.predict([doctor_input])

	if prediction == 'B':
		st.success('The breast cells of the patient are likely to be Benign')
	elif prediction == 'M':
		st.success('The breast cells of the patient are likely to be Malignant')