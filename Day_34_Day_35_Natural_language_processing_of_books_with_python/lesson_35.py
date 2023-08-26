import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Loading the book
with open("../Day_34_Day_35_Natural_language_processing_of_books_with_python/miracle_in_the_andes.txt", "rb") as file:
    book = file.read().decode("utf-8")

# The most used words
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
#print(len(findings))

d ={}

for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for key, value in d.items()]
#print(sorted(d_list, reverse=True))


english_stopwords = stopwords.words("english")

filtered_words = []

for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))
print(filtered_words[:10])

# Sentiment Analysis

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores('Hey, look how beautiful the day is')

if scores['pos'] > scores['neg']:
    print("The sentence is positive")
else:
    print("The sentence is negative")

scores = analyzer.polarity_scores(book)
if scores['pos'] > scores['neg']:
    print("The Chapter is positive")
else:
    print("The Chapter is negative")

pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
chapters = chapters[1:]

for chapter in chapters:
    scores = analyzer.polarity_scores(chapter)
    print(scores)