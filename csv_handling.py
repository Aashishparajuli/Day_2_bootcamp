import csv

with open('student.csv') as file:
    rows = csv.DictReader(file)
    #print(file.read())
    for row in rows:
        print(row['email'])
        