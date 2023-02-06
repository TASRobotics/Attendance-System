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
            [sg.Text('Raid One Or Raid Zero'), sg.Combo(['Raid One', 'Raid Zero'])],
            [sg.Text('Subteam:'), sg.Combo(['Programming', 'Mechanical', 'Electrical', 'Design', 'Statistics', 'Logistics'])],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Attendance System', layout)

while True:

    # read the values in the window
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    # selects the right file for what month it is (makes it easier to check the attendance)
    if currentDate.month == 1 and values[2] == 'Raid One':
        filename = "oStudentsJan.csv"
    elif currentDate.month == 1 and values[2] == 'Raid Zero':
        filename = 'zStudentsJan.csv'
    elif currentDate.month == 2 and values[2] == 'Raid One':
        filename = "oStudentsFeb.csv"
    elif currentDate.month == 2 and values[2] == 'Raid Zero':
        filename = 'zStudentsFeb.csv'
    elif currentDate.month == 3 and values[2] == 'Raid One':
        filename = 'oStudentsMar.csv'
    elif currentDate.month == 3 and values [2]== 'Raid Zero':
        filename = 'zStudentsMar.csv'
    elif currentDate.month == 4 and values [2] == 'Raid One':
        filename = 'oStudentsApril.csv'
    elif currentDate.month == 4 and values[2] == 'Raid Zero':
        filename = 'zStudentsApril.csv'
    elif currentDate.month == 5 and values[2] == 'Raid One':
        filename = 'oStudentsMay.csv'
    elif currentDate.month == 5 and values[2] == 'Raid Zero':
        filename = 'zStudentsMay.csv'

    # the student values based on what they type
    students = [
    {'id': values[0], 'name': values[1], 'team': values[2], 'subteam': values[3], 'timeAdded': currentDate}
]
    # The fields for the csv files
    fields = ['id', 'name', 'subteam', 'team', 'timeAdded']

    # appends it onto the csv file
    with open(filename, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writerows(students)
    #TODO: If already entered give task if not entered ask for name and subteam

    # gives tasks based on what they choose
    #TODO: Give a task
    if values[3] == 'Programming' and values[2]:
        sg.popup('programming task')
    elif values[3] == 'Mechanical':
        sg.popup('Mech task')
    elif values[3] == 'Electrical':
        sg.popup('electrical task')
    elif values[3] == 'Design':
        sg.popup('design task')
    elif values[3] == 'Statistics':
        sg.popup('Stats task')
    elif values[3] == 'Logistics':
        sg.popup('Logistics task')

window.close()
