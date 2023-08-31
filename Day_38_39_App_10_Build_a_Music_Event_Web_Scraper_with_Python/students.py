import datetime
import time

import pandas as pd

import requests
import selectorlib
import streamlit as st
import plotly.express as px
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

connection = sqlite3.connect('stud.db')

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("Day_38_39_App_10_Build_a_Music_Event_Web_Scraper_with_Python/stu"
                                                     ".yaml")
    value = extractor.extract(source)["temperature"]
    return value


def write_temp_yo_file(extracted):
    temperature = extracted
    date = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    new_rows = (date, temperature)
    coursor = connection.cursor()
    coursor.execute("INSERT INTO students VALUES (?, ?)", new_rows)
    connection.commit()


if __name__ == "__main__":
    st.title('Weather Forecast for the Next Days')
    sourced = scrape(URL)
    extracted = extract(sourced)
    write_temp_yo_file(extracted)
    df = pd.read_csv("Day_38_39_App_10_Build_a_Music_Event_Web_Scraper_with_Python/data2.txt")
    figure = px.line(x=df["date"], y=df["temperature"], labels={"x": "Date", "y": "Temperature (C)"})
    st.plotly_chart(figure)
    time.sleep(2)
