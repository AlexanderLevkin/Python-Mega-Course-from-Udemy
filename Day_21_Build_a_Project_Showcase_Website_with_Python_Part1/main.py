import streamlit as st
PATH = "Day_21_Build_a_Project_Showcase_Website_with_Python_Part1/images/"


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(f"{PATH}photo.jpg", width=700)

with col2:
    st.write("Levkin Alexander")
    content = """
    Hi my name is Levkin Alexander. I am a software engineer. I love coding! I love to learn new things. I love to code.
    I have been coding for 1 years now. 
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me
"""
st.write(content2)
