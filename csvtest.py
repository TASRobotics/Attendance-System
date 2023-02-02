import csv
import datetime as dt

currentDate = dt.date.today()

students = [
    {'id': '26113634', 'name': 'Theo Fagen', 'subteam': 'Programming', 'timeAdded': currentDate}
]

fields = ['id', 'name', 'subteam', 'timeAdded']

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

with open(filename, 'w') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames = fields)

    writer.writeheader()

    writer.writerows(students)