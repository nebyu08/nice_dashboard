import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


datapath="C:/Users/nebiy/Documents/ayder-dash board/fake_data.csv"
df=pd.read_csv(datapath)

#changing the values into integers
df=df.astype(int)

def app():
    plt.figure(figsize=(18,19))
    #sns.heatmap(df,annot=True,cmap='YlGnBu',cbar=True)
    fig=px.imshow(df,text_auto=True)
    #plt.title("heat map of the data")
    #plt.show()
    st.plotly_chart(fig)

#run the app
if __name__=="__main__":
    app()