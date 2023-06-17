import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select the file to compress:")
inpu1 = sg.Input()
button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select the destination folder:")
input2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
status_text = sg.Text("", key="status_text", text_color="green")

window = sg.Window("Compress", layout=[[label1, inpu1, button1],
                                       [label2, input2, button2],
                                       [compress_button, status_text]],)
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["status_text"].update("Compression completed")

    window.close()

