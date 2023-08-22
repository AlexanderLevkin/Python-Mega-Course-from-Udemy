import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('D:\PycharmProjects\Python-Mega-Course-from-Udemy\Day_32_Build_a_Weather_Forecast_Dashboard_with_'
                 'Python_Part_1\Students_practices\happy.csv')

gdp = df['gdp']
happiness = df['happiness']
social_support = df['social_support']

st.title('In Search for Happiness')

x = st.selectbox(
    "Select the data for the X-axis", ("Happiness", "GDP", "Social Support")
)

y = st.selectbox(
    "Select the data for the Y-axis", ("Happiness", "GDP", "Social Support")
)

st.subheader(f"{x} vs {y}")

data = {
    "Happiness": happiness,
    "GDP": gdp,
    "Social Support": social_support
}

x_array = data.get(x, None)
y_array = data.get(y, None)

fig = px.scatter(x=x_array, y=y_array, labels={"x": x, "y": y})
st.plotly_chart(fig)
