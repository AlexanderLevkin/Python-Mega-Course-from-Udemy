temperatures = [10, 12, 14]
temperatures = [str(item) + "\n" for item in temperatures]
file = open("file.txt", 'w')

file.writelines(temperatures)

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)
