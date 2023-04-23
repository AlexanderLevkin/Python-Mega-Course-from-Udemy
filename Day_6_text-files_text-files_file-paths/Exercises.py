# Exercises 1
# file = open("./files/essay.txt", 'r')
# content = file.read().title()
# print(content)

# Exercises 2
# file = open("./files/essay.txt", 'r')
# content = file.read()
# print(len(content))

# Exercises 3

# user_in = input("Add a new member:\n")
# file = open("./files/members.txt", 'r')
# content = file.readlines()
# file.close()
# content.append(user_in + "\n")
# file = open("./files/members.txt", 'w')
# file.writelines(content)
# file.close()

# Exercises 4

# words = "Hello"
# docs = ["doc.txt", "hello.txt", "join.txt"]
#
# for doc in docs:
#     file = open(f"./files/{doc}", 'w')
#     file.write(words)
#     file.close()

# Exercises 5
list_of_num = ["a.txt", "b.txt", "c.txt"]

for item in list_of_num:
    file = open(f"./files/{item}", 'r')
    print(file.read())
    file.close()
