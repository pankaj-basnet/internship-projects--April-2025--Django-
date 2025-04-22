### copied csv framework for assignment 8
### copied from D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\aaa__csv__final___FRAMEWORK__python__250422_10_56_.py
### assignment 8 --- day 3 --- csv framework copy --- D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\pack\assignment8m4d22csvframework.py
# ===============================================

print("========================================================")

import csv
import json
import os
import re
from datetime import datetime, timedelta

filename_of_csv = "assignment_a8_.csv"  # File to store book records
filename_of_json = "assignment_a8_.json"  # File to export records as JSON

##########################################
# changed all "name" to "topic" in whole file
#  change "borrow" to "start" ------ for borrowed date  to "start time"
#  change "return" to "finish" ------  for returned date  to "finished time"

# change calculate_fine to calculate_coding_duration
# change "fine_in_yen"  to "coding_duration" 

# change "price_in_yen" to "average_coding_time"

##########################################
# id,topic,language,start date,subscribed,due date,price_in_yen,finished date,coding_duration
# 1,django,replace_topic,2025-04-10 20:30:00,False,2025-04-17 20:30:00,99999,2025-04-26 19:15:00,"15 days, 22:45:00"
# 2,data science,python,2025-04-01 20:30:00,False,2025-04-08 20:30:00,175500.5,2025-05-26 19:15:00,"54 days, 22:45:00"
# 3,django,python,2025-04-10 20:30:00,False,2025-04-17 20:30:00,175500.5,2025-04-26 19:15:00,"15 days, 22:45:00"
# 4,data science,python,2025-04-01 20:30:00,False,2025-04-08 20:30:00,175500.5,2025-05-26 19:15:00,"54 days, 22:45:00"
##########################################
# id,topic,language,start date,subscribed,due date,average_coding_time,finished date,coding_duration
# 1,django,replace_topic,2025-04-10 20:30:00,False,2025-04-17 20:30:00,10,2025-04-26 19:15:00,"15 days, 22:45:00"
# 2,data science,python,2025-04-01 20:30:00,False,2025-04-08 20:30:00,30.5,2025-05-26 19:15:00,"54 days, 22:45:00"
# 3,django,python,2025-04-10 20:30:00,False,2025-04-17 20:30:00,10.5,2025-04-26 19:15:00,"15 days, 22:45:00"
# 4,data science,python,2025-04-01 20:30:00,False,2025-04-08 20:30:00,20,2025-05-26 19:15:00,"54 days, 22:45:00"
##########################################
# id,topic,language,start date,subscribed,due date,average_coding_time,finished date,streak,coding_duration
# 1,django,replace_topic,2025-04-10 20:30:00,False,2025-04-17 20:30:00,10,2025-04-26 19:15:00,0,"15 days, 22:45:00"
# 2,data science,python,2025-04-01 20:30:00,False,2025-04-08 20:30:00,30.5,2025-05-26 19:15:00,1,"54 days, 22:45:00"
# 3,django,python,2025-04-10 20:30:00,False,2025-04-17 20:30:00,10.5,2025-04-26 19:15:00,0,"15 days, 22:45:00"
# 4,data science,python,2025-04-01 20:30:00,False,2025-04-08 20:30:00,20,2025-05-26 19:15:00,1,"54 days, 22:45:00"
# 6,sundayProject,python,2025-04-10 20:30:00,False,2025-04-17 20:30:00,34.5,2025-04-26 19:15:00,2,"15 days, 22:45:00"
# 7,sundayProjectTWO,java,2025-04-01 20:30:00,False,2025-04-08 20:30:00,30.6,2025-05-26 19:15:00,0,"54 days, 22:45:00"
##########################################

# Headers for CSV file
headings = [
    "id", "topic", "language", "start date", "subscribed",
    "due date", "average_coding_time", "finished date", "streak" ,"coding_duration"
]

