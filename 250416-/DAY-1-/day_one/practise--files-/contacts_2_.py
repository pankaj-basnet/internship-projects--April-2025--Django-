import os
import csv


print("=================================")

############ WRITING ON csv file
############ csv.DictWriter

csv_file = "day-1-fair-.csv"

# number = int(input("enter a number : "))
# name = input("enter a name : ")
# date = input("enter a date eg, 25/04/16 : ")
# email = input("enter a email : ")

# headings = ["number", "name", "date", "email" ]


if not os.path.exists(csv_file):
    csv_file_write = open(csv_file, 'w', )
    headings = ["number", "name", "date", "email" ]

    # contact_writer = csv.DictWriter(csv_file_write, fieldnames= headings)
    contact_writer = csv.DictWriter(csv_file_write, fieldnames= ["number", "name", "date", "email" ])

    # contact_writer.writerow({ "number": "2025", "name":"Monica 555", "date":"July 1, 2015", "email":"Republican55"})


else:
    csv_file_write = open(csv_file, 'a', newline='')
    headings = ["number", "name", "date", "email" ]

    # contact_writer = csv.DictWriter(csv_file_write, fieldnames= headings)
    contact_writer = csv.DictWriter(csv_file_write, fieldnames= ["number", "name", "date", "email" ])

contact_writer.writerow({ "number": "2666", "name":"Monica 666", "date":"July 1, 2666", "email":"Republican666"})


csv_file_write.close()


print("=================================")

with open('day-1-fair-.csv', 'r', newline='') as csv_file_reader:
    contact_reader = csv.DictReader(csv_file_reader,)
    for row in contact_reader:
        print('----------')
        print(row)

print('----------')
print("=================================")
