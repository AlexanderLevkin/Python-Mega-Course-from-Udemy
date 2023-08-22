import streamlit as st
import plotly.express as px
from backend import get_data

# Add a title, a subtitle, and some text
st.title('Weather Forcast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forcast Days: ', min_value=1, max_value=5, help='Select the number of days or forecasted days')

option = st.selectbox(
    'Select data to view', ('Temperature', 'Sky')
)

st.subheader(f"{option} Forecast for {days} days in {place}")

if place:
    # Get temperature and sky data
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        temperature = [float(item['main']['temp'])-32 / 1.8 for item in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
    if option == 'Sky':
        data = [item['weather'][0]['main'] for item in filtered_data]

        sky_conditions = {
            'Clear': 'Day_32_and_33_Build_a_Weather_Forecast_Dashboard_with_Python_Part_1/img/clear.png',
            'Clouds': 'Day_32_and_33_Build_a_Weather_Forecast_Dashboard_with_Python_Part_1/img/cloud.png',
            'Rain': 'Day_32_and_33_Build_a_Weather_Forecast_Dashboard_with_Python_Part_1/img/rain.png',
            'Snow': 'Day_32_and_33_Build_a_Weather_Forecast_Dashboard_with_Python_Part_1/img/snow.png'
        }
        pictures = [sky_conditions[item] for item in data]
        st.image(pictures, width=115)
