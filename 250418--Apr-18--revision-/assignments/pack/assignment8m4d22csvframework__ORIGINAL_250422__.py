#################################################################
#################################################################
#################################################################
# add , update any field, search any topic or startdate (((ORIGINAL)))
#################################################################
# file_8__ORIGINAL__.py # #  pack\assignment8m4d22csvframework__ORIGINAL_250422__.py
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\file_8__ORIGINAL__.py
#####################################################

#  D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\pack\assignment8m4d22csvframework__ORIGINAL_250422__.py
#################################################################
#################################################################


### copied csv framework for assignment 8
### copied from D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\aaa__csv__final___FRAMEWORK__python__250422_10_56_.py
### assignment 8 --- day 3 --- csv framework copy --- D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\pack\assignment8m4d22csvframework.py
# ===============================================
# Class-based Library Book Tracker (Enhanced Version)
# ===============================================
# Features:
#   - Add a book (topic, author, genre, borrowed date)
#   - Mark book as returned
#   - List currently borrowed books
#   - Show overdue books
#   - Calculate fine based on return delay
#   - Export/import JSON
#   - Group books by week
#   - Validate inputs using regex and type check
#   - Support delete, edit, and search
# ===============================================
# ===============================================

# id,topic,borrowed date,subscribed,due date,price_in_yen,returned date,fine_in_yen
# 1,harry,2025-04-16 20:30:00,True,2025-05-16 20:30:00,60100,2025-04-26 19:15:00,0.0
# 2,harry,2025-04-10 20:30:00,False,2025-05-16 20:30:00,102555,2025-04-26 19:15:00,0.0
# 3,harry,2025-04-11 20:30:00,True,2025-05-16 20:30:00,60100,2025-04-26 19:15:00,0.0
# 4,harry,2025-04-12 20:30:00,False,2025-05-16 20:30:00,75600,2025-04-26 19:15:00,0.0
# 5,hry,2025-04-17 20:30:00,True,2025-05-11 20:30:00,88500,2025-04-29 19:15:00,0.0
# 6,hry,2025-04-18 20:30:00,False,2025-05-11 20:30:00,60100,2025-04-29 19:15:00,0.0
# 7,hry,2025-04-17 20:30:00,True,2025-05-11 20:30:00,60100,2025-04-29 19:15:00,0.0
# 8,hry,2025-04-18 20:30:00,True,2025-05-11 20:30:00,60100,2025-04-29 19:15:00,0.0
# 11,harry,2025-04-16 20:30:00,True,2025-05-16 20:30:00,60100,2025-04-26 19:15:00,0.0
# ===============================================
# ===============================================
# ========================================================
# ✅ Book 'harry' added successfully.

# 📚 Week Group: 2025-W15-S
#   - 1 → - harry → ¥199000.5 (Borrowed: 2025-04-16 20:30:00)
#   - 5 → - hry → ¥88500.0 (Borrowed: 2025-04-17 20:30:00)   
#   - 1 → - harry → ¥60100.0 (Borrowed: 2025-04-16 20:30:00) 
#   - 7 → - hry → ¥60100.0 (Borrowed: 2025-04-17 20:30:00)   
#   - 8 → - hry → ¥60100.0 (Borrowed: 2025-04-18 20:30:00)   

# 📚 Week Group: 2025-W14-NS
#   - 2 → - harry → ¥102555.0 (Borrowed: 2025-04-10 20:30:00)
#   - 4 → - harry → ¥75600.0 (Borrowed: 2025-04-12 20:30:00) 

# 📚 Week Group: 2025-W14-S
#   - 3 → - harry → ¥60100.0 (Borrowed: 2025-04-11 20:30:00) 

# 📚 Week Group: 2025-W15-NS
#   - 6 → - hry → ¥60100.0 (Borrowed: 2025-04-18 20:30:00)   

# 💰 Total Fine Collected: ¥0.00
# 📦 Exported to JSON successfully.
# 💰 Updated price for book ID 1
# 💰 Updated price for book ID 1
# 🔍 Found: harry (ID: 1)
# 🔍 Found: harry (ID: 2)
# 🔍 Found: harry (ID: 3)
# 🔍 Found: harry (ID: 4)
# 🔍 Found: harry (ID: 1)

# 📚 Week Group: 2025-W15-S
#   - 5 → - hry → ¥88500.0 (Borrowed: 2025-04-17 20:30:00)   
#   - 1 → - harry → ¥60100.0 (Borrowed: 2025-04-16 20:30:00) 
#   - 7 → - hry → ¥60100.0 (Borrowed: 2025-04-17 20:30:00)   
#   - 8 → - hry → ¥60100.0 (Borrowed: 2025-04-18 20:30:00)   
#   - 1 → - harry → ¥60100.0 (Borrowed: 2025-04-16 20:30:00) 

# 📚 Week Group: 2025-W14-NS
#   - 2 → - harry → ¥102555.0 (Borrowed: 2025-04-10 20:30:00)
#   - 4 → - harry → ¥75600.0 (Borrowed: 2025-04-12 20:30:00) 

# 📚 Week Group: 2025-W14-S
#   - 3 → - harry → ¥60100.0 (Borrowed: 2025-04-11 20:30:00) 

# 📚 Week Group: 2025-W15-NS
#   - 6 → - hry → ¥60100.0 (Borrowed: 2025-04-18 20:30:00)   

# 💰 Total Fine Collected: ¥0.00
# ======================================================== 
# ======================================================== 

