### copied csv framework for assignment 8
### copied from D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\aaa__csv__final___FRAMEWORK__python__250422_10_56_.py

# ===============================================
# Class-based Library Book Tracker (Enhanced Version)
# ===============================================
# Features:
#   - Add a book (title, author, genre, borrowed date)
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

# id,title,borrowed date,subscribed,due date,price_in_yen,returned date,fine_in_yen
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

# validate_input("title", 508500)

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

filename_of_csv = "framework_.csv"  # File to store book records
filename_of_json = "framework_.json"  # File to export records as JSON

# Headers for CSV file
headings = [
    "id", "title", "borrowed date", "subscribed",
    "due date", "price_in_yen", "returned date", "fine_in_yen"
]

# ===============================================
# Class to represent a Book record
# ===============================================
class BookRecord:
    _id_counter = 1  # Static counter to assign unique ID to each book

    def __init__(self, title, borrowed_date, subscribed, price_in_yen, returned_date=None):
        self.id = BookRecord._id_counter
        BookRecord._id_counter += 1

        self.title = title
        self.borrowed_date = borrowed_date  # datetime object
        self.subscribed = subscribed  # bool

        # Due date logic: 30 days for subscribed users, else 7 days
        self.due_date = borrowed_date + timedelta(days=30 if subscribed else 7)

        self.price_in_yen = price_in_yen  # float
        self.returned_date = returned_date  # datetime object or None
        self.fine_in_yen = self.calculate_fine()  # calculated based on return delay

    def calculate_fine(self):
        # Fine is charged if returned after due date
        if self.returned_date and self.returned_date > self.due_date:
            return 5000.50
        return 0.0

    def to_dict(self):
        # Convert object data to dictionary for CSV/JSON
        return {
            "id": self.id,
            "title": self.title,
            "borrowed date": self.borrowed_date.strftime("%Y-%m-%d %H:%M:%S"),
            "subscribed": self.subscribed,
            "due date": self.due_date.strftime("%Y-%m-%d %H:%M:%S"),
            "price_in_yen": self.price_in_yen,
            "returned date": self.returned_date.strftime("%Y-%m-%d %H:%M:%S") if self.returned_date else "",
            "fine_in_yen": self.fine_in_yen
        }

    @staticmethod
    def from_dict(data):
        # Create a BookRecord instance from dictionary (CSV/JSON)
        return BookRecord(
            title=data["title"],
            borrowed_date=datetime.strptime(data["borrowed date"], "%Y-%m-%d %H:%M:%S"),
            subscribed=data["subscribed"] in ["True", True],
            price_in_yen=float(data["price_in_yen"]),
            returned_date=datetime.strptime(data["returned date"], "%Y-%m-%d %H:%M:%S") if data["returned date"] else None
        )

# ===============================================
# Helper function: Validate inputs
# ===============================================
def validate_input(title, price):
    # Validate title using regex (only alphabets and spaces)
    if not re.match(r"^[A-Za-z\s]+$", title):
        raise ValueError("Invalid title. Only alphabets and spaces are allowed.")
    # Price should be numeric
    if not isinstance(price, (float, int)):
        raise ValueError("Price must be a number.")

# ===============================================
# Append a book to the CSV file
# ===============================================
def append_book_record(book: BookRecord):
    validate_input(book.title, book.price_in_yen)
    file_exists = os.path.exists(filename_of_csv)
    with open(filename_of_csv, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headings)
        if not file_exists:
            writer.writeheader()
        writer.writerow(book.to_dict())
        print(f"✅ Book '{book.title}' added successfully.")

