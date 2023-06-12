import PySimpleGUI as sg

label1 = sg.Text("Select the file to compress:")
inpu1 = sg.Input()
button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select the destination folder:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("Compress", layout=[[label1, inpu1, button1],
                                       [label2, input2, button2],
                                       [compress_button]])
window.read()
window.close()

