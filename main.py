import PySimpleGUI as sg # pip install pysimplegui
import csv
import datetime as dt # pip install datetime
import pandas as pd # pip install pandas

# setup for the date and time
currentDate = dt.date.today()

# All the stuff inside your window.
sg.theme('DarkAmber')   #TODO: Change color theme
layout = [  [sg.Text('Welcome To Raid One/Zero')],
            [sg.Text('TAS ID:'), sg.InputText()],
            [sg.Text('Name:'), sg.InputText()],
            [sg.Text('Subteam:'), sg.Combo(['Programming', 'Mechanical', 'Electrical'])],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Attendance System', layout)

while True:

    # read the values in the window
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    # selects the right file for what month it is (makes it easier to check the attendance)
    if currentDate.month == 1:
        filename = "studentsJan.csv"
    elif currentDate.month == 2:
        filename = "studentsFeb.csv"
    elif currentDate.month == 3:
        filename = 'studentsMar.csv'
    elif currentDate.month == 4:
        filename = 'studentsApril.csv'
    elif currentDate.month == 5:
        filename = 'studentsMay.csv'

    # the student values based on what they type
    students = [
    {'id': values[0], 'name': values[1], 'subteam': values[2], 'timeAdded': currentDate}
]
    # The fields for the csv files
    fields = ['id', 'name', 'subteam', 'timeAdded']

    # appends it onto the csv file
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writerows(students)
    #TODO: If already entered give task if not entered ask for name and subteam

    # gives tasks based on what they choose
    if values[2] == 'Programming':
        sg.popup('programming task')
    elif values[2] == 'Mechanical':
        sg.popup('Mech task')
    elif values[2] == 'Electrical':
        sg.popup('electrical task')

window.close()

