# user_choice = int(input("What is your year of birth?"))
#
#
# def ex_func(year_of_birth, current_year=2023):
#     """EXERCISE 1, 2, 3"""
#     calculte_result = current_year - year_of_birth
#     if year_of_birth >= 120:
#         print("Your age is greater than 120")
#     else:
#         return calculte_result
#
#
# print(ex_func(user_choice))


def names(some_names):
    list_of_names = some_names.split(",")
    return len(list_of_names)


user_choice = input("Enter names separated by commas (no spaces)")

print(names(user_choice))
