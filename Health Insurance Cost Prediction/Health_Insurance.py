# -*- coding: utf-8 -*-
"""
@author: Imane BH
"""

import streamlit as st
import joblib


def main():
    html_temp = """
    <div style="background-color:lightgreen;padding:16px">
    <h2 style="color:black";text-align:center> Health Insurance Cost Prediction Using ML</h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib_gr')
    
    p1 = st.slider('Enter Your Age',18,100)
       
    s1 = st.selectbox('Sex',('Male','Female'))
    # for prediction it requires numerical values
    if s1=='Male':
        p2=1
    else:
        p2=0
    p3 = st.number_input("Enter Your BMI Value")
    
    p4 = st.slider("Enter Number of Children",0,4)
    
    s2 = st.selectbox("Smoker",("Yes","No"))
    
    #again with string values needs to use numerical values
    if s2=='Yes':
        p5=1
    else:
        p5=0
    
    #p6 = st.slider("Enter Your Region",1,4)
    s3=st.selectbox("Region",("southwest","southeast","northwest","northeast"))
    
    if s3=="southwest":
        p6=1
    elif s3=="southeast":
        p6=2
    elif s3=="northwest":
        p6=3
    elif s3=="northeast":
        p6=4
    
    # for the button predict
    if st.button('Predict'):
        pred= model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.balloons()
        st.success('Your Insurance Cost is ($) {}'.format(round(pred[0],2)))
if __name__ == '__main__':
    main()