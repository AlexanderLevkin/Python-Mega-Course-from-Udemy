password = input("Enter new password:")
result = {}
if len(password) >= 8:
    result["len"] = True
else:
    result["len"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result['uppercase'] = uppercase

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")


