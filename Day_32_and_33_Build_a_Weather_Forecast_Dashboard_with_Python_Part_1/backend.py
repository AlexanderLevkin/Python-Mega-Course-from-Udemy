import requests

API_KEY = "2543d18ebc648a443beae795abca745f"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        data = [item['main']['temp'] for item in filtered_data]
    elif kind == "Sky":
        data = [item['weather'][0]['main'] for item in filtered_data]
    return data


if __name__ == '__main__':
    print(get_data(place="Tokyo"))
