import requests
from send_email import send_email

api_key = "fd4697569828499f94d602ea82852a3a"

url = ("https://newsapi.org/v2/everything?q=tesla&from=2023-07-10&sortBy=publishedAt&apiKey"
       "=fd4697569828499f94d602ea82852a3a")

response = requests.get(url)
content = response.json()

body = ''

for article in content['articles']:
    if article['title'] is not None:
        body += article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode('utf-8')
send_email(body)