### functions used for above result ((# # --- double hash --- commented-- not used))
# append_book_record(book_record)
# group_books_by_week()

# validate_input("topic", 508500)

# # append_book_record(book: BookRecord)

# export_to_json()
# update_book_price(book_id= 1, new_price= 60100)

# # delete_book_by_id(book_id = 2)

# # edit_book_by_id(book_id= 3, field= subscribed = False)

# search_books(keyword = "harr")
# group_books_by_week()

# ======================================================== 
# ======================================================== 
# ===============================================
# ===============================================
print("========================================================")

import csv
import json
import os
import re
from datetime import datetime, timedelta

filename_of_csv = "framework_a8_.csv"  # File to store book records
filename_of_json = "framework_a8_.json"  # File to export records as JSON

##########################################
# changed all "name" to "topic" in whole file
#  change "borrow" to "start" ------ for borrowed date  to "start time"
#  change "return" to "finish" ------  for returned date  to "finished time"

# change calculate_fine to calculate_coding_duration
# change "fine_in_yen"  to "coding_duration" 
##########################################

# Headers for CSV file
headings = [
    "id", "topic", "start date", "subscribed",
    "due date", "price_in_yen", "finished date", "coding_duration"
]

# ===============================================
# Class to represent a Book record
# ===============================================
class BookRecord:
    _id_counter = 2  # Static counter to assign unique ID to each book
    _id_counter = 3  # Static counter to assign unique ID to each book

    def __init__(self, topic, start_date, subscribed, price_in_yen, finished_date=None):
        self.id = BookRecord._id_counter
        BookRecord._id_counter += 1

        self.topic = topic
        self.start_date = start_date  # datetime object
        self.subscribed = subscribed  # bool

        # Due date logic: 30 days for subscribed users, else 7 days
        self.due_date = start_date + timedelta(days=30 if subscribed else 7)

        self.price_in_yen = price_in_yen  # float
        self.finished_date = finished_date  # datetime object or None
        self.coding_duration = self.calculate_coding_duration()  # calculated based on finish delay

    print("--------- book record class ----------")

    def calculate_coding_duration(self):
        # Fine is charged if finished after due date
        if self.finished_date and self.finished_date > self.start_date:
            coding_duration = self.finished_date - self.start_date

            print(f'    -----   time delta not changed to "string" (calculate_coding_duration)  ----- ')
            print(coding_duration)
            return coding_duration
        
        coding_duration_zero = timedelta(days= 0)
        print(coding_duration_zero)
        return coding_duration_zero

    def to_dict(self):
        # Convert object data to dictionary for CSV/JSON
        return {
            "id": self.id,
            "topic": self.topic,
            "start date": self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "subscribed": self.subscribed,
            "due date": self.due_date.strftime("%Y-%m-%d %H:%M:%S"),
            "price_in_yen": self.price_in_yen,
            "finished date": self.finished_date.strftime("%Y-%m-%d %H:%M:%S") if self.finished_date else "",
            "coding_duration": self.coding_duration
        }

    @staticmethod
    def from_dict(data):
        # Create a BookRecord instance from dictionary (CSV/JSON)
        return BookRecord(
            topic=data["topic"],
            start_date=datetime.strptime(data["start date"], "%Y-%m-%d %H:%M:%S"),
            subscribed=data["subscribed"] in ["True", True],
            price_in_yen=float(data["price_in_yen"]),
            finished_date=datetime.strptime(data["finished date"], "%Y-%m-%d %H:%M:%S") if data["finished date"] else None
        )

# ===============================================
# Helper function: Validate inputs
# ===============================================
def validate_input(topic, price):
    # Validate topic using regex (only alphabets and spaces)
    if not re.match(r"^[A-Za-z\s]+$", topic):
        raise ValueError("Invalid topic. Only alphabets and spaces are allowed.")
    # Price should be numeric
    if not isinstance(price, (float, int)):
        raise ValueError("Price must be a number.")

# ===============================================
# Append a book to the CSV file
# ===============================================
def append_book_record(book: BookRecord):
    validate_input(book.topic, book.price_in_yen)
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
def update_book_price(book_id: int, new_price: float):
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            books = list(reader)

        for book in books:
            if int(book["id"]) == book_id:

                # if book.get(price_in_yen) == str(new_price): // sn=

                book["price_in_yen"] = str(new_price)
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
    except Exception as e:
        print(f"❌ Error searching books: {e}")

# Sample Record Insertion
# book_record = BookRecord(
#     topic="Sherlock Holmes",
#     started_date=datetime(2025, 4, 21, 20, 30, 0),
#     subscribed=True,
#     price_in_yen=100000.50,
#     finished_date=datetime(2025, 5, 30, 19, 15, 0)
# )

# book_record = [BookRecord(
#     topic="harry",
#     started_date=datetime(2025, 4, 16, 20, 30, 0),
#     subscribed=True,
#     price_in_yen=199000.50,
#     finished_date=datetime(2025, 4, 26, 19, 15, 0)
# ), BookRecord(
#     topic="sherlock",
#     started_date=datetime(2025, 4, 18, 20, 30, 0),
#     subscribed=True,
#     price_in_yen=199000.50,
#     finished_date=datetime(2025, 4, 29, 19, 15, 0)
# )]
        
# book_record = BookRecord(
#     topic="harry",
#     started_date=datetime(2025, 4, 16, 20, 30, 0),
#     subscribed=True,
#     price_in_yen=199000.50,
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
