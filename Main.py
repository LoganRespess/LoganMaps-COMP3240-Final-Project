import PySimpleGUI as sg
import AuburnMap

sg.theme('Dark')


pathResult = "Cuck"
lengthResult = ""
timeResult = ""

#Layout of left side of Screen. Will have the map.
layoutLeft = [
    [sg.Image(source = "Map.PNG", size = (750,750))],
]
layoutCenter = [
    [sg.Text("From: ")],
    [sg.OptionMenu(AuburnMap.nodeList, default_value=AuburnMap.nodeList[1], key = "-FROM-")],
    [sg.Text("To: ")],
    [sg.OptionMenu(AuburnMap.nodeList, default_value=AuburnMap.nodeList[5], key = "-TO-")],
    [sg.Button(button_text="Go.", button_color = "Green", pad = (35,25,0,0), use_ttk_buttons=True, s=(8,1))]
]
layoutRight = [
    [sg.Text("Result: ", pad = (0,0,250,0))],
    [sg.Text(key="-PATH-")],
    [sg.Text(key="-LENGTH-")],
    [sg.Text(key="-TIME-")]
    
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
    if event == "Go.":
        resultList = AuburnMap.result(values["-FROM-"], values["-TO-"])
        pathResult = resultList[0]
        lengthResult = resultList[1]
        timeResult = resultList[2]
        window["-PATH-"].update(pathResult)
        window["-LENGTH-"].update(lengthResult)
        window["-TIME-"].update(timeResult)

window.close()