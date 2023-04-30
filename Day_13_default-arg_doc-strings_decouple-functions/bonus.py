feet_inches = input("Enter feet and inches: ")


def parse(feet_inches_arg):
    parts = feet_inches_arg.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert():
    parsed = parse(feet_inches)
    meters = round(parsed['feet'] * 0.3048 + parsed['inches'] * 0.0254)
    return f"{parsed['feet']} feet and {parsed['inches']} inches is equal {meters} meters"


print(convert())
