import pandas
import pandas as pd
from flask import Flask, render_template

app = Flask("__name__")

station = pd.read_csv("..\Day_30_Build_a_Historical_Weather_Data_API_with_Python_(Part_2)\data_small\stations.txt",
                      skiprows=17)
station = station[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", data=station.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = ("D:\PycharmProjects\Python-Mega-Course-from-Udemy"
                + "\Day_30_Build_a_Historical_Weather_Data_API_with_Python_(Part_2)\data_small\TG_STAID" +
                str(station).zfill(6) + ".txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = ("D:\PycharmProjects\Python-Mega-Course-from-Udemy"
                + "\Day_30_Build_a_Historical_Weather_Data_API_with_Python_(Part_2)\data_small\TG_STAID" +
                str(station).zfill(6) + ".txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/yearly/<station>//<year>")
def yearly(station,year):
    filename = ("D:\PycharmProjects\Python-Mega-Course-from-Udemy"
                + "\Day_30_Build_a_Historical_Weather_Data_API_with_Python_(Part_2)\data_small\TG_STAID" +
                str(station).zfill(6) + ".txt")
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict()
    return result

if __name__ == "__main__":
    app.run(debug=True, port=5001)
