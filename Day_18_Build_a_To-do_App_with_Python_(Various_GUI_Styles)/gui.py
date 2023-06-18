import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        file.write("")

sg.theme('Black')
time_t = sg.Text('', key='clock')
label = sg.Text("Todo List App")
input_box = sg.InputText(tooltip="Enter your todo", key="todo")
add_button = sg.Button(image_source="add.png", size=2, key="Add", tooltip="Add Todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete.png", size=1, key="Complete", tooltip="Complete Todo")
exit_button = sg.Button("Exit")

window = sg.Window(title="Todo List App",
                   layout=[[time_t],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%d/%m/%y %H:%M:%S"))
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo to edit", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select a todo to complete", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
