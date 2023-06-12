import PySimpleGUI as sg

text1 = sg.Text("Enter feet")
input_box = sg.Input()
text2 = sg.Text("Enter inches")
input_box2 = sg.Input()
button = sg.Button("Convert")


window = sg.Window("Converter", layout=[[text1, input_box], [text2, input_box2], [button]])
window.read()
window.close()

