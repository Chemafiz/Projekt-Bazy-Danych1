import PySimpleGUI as sg

option = []
layout = [
    [sg.Text("Select options:")],
    [sg.Checkbox("Option 1", key="option1")],
    [sg.Button("OK")]
]

window = sg.Window("Example", layout)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "OK"):
        break

    if event == "OK":
        option.append(str(values["option1"]))

window.close()
print(option)