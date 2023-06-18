import PySimpleGUI as sg
from cli import converter

text_feet = sg.Text("Enter feet:")
text_inches = sg.Text("Enter inches:")

input_feet = sg.Input(key="feet")
input_inches = sg.Input(key="inches")
convert_button = sg.Button("Convert", key="convert")
status_text = sg.Text("", key="status_text")
exit_button = sg.Button("Exit")

col1 = sg.Column([[text_feet, input_feet]])
col2 = sg.Column([[text_inches, input_inches]])

layout = [[col1, col2],
          [convert_button, exit_button, status_text]]

window = sg.Window("Convertor", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "convert":
        feet = values["feet"]
        inches = values["inches"]
        result = converter(feet, inches)
        window["status_text"].update(f"{result} m", text_color="green")

window.close()
