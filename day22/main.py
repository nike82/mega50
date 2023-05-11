import streamlit as st
import pandas

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.png", width=600)
with column2:
    st.title("Never did backups!!!")
    content = """
    Hi! That guy never performed DBs backups and one day he payed his
debts! The clue is: DO NOT PASS ON BACKUPS!
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Have a fun!
"""
st.write(content2)

column3, empty_column, column4 = st.columns([1.5, 0.5, 1.5])
data_frame = pandas.read_csv("data.csv", sep=";")

with column3:
    for index, row in data_frame[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with column4:
    for index, row in data_frame[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