# ===============================================
# Class to represent a Book record
# ===============================================
class BookRecord:
    _id_counter = 8  # Static counter to assign unique ID to each book
    # _id_counter = 3  # Static counter to assign unique ID to each book

    # def __init__(self, topic, language, start_date, subscribed, average_coding_time, finished_date=None):
    def __init__(self, topic, language, start_date, subscribed, finished_date=None):
        self.id = BookRecord._id_counter
        BookRecord._id_counter += 1

        self.topic = topic
        self.language = language
        self.start_date = start_date  # datetime object
        self.subscribed = subscribed  # bool

        # Due date logic: 30 days for subscribed users, else 7 days
        self.due_date = start_date + timedelta(days=30 if subscribed else 7)

        self.average_coding_time = self.calculate_average_coding_time()  # float
        self.finished_date = finished_date  # datetime object or None
        self.streak = self.calculate_streak()
        print("=========================================")
        print("=========", self.streak)
        print("=========================================")
        self.coding_duration = self.calculate_coding_duration()  # calculated based on finish delay


    print("--------- book record class ----------")


    def calculate_coding_duration(self):
        print("---------------")
        print("calcalating coding duration")
        print("---------------")
        # Fine is charged if finished after due date
        
        if self.finished_date and self.finished_date > self.start_date:
            coding_duration = self.finished_date - self.start_date

            # print(f'    -----   time delta not changed to "string" (calculate_coding_duration)  ----- ')
            print(coding_duration)
            return coding_duration
        
        coding_duration_zero = timedelta(days= 0)
        print(coding_duration_zero)
        return coding_duration_zero
    

    def calculate_average_coding_time(self):

        try:
            with open(filename_of_csv, 'r', newline='') as file:
                reader = csv.DictReader(file)
                days_of_coding = list(reader)

                print("--------")
                sum_of_dur = 0

                list_dur = [(float((ii.get("coding_duration"))[:2]) )for ii in days_of_coding]  ## complex calculation along with list comprehension for beginner # str to float() , get method for dictionary, slicing of string
                print(list_dur)
                print(list_dur[1], type(list_dur[1]))
                print("-----")

                sum_of_dur = sum(list_dur)
                print(sum_of_dur)
                print("-----")

                avg = (sum(list_dur)/len(list_dur))
                print(avg, "avg")

                print("")

                # self.average_coding_time = avg ### error # return value to init() to initialize instant variable ## pitfall= beginner=
                
                return avg

                #===================================

                ### con= error when iterating over list of dictionary and get value from each dictionary, convert each value to float and find average prac= sn= beginners problem=
                # for ii in days_of_coding:
                #     # print(ii)
                #     print("--------")
                #     dur = ii.get("coding_duration")
                #     print(dur , type(dur))
                #     print("--------")
                #     sum += float(dur[:2])
                #     print(sum)

                #     print("--------")
                #     # print(ii["duration"])

            # for book in books:
            # list_of_duration = [day["coding_duration"] for day in days_of_coding]
            # print(list_of_duration)
            # for day in days_of_coding:
            #     print(day[""])
            # print(list_of_duration)

            # sum_of_all_coding_time = sum(list_of_duration)
            print("---------------------------")


        except Exception as e:
            print(f"❌ Error calculating_average_coding_time: {e}")


            ################################################
            ################################################
    # try:
            
        # def calculate_streak(self):
        #     print("---------------")
        #     print("calcalating streak")
        #     print("---------------")

            ### problem for beginners with list of dictionary, sorting list of dictionary, date parsing , using already made function search_books()
            ## this solution has error

            # print("calcalating streak")
            # print("---------------")
            # print(self.finished_date, type(self.finished_date))
            # print("---------------")
            # print((datetime.now()- self.finished_date ) > timedelta(days=1), type((datetime.now()- self.finished_date ) > timedelta(days=1)))
            # print("---------------")

            # # if self.finished_date - datetime.now()
            # if (datetime.now()- self.finished_date ) > timedelta(days=1): # ">" greater than 1 day
            #     print("-------- more than one day-- streak 0 ------")
            #     return 0
            # else:
            #     try:
            #         with open(filename_of_csv, 'r', newline='') as file:
            #             reader = csv.DictReader(file)
            #             days_of_coding = list(reader)
                    
            #             total_days_of_streak = list_of_topics = search_books("sundayProjectTWO")

            #             print("=============")
            #             # sorted(list_of_topics, key= topic.get("") for topic in list_of_topics) ## error= # pitfall= bieginners=
            #             sorted(list_of_topics, key=lambda x: datetime.strptime(x['finished date'], '%y-%m-%d %H:%M:%S'))
            #             # print(list_of_topics)
            #             print("=============")
            #             print(list_of_topics)
            #             print("=============")
                    
                # except Exception as e:
                #     print(f"error reading csv in calculate_streak() function {e}")




            print("---------------")

            # if self.finished_date - datetime.now()
            # if ( datetime.now() -datetime(2025, 4, 1, 20, 30, 0)) > timedelta(days=1):
            #     print("-------- more than one day--------")
    
    # except:
    #     print("error while calculating streak")
        
            ################################################
            ################################################

    def calculate_streak(self):
        print("---------------")
        print("calculating streak")
        print("---------------")
        try:
            if not self.finished_date:
                return 0

            # If the project was finished less than a day ago, streak = 0
            if (datetime.now() - self.finished_date) < timedelta(days=1):
                print("-------- finished recently -- streak 0 ------")
                return 0

            # Search for all previous books with the same topic
            previous_books = search_books(self.topic)

            # Filter only those with a valid finished date
            finished_books = []
            for book in previous_books:
                if book.get("finished date"):
                    try:
                        finished_dt = datetime.strptime(book["finished date"], "%Y-%m-%d %H:%M:%S")
                        finished_books.append(finished_dt)
                    except Exception as dt_error:
                        print(f"❌ Date parsing error: {dt_error}")

            # Sort by finished date in ascending order
            finished_books.sort()

            # Count how many are spaced 1 day apart
            streak = 1

            # for i in range(len(finished_books) - 1, 0, -1):
            #     diff = (finished_books[i] - finished_books[i - 1]).days
            #     if diff == 1:
            #         streak += 1
            #     else:
            #         break

            print(f"✅ Calculated streak: {streak}")
            return streak

        except Exception as e:
            print(f"❌ Error in calculate_streak(): {e}")
            return 0





    def to_dict(self):
        # Convert object data to dictionary for CSV/JSON
        return {
            "id": self.id,
            "topic": self.topic,
            "language": self.language,
            "start date": self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "subscribed": self.subscribed,
            "due date": self.due_date.strftime("%Y-%m-%d %H:%M:%S"),
            "average_coding_time": self.average_coding_time,
            "finished date": self.finished_date.strftime("%Y-%m-%d %H:%M:%S") if self.finished_date else "",
            "streak": self.streak,
            "coding_duration": self.coding_duration
        }

    @staticmethod
    def from_dict(data):
        # Create a BookRecord instance from dictionary (CSV/JSON)
        return BookRecord(
            topic=data["topic"],
            language=data["language"],
            start_date=datetime.strptime(data["start date"], "%Y-%m-%d %H:%M:%S"),
            subscribed=data["subscribed"] in ["True", True],
            average_coding_time=float(data["average_coding_time"]),
            finished_date=datetime.strptime(data["finished date"], "%Y-%m-%d %H:%M:%S") if data["finished date"] else None
        )

