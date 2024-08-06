import streamlit as st
import string
import pandas as pd

datapath="C:/Users/nebiy/Documents/ayder-dash board/fake_data.csv"
df=pd.read_csv(datapath)

#rename the columns of the dataset
df.columns=[col for col in string.ascii_lowercase[:len(df.columns)]]

def app():
    column_name=st.selectbox('Select a column',df.columns)

    st.bar_chart(df[column_name].value_counts())