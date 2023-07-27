import smtplib, ssl
import os


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
