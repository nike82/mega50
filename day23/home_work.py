import streamlit as st
import pandas

st.set_page_config(layout="wide")

# column1, column2 = st.columns(2)
#
# with column1:
#     st.image("images/photo.png", width=600)
# with column2:
#     st.title("Never did backups!!!")
#     content = """
#     Hi! That guy never performed DBs backups and one day he paid his
# debts! The clue is: DO NOT PASS ON BACKUPS!
#     """
#     st.info(content)

st.title("The Best Company")

content1 = """
Below you can find some of the apps I have built in Python. Have a fun!
"""
st.write(content1)

st.subheader("Our Team")

column1, empty_column1, column2, empty_column2, column3 = st.columns([1.0, 0.2, 1.0, 0.2, 1.0])
data_frame = pandas.read_csv("data_hw.csv")

with column1:
    for index, row in data_frame[:4].iterrows():
        # st.header(row["first name"].title() + " " + row["last name"].title())
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images_hw/" + row["image"])

with column2:
    for index, row in data_frame[4:8].iterrows():
        # st.header(row["first name"].title() + " " + row["last name"].title())
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images_hw/" + row["image"])

with column3:
    for index, row in data_frame[8:].iterrows():
        # st.header(row["first name"].title() + " " + row["last name"].title())
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images_hw/" + row["image"])
