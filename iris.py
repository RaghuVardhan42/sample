import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.text_input("username")

uploaded_file = st.file_uploader("Upload Files",type=['csv'])

butt=st.button("submit")
if (butt==True):
    df=pd.read_csv(uploaded_file)
    st.write(df.head())
    
    fig = px.scatter(x=df["sepal.length"],y=df["petal.length"],)
    fig.update_layout(xaxis_title="sepal length",yaxis_title="petal length",)

    st.write(fig)
