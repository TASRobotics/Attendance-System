import csv

search_value = '26113634'
file_name = 'studentsFeb.csv'

def find_row(file_name, search_value):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if len(row) > 0 and row[0] == search_value:
                return row[1:]
    return None

result = find_row('studentsFeb.csv', search_value)
if result:
    print(result)
else:
    print('Value not found.')