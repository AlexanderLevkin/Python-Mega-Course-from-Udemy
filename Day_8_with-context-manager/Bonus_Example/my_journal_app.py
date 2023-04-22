date = input("Enter today's date:")
question = input("How do you rate your mood today from 1 to 10?: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"journal/{date}.txt", "w") as file:
    content = file.writelines(f'the mood :{question}\nflow from today is: {thoughts}\n\n')




