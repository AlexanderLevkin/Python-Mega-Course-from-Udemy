while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or "new" in user_action:
        todo = user_action[4:]
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif 'edit' in user_action:
        number = user_action[5:]
        number = int(number) - 1
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter the new type: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'exit' in user_action:
        break
    elif 'complete' in user_action:
        number = user_action[9:]
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[int(number) - 1].strip('\n')
        todos.pop(int(todo_to_remove))

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f'Todo {todo_to_remove} was remove from the list'
        print(message)
    else:
        print("Hey! this a wrong word, please try again")

print("Bye!")
