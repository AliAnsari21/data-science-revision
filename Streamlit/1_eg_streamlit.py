import streamlit as st
import pandas as pd
import numpy as np

st.title("streamlit text input")

name=st.text_input("enter your name")
age=st.slider("select your age:",0,100,25)
st.write(f'your age is {age}')

if name:
    st.write(f'hello ,{name}')

options=["python","c++","java","html"]
choice=st.selectbox("choose your favorite language",options)
st.write(f'you selected {choice}')

data={
    "name":['john','lisa','jay'],
    "age":[23,31,26],
    "city":["mumbai","thane","mumbra"]
}

df=pd.DataFrame(data)
df.to_csv("samplesata.csv")
st.write(df)

upload_file=st.file_uploader("choose a csv file",type="csv")

if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)