todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':  # | - it is "OR"
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1}-{item}")
            print(len(todos))
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
