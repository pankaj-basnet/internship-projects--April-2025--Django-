        
from datetime import datetime
import csv


def calculate_streak():
    print("---------------")
    print("calcalating streak")
    print("---------------")
    print("---------------")
    # print(self.finished_date, type(self.finished_date))
    # print("---------------")
    # print((datetime.now()- self.finished_date ) > timedelta(days=1), type((datetime.now()- self.finished_date ) > timedelta(days=1)))
    # print("---------------")

    # if self.finished_date - datetime.now()
    # if (datetime.now()- self.finished_date ) > timedelta(days=1):
    #     print("-------- more than one day-- streak 0 ------")
    #     return 0
    # else:
    filename_of_csv = 'prac_8_222.csv'
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            days_of_coding = list(reader)
        
            total_days_of_streak = list_of_topics = search_books("sundayProjectTWO")

            print("=============")
            print(list_of_topics)
            print("=============")
        
    except Exception as e:
        print(f"error reading csv in calculate_streak() function {e}")



    print("---------------")

    # if self.finished_date - datetime.now()
    # if ( datetime.now() -datetime(2025, 4, 1, 20, 30, 0)) > timedelta(days=1):
    #     print("-------- more than one day--------")

calculate_streak()