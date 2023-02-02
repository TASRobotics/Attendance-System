import PySimpleGUI as sg # pip install pysimplegui
import csv

sg.theme('DarkAmber')   #TODO: Change color theme
# All the stuff inside your window.
layout = [  [sg.Text('Welcome To Raid One/Zero')],
            [sg.Text('Please Enter Your TAS ID'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Attendance System', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    #TODO: If already entered give task if not entered ask for name and subteam
    

window.close()

