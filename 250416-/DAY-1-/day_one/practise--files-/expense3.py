import datetime
import os
import csv

# print(datetime.date.today())

################################################################
################################################################
########## ((((  WEEKLY EXPENSES CALCULATION DONE, ADDING EXPENSES (HARD CODED) DONE  ))))
################################################################
################################################################

print('----------------------------------------------')
print('----------------------------------------------')

today = datetime.date.today()
print(today)
today_string = (today.strftime(format="%Y/%m/%d")).replace("/", "-")
print(today)

# date_for_one_week_ago = today - datetime.timedelta(7)
date_for_one_week_ago = today - datetime.timedelta(6)
print(date_for_one_week_ago)


# date_for_one_week_ago_string = ((date_for_one_week_ago + datetime.timedelta(2)).strftime(format="%Y/%m/%d")).replace("/", "-")
date_for_one_week_ago_string = ((date_for_one_week_ago).strftime(format="%Y/%m/%d")).replace("/", "-")

print(date_for_one_week_ago_string)

# date_for_one_week_ago_string = (date_for_one_week_ago.strftime(format="%Y/%m/%d")).replace("/", "-")
# print(date_for_one_week_ago_string)


# print((today.strftime(format="%Y/%m/%d")).replace("/", "-"), type(today.strftime(format="%Y/%m/%d")))

csv_file = "day-1-expense-.csv"

if not os.path.exists(csv_file):
    print("**** you have no expense record ****")
else:
    with open('day-1-expense-.csv', 'r', newline='') as csv_file_reader:
        expense_reader = csv.DictReader(csv_file_reader,)


        ############ ------------------------------------
        ############ Today's expense
        print("**** Today's expense (Total): ****")

        today = datetime.date.today()

        todays_expense_total = 0
        
        for row in expense_reader:
            # print(row["date"], row["amount"])
            # print(today_string, today)
            if row["date"] == today_string:
                
            # if "hi" == "hi":
                # print("---------", row["amount"])

                todays_expense_total += int(row["amount"])
                print(todays_expense_total)
        
        print(f"Today's expense (Total): {todays_expense_total}") 

            # print(row["description"], row["amount"], row["date"] )

 
print('----------------------------------------------')
if not os.path.exists(csv_file):
    print("**** you have no expense record ****")
else:
    with open('day-1-expense-.csv', 'r', newline='') as csv_file_reader:
        expense_reader = csv.DictReader(csv_file_reader,)

               ############ ------------------------------------
        ############ WEEKLY EXPENSE
    
        # weekly = input("Do you want weekly expense report ?")
        # if weekly == "y" or "yes":

        #     weekly_expense_total = 0
        weekly_expense_total = 0

        # date_for_one_week_ago = today - datetime.timedelta(7)
        print(date_for_one_week_ago)

        print( date_for_one_week_ago_string[8:10]  )

        print("..........................")
        for row in expense_reader:

            print("......")

            print(row["date"], row["amount"])
            # if row["date"] - date_for_one_week_ago <= 7:
            print(row["date"][8:10] , date_for_one_week_ago_string[8:10]  )
            if int(row["date"][8:10]) - int(date_for_one_week_ago_string[8:10]) >= 0:

                weekly_expense_total += int(row["amount"])
            print(f"{weekly_expense_total}")

    
        print(f"Weekly expense (Total): {weekly_expense_total}")


print('----------------------------------------------')


if not os.path.exists(csv_file):
    
    with open('day-1-expense-.csv', 'w', newline= '' ) as csv_file_write:
        headings = ["description", "amount", "date" ]     
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)
        contact_writer.writeheader()
        # contact_writer.writerow({ "number": number, "name": name, "date": date, "email": email})
        # contact_writer.writerow({ "description": description, "amount": amount, "date": date, })
        contact_writer.writerow({ "description": "description111", "amount": "1111", "date": f'{datetime.date.today()}', })

else:

    with open('day-1-expense-.csv', 'a', newline= '' ) as csv_file_write:
        headings = ["description", "amount", "date" ]     
        contact_writer = csv.DictWriter(csv_file_write,fieldnames= headings)
        # contact_writer.writerow({ "description": "description222", "amount": "222", "date": f'{datetime.date.today()}', })
        contact_writer.writerow({ "description": "description222", "amount": "111", "date": date_for_one_week_ago_string})
        print(date_for_one_week_ago_string)

        # contact_writer.writerow({ "description": description, "amount": amount, "date": date, })

print('----------------------------------------------')
print('----------------------------------------------')