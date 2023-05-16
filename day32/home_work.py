import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("happy.csv")
st.title("In Search for Happiness")
first_option = st.selectbox("Select data to view", ("GDP", "Happiness", "Generosity"))
second_option = st.selectbox("Select the data for Y-axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{first_option} and {second_option}")


def get_data(first_option_, second_option_):
    first_option_data = df[first_option_.lower()]
    second_option_data = df[second_option_.lower()]
    return first_option_data, second_option_data


d, t = get_data(first_option, second_option)
figure = px.scatter(x=d, y=t, labels={"x": first_option, "y": second_option})
st.plotly_chart(figure)

