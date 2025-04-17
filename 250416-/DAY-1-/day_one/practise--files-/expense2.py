import datetime
import os
import csv

print(datetime.date.today())

        ############ Today's expense (((((( DONE $$$$$$$$$$$$$$$ ))))))
        ############ WEEKLY expense , SOME BUG LEFT (((((( DONE $$$$$$$$$$$$$$$ ))))))


today = datetime.date.today()
today_string = (today.strftime(format="%Y/%m/%d")).replace("/", "-")

date_for_one_week_ago = today - datetime.timedelta(7)
print(date_for_one_week_ago)

print((today.strftime(format="%Y/%m/%d")).replace("/", "-"), type(today.strftime(format="%Y/%m/%d")))

csv_file = "day-1-expense-.csv"

if not os.path.exists(csv_file):
    print("**** you have no expense record ****")
else:
    with open('day-1-expense-.csv', 'r', newline='') as csv_file_reader:
        contact_reader = csv.DictReader(csv_file_reader,)
        
        ############ Today's expense (((((( DONE $$$$$$$$$$$$$$$ ))))))
        print("**** Today's expense (Total): ****")

        today = datetime.date.today()

        todays_expense_total = 0
        
        for row in contact_reader:
            print(row["date"], row["amount"])
            print(today_string, today)
            if row["date"] == today_string:
                
            # if "hi" == "hi":
                print("---------", row["amount"])

                todays_expense_total += int(row["amount"])
                print(todays_expense_total)
        
        print(f"Today's expense (Total): {todays_expense_total}") 

            # print(row["description"], row["amount"], row["date"] )

        ############ WEEKLY EXPENSE
    
        weekly = input("Do you want weekly expense report ?")
        if weekly == "y" or "yes":
            weekly_expense_total = 0

            date_for_one_week_ago = today - datetime.timedelta(7)
            print(date_for_one_week_ago)
            for row in contact_reader:
                if row["date"] - date_for_one_week_ago <= 7:
                    weekly_expense_total += row["amount"]
        
            print(f"Weekly expense (Total): {weekly_expense_total}")



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
        contact_writer.writerow({ "description": "description222", "amount": "222", "date": "date"})

        # contact_writer.writerow({ "description": description, "amount": amount, "date": date, })

print('----------------------------------------------')
print('----------------------------------------------')