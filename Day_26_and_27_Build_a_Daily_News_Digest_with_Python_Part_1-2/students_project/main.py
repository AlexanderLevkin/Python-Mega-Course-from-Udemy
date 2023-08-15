import requests
import streamlit as st


api_key = "HnVhftYeseLgQoFAvEfc4RmvlL84MZ1AcaVeBprC"

response = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key)

title = response.json()['title']
article = response.json()['explanation']
url_img = requests.get(response.json()['hdurl'])

with open("img.jpg", "wb") as file:
    file.write(url_img.content)


st.set_page_config("wide")
st.header(title + "\n")
st.image("img.jpg", width=700)
st.info(article)
