import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('/content/dataset.csv')

data = data_path()

# Simple Streamlit app using Plotly
st.title("Streamlit Dashboard with Plotly")
st.write("This is a simple example dashboard with Plotly visualizations.")


fig = px.line(data, x="year", y="population", color="sex", title="Total inactive population by year and sex")
fig = px.bar(data, x="year", y="population", color="sex", title="Total inactive population by year and sex")
fig = px.line(data, x="year", y="population", color="sex", title="Total unemployed population by year and sex")
fig = px.bar(data, x="year", y="population", color="sex", title="Total unemployed population by year and sex")
fig = px.line(data, x="year", y="population", color="sex", title="Total employed population by year and sex")
fig = px.bar(data, x="year", y="population", color="sex", title="Total employed population by year and sex")

st.plotly_chart(fig)