countries = []

while True:
    chose_country = input("Please pick a country or type Exit, Show: ")
    chose_country = chose_country.capitalize().strip()
    match chose_country:
        case 'Usa':
            print("Hello")
            countries.append(chose_country)
        case 'India':
            print("Namaste")
            countries.append(chose_country)
        case 'Germany':
            print("Hallo")
            countries.append(chose_country)
        case 'Show':
            for country in countries:
                print(country, end=" ")
            break
        case _:
            print("You entered the wrong world. Please try again")

# ingredients = ["john smith", "sen plakay", "dora ngacely"]
#
# for ingredient in ingredients:
#     print(ingredient.title())