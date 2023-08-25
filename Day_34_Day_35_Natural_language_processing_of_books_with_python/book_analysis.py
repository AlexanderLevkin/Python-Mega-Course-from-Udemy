import re

with open("../Day_34_Day_35_Natural_language_processing_of_books_with_python/miracle_in_the_andes.txt", "rb") as file:
    book = file.read().decode("utf-8")

chapter_count = book.count("Chapter")
print(chapter_count)

# with regex

pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book)

print(len(findings))

# Which are the sentences that contain the word “Love”?

pattern = re.compile('[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z][^.]*.')

findings = re.findall(pattern, book)
print(len(findings))

# What are the most used words?

pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
print(len(findings))

d ={}

for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for key, value in d.items()]
sorted(d_list, reverse=True)

print(sorted(d_list, reverse=True))