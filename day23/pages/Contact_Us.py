import streamlit as st
from send_email import send_email
import pandas

# st.header("Contact Me")
#
# with st.form(key="email_form"):
#     user_email = st.text_input("Enter your email address")
#     raw_message = st.text_area("Your message here")
#     message = f"""\
# Subject: New email from {user_email}
#
# From: {user_email}
# {raw_message}
# """
#     submit_button = st.form_submit_button("Submit")
#     if submit_button:
#         send_email(message)
#         st.info("Email was send successfully!")

topics = pandas.read_csv("topics.csv")
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address")
    select_box = st.multiselect("What topic do you want to discuss?", topics["topic"])
    raw_message = st.text_area("Your message here")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {select_box}
{raw_message}
"""

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Email was send successfully!")
