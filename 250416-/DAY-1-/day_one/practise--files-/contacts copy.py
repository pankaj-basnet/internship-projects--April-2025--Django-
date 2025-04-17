### before 250416-1128


import csv

print('----------------------------------------------')
print('----------------------------------------------')

""" csv.reader worked fine before coding csv.writer"""

# with open('day-1-fair-.csv') as csvfile:
#     contact_reader = csv.reader(csvfile)
#     # contact_writer = csv.writer(csvfile, delimiter= " ")
#     # contact_writer.writerow(["2017","Monica Rodriguez","July 1, 2017","Democratic"])
#     for row in contact_reader:
        

#         print("===============")
#         print(row[0], type(row[0]))
#         print(row[1], type(row[1]))
#         # print(row[2], type(row[2]))
#         # print(row[3], type(row[3]))
#         print(", ".join(row))


""" csv.writer did not put 'comma' between values like in original downloaded file . using csv.DictWriter instead"""

with open('day-1-fair-.csv', 'w', newline= '' ) as csv_file_write:
    contact_writer = csv.writer(csv_file_write, delimiter= " ")
    contact_writer.writerow(["2020","Monica Rodriguez3","July 1, 2019","Democratic3"])
    
# with open('day-1-fair-.csv') as csvfile:
#     contact_reader = csv.reader(csvfile)
#     # contact_writer = csv.writer(csvfile, delimiter= " ")
#     # contact_writer.writerow(["2017","Monica Rodriguez","July 1, 2017","Democratic"])
#     for row in contact_reader:
#         print("===============")
#         print(row[0], type(row[0]))
#         print(row[1], type(row[1]))
#         # print(row[2], type(row[2]))
#         # print(row[3], type(row[3]))
#         print(", ".join(row))



print('----------------------------------------------')
print('----------------------------------------------')

### csv.DictWriter

with open('day-1-fair-.csv', 'w', newline= '' ) as csv_file_write:
    headings = ["number", "name", "date", "email" ]
    contact_writer = csv.DictWriter(csv_file_write, headings)
    contact_writer.writeheader()
    contact_writer.writerow({ "number": "2020", "name":"Monica Rodriguez3", "date":"July 1, 2019", "email":"Democratic3"})
    
print('----------------------------------------------')
print('----------------------------------------------')
