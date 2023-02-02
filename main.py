import PySimpleGUI as sg # pip install pysimplegui
import csv
import datetime as dt # pip install datetime

# setup for the date and time
currentDate = dt.date.today()

# the fields for the csv files
fields = ['id', 'name', 'subteam', 'timeAdded']

sg.theme('DarkAmber')   #TODO: Change color theme
# All the stuff inside your window.
layout = [  [sg.Text('Welcome To Raid One/Zero')],
            [sg.Text('TAS ID:'), sg.InputText()],
            [sg.Text('Name:'), sg.InputText()],
            [sg.Text('Subteam:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Attendance System', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    #TODO: If already entered give task if not entered ask for name and subteam

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

    # the student id number
    students = [
    {'id': values[0], 'name': values[1], 'subteam': values[2], 'timeAdded': currentDate}
]
    
    with open(filename, 'w') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames = fields)

        writer.writeheader()

        writer.writerows(students)
window.close()

