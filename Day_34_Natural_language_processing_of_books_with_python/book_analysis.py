import re

with open("../Day_34_Natural_language_processing_of_books_with_python/miracle_in_the_andes.txt", "rb") as file:
    book = file.read().decode("utf-8")

chapter_count = book.count("Chapter")
print(chapter_count)


# with regex

pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book)

print(len(findings))