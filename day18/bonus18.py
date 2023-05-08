import PySimpleGUI as sg
from zip_creator import make_archive
from zip_extractor import extract_archive

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archive_path = values["archive"]
    destination_folder = values["folder"]
    extract_archive(archive_path, destination_folder)
    window["output"].update(value="Extraction completed!")

window.close()
