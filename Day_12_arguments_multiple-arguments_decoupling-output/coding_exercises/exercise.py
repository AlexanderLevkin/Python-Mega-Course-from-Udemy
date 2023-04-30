def cubic_meter(liters):
    result = liters / 1000
    return print(f"{liters} liters = {result}m3")


cubic_meter(1000)

user_choice = input("Enter the new password: ")


def password_func(password):
    result = {}
    if len(password) >= 8:
        result["lenght"] = True
    else:
        result["lenght"] = False

    uppercase = False
    digit = False

    for i in password:
        if i.isdigit():
            digit = True
            result["digit"] = digit
        if i.isupper():
            uppercase = True
            result["upper"] = uppercase

    if all(result.values()):
        print("Strong Password")
    else:
        print("Weak password")


password_func(user_choice)
