import csv
import os

print('----------------------------------------------')
print('----------------------------------------------')

############ READING csv file
############ csv.DictReader

csv_file = "day-1-fair-.csv"

# check if "csv_file" already exists
if not os.path.exists(csv_file):
    print("**** you have no contacts ****")
else:
    with open('day-1-fair-.csv', 'r', newline='') as csv_file_reader:
        contact_reader = csv.DictReader(csv_file_reader,)

        print("**** Your all contacts: ****")

        for row in contact_reader:
            print(row["number"], row["name"], row["date"], row["email"], )

        print("--------------------------------------")

if not os.path.exists(csv_file):
    print("**** you have no contacts ****")
else:
    with open('day-1-fair-.csv', 'r', newline='') as csv_file_reader:
        contact_reader = csv.DictReader(csv_file_reader,)

        ############ SEARCH
        print("**** Searching for a contact: ****")

        question = input("Do you want to search for a name ?")
        if question == "y" or "yes":
        # search_name = "name888"
            search_name = input("Do you want to search for a name ?")

            found = False
            for row in contact_reader:
                if search_name == row["name"]:
                    print(row["number"], row["name"], row["date"], row["email"])
                    found = True

print("--------------------------------------")

############ WRITING ON csv file
############ csv.DictWriter

number = int(input("enter a number to add to contacts: "))
name = input("enter a name : ")
date = input("enter a date eg, 25/04/16 : ")
email = input("enter a email : ")


if not os.path.exists(csv_file):
    
    with open('day-1-fair-.csv', 'w', newline= '' ) as csv_file_write:
        headings = ["number", "name", "date", "email" ]     
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)
        contact_writer.writeheader()
        contact_writer.writerow({ "number": number, "name": name, "date": date, "email": email})

else:

    with open('day-1-fair-.csv', 'a', newline= '' ) as csv_file_write:
        headings = ["number", "name", "date", "email" ]     
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)
        contact_writer.writerow({ "number": number, "name": name, "date": date, "email": email})

print('----------------------------------------------')
print('----------------------------------------------')

