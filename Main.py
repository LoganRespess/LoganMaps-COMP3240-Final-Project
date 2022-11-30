import PySimpleGUI as sg
import AuburnMap

sg.theme('Dark')

#Layout of left side of Screen. Will have the map.
layoutLeft = [
    [sg.Image(source = "Map.PNG", size = (750,750))],
]
layoutCenter = [
    [sg.Text("From: ")],
    [sg.OptionMenu(AuburnMap.nodeList, default_value=AuburnMap.nodeList[1])],
    [sg.Text("To: ")],
    [sg.OptionMenu(AuburnMap.nodeList, default_value=AuburnMap.nodeList[5])],
    [sg.Button(button_text="Go.", button_color = "Green", pad = (35,25,0,0), use_ttk_buttons=True, s=(8,1))]
]
layoutRight = [
    [sg.Text("Result: ")]
]
layout = [
    [
        sg.Column(layoutLeft),
        sg.VSeperator(),
        sg.Column(layoutCenter),
        sg.VSeparator(),
        sg.Column(layoutRight)
    ]
]
window = sg.Window('Logan Map', layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()