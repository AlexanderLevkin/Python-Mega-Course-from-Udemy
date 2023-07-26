import streamlit as st
import pandas as pd

PATH = "D:\PycharmProjects\Python-Mega-Course-from-Udemy\Day_22_Build_a_Project_Showcase_Website_with_Python_Part2\images"

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(f"{PATH}/photo.jpg", width=700)

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("D:\PycharmProjects\Python-Mega-Course-from-Udemy\Day_22_Build_a_Project_Showcase_Website_with_Python_Part2\data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"{PATH}/{row['image']}")
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"{PATH}/{row['image']}")
        st.write(f'[Source Code]({row["url"]})')
