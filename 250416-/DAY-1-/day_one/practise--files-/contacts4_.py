import csv
import os

print('----------------------------------------------')
print('----------------------------------------------')

############ WRITING ON csv file
############ csv.DictWriter

csv_file = "day-1-fair-.csv"

if not os.path.exists(csv_file):
    print("**** you have no contacts ****")
else:
    with open('day-1-fair-.csv', 'r', newline='') as csv_file_reader:
        contact_reader = csv.DictReader(csv_file_reader,)

        print("**** Your all contacts: ****")

        for row in contact_reader:
            print(row["number"], row["name"], row["date"], row["email"], )
    
        search_name = input("Do you want to search for a name ?")
        if search_name == "y" or "yes":
            for row in contact_reader:
                if search_name == row:
                    print(row["number"], row["name"], row["date"], row["email"])

            print(f"no contact found for {search_name}")



number = int(input("enter a number to add to contacts: "))
name = input("enter a name : ")
date = input("enter a date eg, 25/04/16 : ")
email = input("enter a email : ")


if not os.path.exists(csv_file):
    
    with open('day-1-fair-.csv', 'w', newline= '' ) as csv_file_write:
        headings = ["number", "name", "date", "email" ] ## issue= writes heading everytime we append
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)
        contact_writer.writeheader()
        # contact_writer.writerow({ "number": "2025", "name":"Monica 555", "date":"July 1, 2015", "email":"Republican55"})
        contact_writer.writerow({ "number": number, "name": name, "date": date, "email": email})

else:

    with open('day-1-fair-.csv', 'a', newline= '' ) as csv_file_write:
        headings = ["number", "name", "date", "email" ] ## issue= writes heading everytime we append
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)
        # contact_writer.writerow({ "number": "2666", "name":"Monica 666", "date":"July 1, 2666", "email":"Republican666"})
        contact_writer.writerow({ "number": number, "name": name, "date": date, "email": email})

print('----------------------------------------------')
print('----------------------------------------------')









######################################################
######################################################
###########           NOTES         ##################

###  WRITING ON csv file
# "a" to append , creates a file if no existing file

######################################################
######################################################