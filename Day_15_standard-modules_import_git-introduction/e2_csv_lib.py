import csv

with open('weather.csv', 'r') as csv_file:
    data = list(csv.reader(csv_file))


city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
