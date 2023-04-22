while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':  # | - it is "OR"
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the new type: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'exit':
            break
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(int(todo_to_remove))

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todo_to_remove} was remove from the list'
            print(message)
        case _:
            print("Hey! this a wrong word, please try again")

print("Bye!")