# ===============================================
# Helper function: Validate inputs
# ===============================================
def validate_input(topic, average_coding_time):
    # Validate topic using regex (only alphabets and spaces)
    if not re.match(r"^[A-Za-z\s]+$", topic):
        raise ValueError("Invalid topic. Only alphabets and spaces are allowed.")
    # Price should be numeric
    if not isinstance(average_coding_time, (float, int)):
        raise ValueError("average_coding_time must be a number.")

# ===============================================
# Append a book to the CSV file
# ===============================================
def append_book_record(book: BookRecord):
    # validate_input(book.topic, book.average_coding_time)
    validate_input(book.topic, float(0.0 if book.average_coding_time is None else book.average_coding_time ) or 0.0)
    file_exists = os.path.exists(filename_of_csv)
    with open(filename_of_csv, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headings)
        if not file_exists:
            writer.writeheader()
        writer.writerow(book.to_dict())
        print(f"✅ Book '{book.topic}' added successfully.")

# ===============================================
# Update book price using ID
# ===============================================
# def update_book_price(book_id: int, new_price: float):
def update_book_price(book_id: int, new_avg: float):
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            books = list(reader)

        for book in books:
            if int(book["id"]) == book_id:

                # if book.get(average_coding_time) == str(new_price): // sn=

                # book["average_coding_time"] = str(new_price)
                # book["average_coding_time"] = new_price
                book["average_coding_time"] = new_avg
                print(f"💰 Updated price for book ID {book_id}")

        with open(filename_of_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings)
            writer.writeheader()
            writer.writerows(books)

    except Exception as e:
        print(f"❌ Error updating price: {e}")

