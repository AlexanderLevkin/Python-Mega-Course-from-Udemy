import streamlit as st
from ..send_email import send_email

st.header("Contact Me")

with st.form(key="my_form"):
    user_email = st.text_input(label="Your email address")
    raw_message = st.text_area(label="Message")
    button = st.form_submit_button(label="Submit")

    message = f"""
    Subject: New email from {user_email}
    From: {user_email}
    Message: {raw_message}
    """

    if button:
        send_email(reciver=user_email, message=message)
        st.info("Email sent")


