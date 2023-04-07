# EX 1

# dollar_amount = input("Please enter the dollar amount: ")
# euro_k = 0.95
# convert_result = float(dollar_amount) * euro_k
#
# print(f"The amount in euros is: {round(convert_result, 2)}")

# EX 2

# ranking = ['John', 'Sen', 'Lisa']
# user_choice = int(input("Enter the rank number: "))
# user_choice = user_choice - 1
# print(ranking[user_choice])

# EX 3

ranking = ['John', 'Sen', 'Lisa']
user_choice = input("Enter a name: ")
rank = ranking.index(user_choice) + 1
print(rank)

