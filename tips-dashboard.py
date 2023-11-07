import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tips Dashboard",
                   page_icon=None, 
                   layout="wide", 
                   initial_sidebar_state="expanded")
# data
df = pd.read_csv('tips.csv')

# sidebar
st.sidebar.header("Tips Dashboard")
st.sidebar.write("This dashboard is all about tips in a resturant")
st.sidebar.image('tips.jpg')
cat_filter = st.sidebar.selectbox("Categorical Filtering", [None, 'sex', 'smoker', 'day'])
num_filter = st.sidebar.selectbox("Numerical Filtering", [None, 'total_bill','tip'])

# graphs
st.subheader('Comparison between Total Bill vs. Tips')
fig = px.scatter(data_frame=df, x='total_bill', y='tip', color=cat_filter, size=num_filter)
st.plotly_chart(fig)

c1, c2 = st.columns(2)

with c1:
    st.subheader("Gender")
    fig = px.bar(data_frame=df, x='sex')
    st.plotly_chart(fig)

with c2:
    st.subheader("Smoking")
    fig = px.pie(data_frame=df, names='smoker')
    st.plotly_chart(fig)