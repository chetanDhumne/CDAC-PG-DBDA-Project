import numpy as np
import pandas as pd
import streamlit as st
import pickle

pickel_in = open("C:/Users/panka/Documents/Project 2020/classifier.pkl","rb")
rm=pickle.load(pickel_in)

def predictions(pH,EC,OC,N,P,K,S,Zn,Fe,Cu,Mn,B):
    pred=rm.predict([[pH,EC,OC,N,P,K,S,Zn,Fe,Cu,Mn,B]])
    print(pred)
    return(pred)

def main():
    st.title("Crop Predication")
    html_temp = """
    <div style="background-color:tomato;padding:10px;">
    <h2 style="color:white;text-align:center;">Crop Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    pH = st.text_input("pH")
    EC = st.text_input("EC")
    OC = st.text_input("OC")
    N = st.text_input("N")
    P = st.text_input("P")
    K = st.text_input("K")
    S = st.text_input("S")
    Zn = st.text_input("Zn")
    Fe = st.text_input("Fe")
    Cu = st.text_input("Cu")
    Mn = st.text_input("Mn")
    B = st.text_input("B")
    result=""
    if st.button("Predict"):
        result=predictions(pH,EC,OC,N,P,K,S,Zn,Fe,Cu,Mn,B)
    st.success('Crop Predicated is : {}'.format(result))
if __name__=='__main__':
    main()
    
    
