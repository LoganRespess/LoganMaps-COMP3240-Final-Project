import PySimpleGUI as sg
import AuburnMap

sg.theme('Dark')
#Layout of left side of Screen. Will have the map.
layoutLeft = [
    [sg.Image(source= "Capture.PNG", size = (250,250))],
]
layoutRight = [
    [sg.Text("From: ")],
    #[sg.MenuBar()]
    [sg.Text("To: ")],
]
layout = [
    [
        sg.Column(layoutLeft),
        sg.VSeperator(),
        sg.Column(layoutRight)
    ]
]
window = sg.Window('Logan Map', layout)

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()