# ===============================================
# Export all book records to JSON file
# ===============================================
def export_to_json():
    try:
        with open(filename_of_csv, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        with open(filename_of_json, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("📦 Exported to JSON successfully.")
    except Exception as e:
        print(f"❌ JSON export error: {e}")

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
# Delete a book using ID
# ===============================================
def delete_book_by_id(book_id: int):
    try:
        with open(filename_of_csv, 'r') as file:
            books = list(csv.DictReader(file))
        books = [book for book in books if int(book['id']) != book_id]
        with open(filename_of_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings)
            writer.writeheader()
            writer.writerows(books)
        print(f"🗑️ Deleted book with ID {book_id}")
    except Exception as e:
        print(f"❌ Error deleting book: {e}")

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
# Search books by keyword (title/date/author)
# ===============================================
def search_books(keyword: str):
    try:
        with open(filename_of_csv, 'r') as file:
            books = list(csv.DictReader(file))
        results = [b for b in books if keyword.lower() in b['title'].lower() or keyword in b['borrowed date']]
        for book in results:
            print(f"🔍 Found: {book['title']} (ID: {book['id']})")
    except Exception as e:
        print(f"❌ Error searching books: {e}")

# ===============================================
# Group borrowed books by week of borrow date
# ===============================================
def group_books_by_week():
    try:
        with open(filename_of_csv, 'r') as file:
            reader = csv.DictReader(file)
            books = list(reader)

        grouped_books = {}
        total_fine = 0.0

        for row in books:
            # Determine if user is subscribed
            subscribed = row["subscribed"].strip().lower() == 'true'
            borrow_dt = datetime.strptime(row["borrowed date"], "%Y-%m-%d %H:%M:%S")

            # Group key includes year, week number, and subscription status
            week_key = borrow_dt.strftime("%Y-W%U") + ("-S" if subscribed else "-NS")

            # Convert to correct types
            row["price_in_yen"] = float(row["price_in_yen"])
            row["fine_in_yen"] = float(row["fine_in_yen"] or 0.0)
            total_fine += row["fine_in_yen"]

            if week_key not in grouped_books:
                grouped_books[week_key] = []
            grouped_books[week_key].append(row)

        for week, book_list in grouped_books.items():
            print(f"\n📚 Week Group: {week}")
            sorted_books = sorted(book_list, key=lambda b: b["price_in_yen"], reverse=True)
            for book in sorted_books:
                print(f"  - {book['id']} → - {book['title']} → ¥{book['price_in_yen']} (Borrowed: {book['borrowed date']})")

        print(f"\n💰 Total Fine Collected: ¥{total_fine:.2f}")

    except Exception as e:
        print(f"❌ Error grouping books: {e}")

# Sample Record Insertion
# book_record = BookRecord(
#     title="Sherlock Holmes",
#     borrowed_date=datetime(2025, 4, 21, 20, 30, 0),
#     subscribed=True,
#     price_in_yen=100000.50,
#     returned_date=datetime(2025, 5, 30, 19, 15, 0)
# )

# book_record = [BookRecord(
#     title="harry",
#     borrowed_date=datetime(2025, 4, 16, 20, 30, 0),
#     subscribed=True,
#     price_in_yen=199000.50,
#     returned_date=datetime(2025, 4, 26, 19, 15, 0)
# ), BookRecord(
#     title="sherlock",
#     borrowed_date=datetime(2025, 4, 18, 20, 30, 0),
#     subscribed=True,
#     price_in_yen=199000.50,
#     returned_date=datetime(2025, 4, 29, 19, 15, 0)
# )]
        
book_record = BookRecord(
    title="harry",
    borrowed_date=datetime(2025, 4, 16, 20, 30, 0),
    subscribed=True,
    price_in_yen=199000.50,
    returned_date=datetime(2025, 4, 26, 19, 15, 0)
)

append_book_record(book_record)
group_books_by_week()

print("------------------------------------------")   
# def validate_input(title, price):
validate_input("title", 508500)
print("------------------------------------------")
# def append_book_record(book: BookRecord):
# append_book_record(book: BookRecord)
print("------------------------------------------")
# def export_to_json():
export_to_json()
print("------------------------------------------")
# def update_book_price(book_id: int, new_price: float):
update_book_price(book_id= 1, new_price= 60100)
print("------------------------------------------")
# def delete_book_by_id(book_id: int):
delete_book_by_id(book_id = 1)
print("------------------------------------------")
# def edit_book_by_id(book_id: int, field: str, new_value):
edit_book_by_id(book_id= 3, field= "subscribed" , new_value= False)
print("------------------------------------------")
# def search_books(keyword: str):
search_books(keyword = "harr")
print("------------------------------------------")
# def group_books_by_week():
group_books_by_week()


print("========================================================")
