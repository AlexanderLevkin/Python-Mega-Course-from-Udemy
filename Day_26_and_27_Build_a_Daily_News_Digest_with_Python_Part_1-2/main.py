import requests
from send_email import send_email

topic = "tesla"
api_key = "fd4697569828499f94d602ea82852a3a"
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2023-07-10&sortBy=publishedAt&apiKey"
       "=fd4697569828499f94d602ea82852a3a&language=en")

response = requests.get(url)
content = response.json()

body = ''

for article in content['articles'][0:20]:
    if article['title'] is not None:
        body += "Subject: Today's news" + article['title'] + '\n' + article['description'] + "" + "\n" + 2*'\n'

body = body.encode('utf-8')
send_email(body)
