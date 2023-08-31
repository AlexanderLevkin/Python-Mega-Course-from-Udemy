import smtplib
import sqlite3
import ssl
import time

import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"
connection = sqlite3.connect('data.db')


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(reciver, message):
    host = "smtp.gmail.com"
    port = 465
    username = "yRqoM@example.com"
    password = "password"
    reciver = reciver
    message = message
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciver, message)
    print("Email sent!")


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?, ?, ?)", row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows


if __name__ == "__main__":
    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)

        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
            print(row)
        time.sleep(2)
