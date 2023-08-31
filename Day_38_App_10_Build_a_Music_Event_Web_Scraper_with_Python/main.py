import smtplib
import ssl
import time

import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"


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
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")


def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)

        content = read(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email("yRqoM@example.com", extracted)
        time.sleep(2)
