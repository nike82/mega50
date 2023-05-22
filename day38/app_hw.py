import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data_hw.txt")
figure = px.line(x=df["date"], y=df["temperature"], labels={"x": "date", "y": "temperature"})
st.plotly_chart(figure)
