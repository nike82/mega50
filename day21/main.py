import streamlit as st

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.png", width=550)
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

