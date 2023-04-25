password = input("enter a new password: ")

if len(password) > 7 and password.isdigit():
    print("Password is ok, but not too strong")
elif len(password) > 7:
    print("Great password there!")
else:
    print("Your password is weak!")

