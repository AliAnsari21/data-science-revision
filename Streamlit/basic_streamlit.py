import streamlit as st
import pandas as pd
import numpy as np

#title of the application
st.title("Hello Streamlit")

#display a simple text
st.write("this is a simple text")

#create a simple dataframe
df=pd.DataFrame({
    'first columns':[1,2,3,4],
    'second columns':[10,20,30,40]
})

#display the dataframe
st.write("here is the dataframe")
st.write(df)

#create a line chart
chart_data=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)