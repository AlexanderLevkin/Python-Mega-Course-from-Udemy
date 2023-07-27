# my solution:
# while True:
#     data = input("Throw the coin and enter head or tail here or type exit:")
#     if data == "exit":
#         print("Bye! Bye!")
#         break
#     elif data not in ["head", "tail"]:
#         print("You typed the wrong words or characters")
#     else:
#         with open("content/count.txt") as file:
#             sum_ = file.readlines()
#             sum_.append(data + "\n")
#             list_of_head = [item for item in sum_ if item.strip() == "head"]
#         with open("content/count.txt", "w") as file:
#             file.writelines(sum_)
#         final_output = len(list_of_head) / len(sum_) * 100
#         print(f"Heads: {final_output}")

# Ardit solution
while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")
    if side.strip() == "exit":
        break