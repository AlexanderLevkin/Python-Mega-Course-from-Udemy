import functions as f
import PySimpleGUI as sg

label = sg.Text("Todo List App")
input_box = sg.InputText(tooltip="Enter your todo", key="-INPUT-")
add_button = sg.Button("Add")

window = sg.Window(title="Todo List App", layout=[[label], [input_box, add_button]])
window.read()
window.close()

