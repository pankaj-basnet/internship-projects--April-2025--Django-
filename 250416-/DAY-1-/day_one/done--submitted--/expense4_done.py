import datetime
import os
import csv

print('----------------------------------------------')
print('----------------------------------------------')

today = datetime.date.today()

# 2025-04-16 
today_string = (today.strftime(format="%Y/%m/%d")).replace("/", "-") 

date_for_one_week_ago = today - datetime.timedelta(6)
print(date_for_one_week_ago)
# 2025-04-10 
date_for_one_week_ago_string = ((date_for_one_week_ago).strftime(format="%Y/%m/%d")).replace("/", "-")

csv_file = "day-1-expense-.csv"

if not os.path.exists(csv_file):
    print("**** you have no expense record ****")
else:
    with open('day-1-expense-.csv', 'r', newline='') as csv_file_reader:
        expense_reader = csv.DictReader(csv_file_reader,)


        ############ ------------------------------------
        ############ TODAY'S EXPENSE
        print("**** Today's expense (Total): ****")

        today = datetime.date.today()

        todays_expense_total = 0
        
        for row in expense_reader:
            if row["date"] == today_string:
                todays_expense_total += int(row["amount"])
                print(todays_expense_total)
        
        print(f"Today's expense (Total): {todays_expense_total}")
 
print('----------------------------------------------')

if not os.path.exists(csv_file):
    print("**** you have no expense record ****")
else:
    with open('day-1-expense-.csv', 'r', newline='') as csv_file_reader:
        expense_reader = csv.DictReader(csv_file_reader,)
        weekly_expense_total = 0

        for row in expense_reader:
            if int(row["date"][8:10]) - int(date_for_one_week_ago_string[8:10]) >= 0:

                weekly_expense_total += int(row["amount"])

        print(f"Weekly expense (Total): {weekly_expense_total}")


print('----------------------------------------------')


############ ------------------------------------
############ ADD EXPENSE
print(date_for_one_week_ago_string)

description = input("enter description of expense: ")
amount = input("enter amount of expense: ")
date = input("enter date of expense: eg, 2025-04-16 ")

if not os.path.exists(csv_file):
    
    with open('day-1-expense-.csv', 'w', newline= '' ) as csv_file_write:
        headings = ["description", "amount", "date" ]     
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)
        contact_writer.writeheader()
        contact_writer.writerow({ "description": description, "amount": amount, "date": f'{datetime.date.today()}', })

else:

    with open('day-1-expense-.csv', 'a', newline= '' ) as csv_file_write:
        headings = ["description", "amount", "date" ]     
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)

        contact_writer.writerow({ "description": description, "amount": amount, "date": date })
        
print('----------------------------------------------')
print('----------------------------------------------')