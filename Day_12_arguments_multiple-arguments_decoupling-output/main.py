def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos('files/todos.txt')

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = user_action[5:]
            number = int(number) - 1

            todos = get_todos('files/todos.txt')

            new_todo = input("Enter the new type: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
        continue
    elif user_action.startswith('exit'):
        break
    elif user_action.startswith('complete'):
        try:
            number = user_action[9:]
            todos = get_todos('files/todos.txt')

            todo_to_remove = todos[int(number) - 1].strip('\n')
            todos.pop(int(todo_to_remove))

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todo_to_remove} was remove from the list'
            print(message)
        except IndexError:
            print("There is no item with that number.")
        continue
    else:
        print("Hey! this a wrong word, please try again")

print("Bye!")