# ===============================================
# Edit any field of a book using ID
# ===============================================
def edit_book_by_id(book_id: int, field: str, new_value):
    try:
        with open(filename_of_csv, 'r') as file:
            books = list(csv.DictReader(file))
        for book in books:
            if int(book['id']) == book_id:
                book[field] = new_value
        with open(filename_of_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings)
            writer.writeheader()
            writer.writerows(books)
        print(f"✏️ Edited book with ID {book_id}")
    except Exception as e:
        print(f"❌ Error editing book: {e}")

# ===============================================
# Search books by keyword (topic/date/author)
# ===============================================
def search_books(keyword: str):
    try:
        with open(filename_of_csv, 'r') as file:
            books = list(csv.DictReader(file))
        results = [b for b in books if keyword.lower() in b['topic'].lower() or keyword in b['start date']]
        for book in results:
            print(f"🔍 Found: {book['topic']} (ID: {book['id']})")

        # number_of_books = len(results) # sn= {added for self.calculate_streak()} # we need results finish date -- no read all books functionality yet # return results ((list of dictionary))
        # return number_of_books # sn=
        return results # sn=  {added for self.calculate_streak()} 
    
    except Exception as e:
        print(f"❌ Error searching books: {e}")

# Sample Record Insertion
# book_record = BookRecord(
#     topic="Sherlock Holmes",
#     started_date=datetime(2025, 4, 21, 20, 30, 0),
#     subscribed=True,
#     average_coding_time=100000.50,
#     finished_date=datetime(2025, 5, 30, 19, 15, 0)
# )

# book_record = [BookRecord(
#     topic="harry",
#     started_date=datetime(2025, 4, 16, 20, 30, 0),
#     subscribed=True,
#     average_coding_time=199000.50,
#     finished_date=datetime(2025, 4, 26, 19, 15, 0)
# ), BookRecord(
#     topic="sherlock",
#     started_date=datetime(2025, 4, 18, 20, 30, 0),
#     subscribed=True,
#     average_coding_time=199000.50,
#     finished_date=datetime(2025, 4, 29, 19, 15, 0)
# )]
        
# book_record = BookRecord(
#     topic="harry",
#     started_date=datetime(2025, 4, 16, 20, 30, 0),
#     subscribed=True,
#     average_coding_time=199000.50,
#     finished_date = datetime(2025, 4, 26, 19, 15, 0)
# )

# append_book_record(book_record)
# group_books_by_week()

print("------------------------------------------")   
# def validate_input(topic, price):
# validate_input("topic", 508500)
print("------------------------------------------")
# def append_book_record(book: BookRecord):
# append_book_record(book: BookRecord)
print("------------------------------------------")
# def export_to_json():
# export_to_json()
print("------------------------------------------")
# def update_book_price(book_id: int, new_price: float):
# update_book_price(book_id= 1, new_price= 60100)
print("------------------------------------------")
# def delete_book_by_id(book_id: int):
# delete_book_by_id(book_id = 1)
print("------------------------------------------")
# def edit_book_by_id(book_id: int, field: str, new_value):
# edit_book_by_id(book_id= 3, field= "subscribed" , new_value= False)
print("------------------------------------------")
# def search_books(keyword: str):
# search_books(keyword = "harr")
print("------------------------------------------")
# def group_books_by_week():
# group_books_by_week()


print("========================================================")
