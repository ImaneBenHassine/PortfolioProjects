# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 11:13:08 2021

@author: Imane BH
"""

# Imports libraries
import streamlit as st
import pandas as pd
import seaborn as sns



# Header and subheader

st.title("Data Analysis")
st.subheader("Data Analysis using Python & Streamlit")

#Upload Dataset

upload=st.file_uploader("Upload your Dataset")
if upload is not None:
    df=pd.read_csv(upload) #converted uploaded file into csv to perform data analytics
    
    
# Show Dataset 
# check if the data is uploaded first
if upload is not None:
  if st.checkbox("Preview Dataset"):
    if st.button("Head"):
        st.write(df.head())
    if st.button("Tail"):
        st.write(df.tail())
        
# Find shape of dataset
if upload is not None:
    st.write("Check data shape")
    st.write(df.shape)
    
# check for Null Values in dataset
if upload is not None:
    test=df.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in the dataset"):
            st.write(df.isnull().sum())
            
    else:
        st.success("Congrat!! No Missing Values")
            
# Find Duplicate Values in dataset
if upload is not None:
    test==df.duplicated().any()
    if test==True:
        st.warning("This Dataset contains some Duplicate values")
        dupli=st.selectbox("Do you want to remove Duplicate Values?",\
                           ("select one", "Yes","No"))
        if dupli=="Yes":
            df=df.drop_duplicates()
            st.text("Duplicate Values are removed")
        if dupli=="No":
            st.text("Keeping duplicated values")    
            
            
# Overall statistics
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(df.describe())
  
if st.button("About App"):
    st.text("Built with Streamlit")
    st.success("Imane")
    
    