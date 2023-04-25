try:
    total_value = int(input("Enter total value: "))
    value = int(input("Enter value: "))
    final = value / total_value * 100
    print(f"{final}%")
except ValueError:
    exit("you need to enter a number. Run the program again")
except ZeroDivisionError:
    print("Your total value cannot be zero")

