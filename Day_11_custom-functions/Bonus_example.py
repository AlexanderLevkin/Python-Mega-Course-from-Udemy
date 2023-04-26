from statistics import mean


def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()
    list_of_temp = [float(item.strip()) for item in data if item.strip().isdigit()]
    av = mean(list_of_temp)
    return av


average = get_average()
print(average)
