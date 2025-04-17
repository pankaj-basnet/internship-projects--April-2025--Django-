import csv


print('----------------------------------------------')
print('----------------------------------------------')

############ WRITING ON csv file
############ csv.DictWriter

## ****** uncomment these inputs if necessary ******
# number = int(input("enter a number : "))
# name = input("enter a name : ")
# date = input("enter a date eg, 25/04/16 : ")
# email = input("enter a email : ")

with open('day-1-fair-.csv', 'a', newline= '' ) as csv_file_write:
    headings = ["number", "name", "date", "email" ] ## issue= writes heading everytime we append
    contact_writer = csv.DictWriter(csv_file_write, headings)
    contact_writer.writeheader()
    contact_writer.writerow({ "number": "2025", "name":"Monica 555", "date":"July 1, 2015", "email":"Republican55"})
    # contact_writer.writerow({ "number": number, "name": name, "date": date, "email": email})
    
    
print('---------------------------')
print('---------------------------')
print('---------------------------')


############ READING from csv file
############ csv.DictWriter

with open('day-1-fair-.csv', 'r', newline='') as csv_file_reader:
    contact_reader = csv.DictReader(csv_file_reader,)
    for row in contact_reader:
        print('----------')
        print(row)


    
print('----------------------------------------------')
print('----------------------------------------------')


############ SEARCH BY NAME from csv file
############ csv.DictWriter











######################################################
######################################################
###########           NOTES         ##################

###  WRITING ON csv file
# "a" to append , creates a file if no existing file

######################################################
######################################################