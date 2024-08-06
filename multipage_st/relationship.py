import streamlit as st
import string
import pandas as pd

datapath="C:/Users/nebiy/Documents/ayder-dash board/fake_data.csv"
df=pd.read_csv(datapath)

#rename the columns of the dataset
df.columns=[col for col in string.ascii_lowercase[:len(df.columns)]]

def app():
    x_col=st.selectbox('select x axis',df.columns)
    y_col=st.selectbox('select y axis',df.columns)

    st.bar_chart(df[[x_col,y_col]])
