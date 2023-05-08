import PySimpleGUI as sg
from convert import convert

label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inch")

meters = sg.Text(key="output")

convert_button = sg.Button("Convert")
window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button, meters]])

while True:
    event, values = window.read()
    match event:
        case "Convert":
            print(event, values)
            feet = float(values["feet"])
            inch = float(values["inch"])
            result = convert(feet, inch)
            window["output"].update(value=f"{result} m")
        case sg.WIN_CLOSED:
            break

window.close()
