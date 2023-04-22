while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':  # | - it is "OR"
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            #new_todo = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todo):
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new type: ")
            todos[number] = new_todo
        case 'exit':
            break
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case _:
            print("Hey! this a wrong word, please try again")

print("Bye!")
