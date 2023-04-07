todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':  # | - it is "OR"
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter the new type: ")
            todos[number] = new_todo
        case _:
            print("Hey! this a wrong word, please try again")

print("Bye!")
 