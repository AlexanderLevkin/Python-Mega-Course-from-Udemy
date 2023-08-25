import re

with open("/miracle_in_the_andes.txt", "rb") as file:
    book = file.read().decode("utf-8")

chapter_count = book.count("Chapter")
print(chapter_count)

pattern = re.compile("[^\n]* love[^\n]*.")

print(len(re.findall(pattern, book)))

pattern = re.compile("Chapter [^$]+[A-Z][^$]")

print(re.findall(pattern, book))


def find_words_in_book(book_link, word):
    with open(str(book_link), "rb") as file:
        book = file.read().decode("utf-8")
        pattern = re.compile(f' {word} ')
        findings = re.findall(pattern, book)
        return len(findings)


find_words_in_book("../Day_34_Day_35_Natural_language_processing_of_books_with_python/miracle_in_the_andes.txt", "what")
print(find_words_in_book("../Day_34_Day_35_Natural_language_processing_of_books_with_python/miracle_in_the_andes.txt", "love"))
