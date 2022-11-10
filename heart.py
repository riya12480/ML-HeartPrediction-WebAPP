# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:54:53 2022

@author: 91971
"""

import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:red";text-align:center>Heart Diseases Prediction</h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    model = joblib.load('model_joblib_heart')
    
    f1 = st.slider("Age")
    f2 = st.selectbox("Sex  (Male-1 | Female-0)", ("1","0"))
    f3 = st.selectbox("cp", ("0","1","2"))  
    f4 = st.text_input("trestbps")
    f5 = st.text_input("chol")
    f6 = st.text_input("fbs")
    f7 = st.text_input("restcg")
    f8 = st.text_input("thalach")
    f9 = st.text_input("exang")
    f10 = st.text_input("oldpeak")
    f11 = st.text_input("slope")
    f12 = st.text_input("ca")
    f13 = st.text_input("thal")
    
    if st.button("Predict"):
        pred = model.predict([[int(f1),int(f2),int(f3),int(f4),int(f5),int(f6),int(f7),int(f8),int(f9),float(f10),int(f11),int(f12),int(f13)]])
        if pred==1:
            st.success("You have Heart Diseases.")
        if pred==0:
            st.success("Great! you are healthy.")

if __name__ == '__main__':
    main()