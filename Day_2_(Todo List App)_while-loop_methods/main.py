# user_prompt = "Enter a:"
#
# todos = []
#
# while True:
#     todo1 = input(user_prompt)
#     todo2 = todo1.capitalize()
#     todos.append(todo2)
#     print(todos)

password = input("Enter the password: ")

while password != "pass123":
    password = input("Enter the password: ")

print("Password was correct! ")

# How to find the code you need
dir(str)
help("str".capitalize())
dir([])
