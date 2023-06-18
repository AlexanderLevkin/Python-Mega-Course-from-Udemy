def converter(feets, inches):
    feet = int(feets)
    inch = int(inches)
    feet_to_meter = feet / 3
    inches_to_meter = inch * 0.0254
    return feet_to_meter + inches_to_meter


if __name__ == '__main__':
    print(converter(3, 4))
