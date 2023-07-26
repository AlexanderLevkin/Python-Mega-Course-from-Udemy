import streamlit as st
import pandas as pd

PATH = "Day_22_Build_a_Project_Showcase_Website_with_Python_Part2/my_own_web_site/images_1"

st.set_page_config(layout="wide")
df = pd.read_csv("Day_22_Build_a_Project_Showcase_Website_with_Python_Part2/my_own_web_site/data_1.csv", sep=",")


st.header("The Best Company")
content = """This is the best company ever, I love it"""
st.write(content)
st.subheader("Our Team")

member_column1, member_column2, member_column3 = st.columns(3)

with member_column1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"]} {row["last name"]}'.title())
        st.write(row["role"])
        st.image(f"{PATH}/{row['image']}")

with member_column2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"]} {row["last name"]}'.title())
        st.write(row["role"])
        st.image(f"{PATH}/{row['image']}")

with member_column3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"]} {row["last name"]}'.title())
        st.write(row["role"])
        st.image(f"{PATH}/{row['image']}")


