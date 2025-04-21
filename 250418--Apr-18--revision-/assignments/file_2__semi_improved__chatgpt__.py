## Here's the improved and clean version of your Library Book Tracker assignment with better structure, error handling, and accurate type handling (especially for booleans and date formats):

# Assignment - 2
# Improved: Library Book Tracker

import csv
import datetime
import os

FILENAME = 'file2_semi_.csv'
HEADERS = ["title", "author", "genre", "borrowed date", "returned"]

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()

def add_book(title, author, genre):
    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "borrowed date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "returned": "False"
    }
    with open(FILENAME, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow(book)
    print(f"Added book: {title}")

def list_borrowed_books():
    print("\n📚 Currently Borrowed Books:")
    with open(FILENAME, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['returned'].strip().lower() == 'false':
                print(f"- {row['title']} (Borrowed on: {row['borrowed date'][:10]})")

def mark_book_returned(borrowed_date_str_prefix):
    updated_rows = []
    with open(FILENAME, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['borrowed date'].startswith(borrowed_date_str_prefix):
                row['returned'] = "True"
            updated_rows.append(row)

    with open(FILENAME, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(updated_rows)
    print(f"Book marked as returned for borrow time: {borrowed_date_str_prefix}")

def show_due_dates():
    print("\n📅 Book Due Dates:")
    with open(FILENAME, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                borrowed_date = datetime.datetime.strptime(row['borrowed date'][:19], "%Y-%m-%d %H:%M:%S")
                due_date = borrowed_date + datetime.timedelta(days=7)
                print(f"- {row['title']} | Due on: {due_date.strftime('%Y-%m-%d')}")
            except Exception as e:
                print(f"⚠️ Error parsing date for {row.get('title')}: {e}")

# Initialize CSV (creates with headers if not exists)
initialize_csv()

# Example usage:
add_book("The Alchemist", "Paulo Coelho", "Fiction")
add_book("Sherlock Holmes", "Arthur Conan Doyle", "Mystery")

list_borrowed_books()

mark_book_returned("2025-04-12 21:22")  # use appropriate prefix to match existing row

show_due_dates()


# Improvements Made:
# Boolean fields (returned) stored as strings: "True" / "False" and handled carefully.

# Used datetime.strftime and strptime for consistent date formatting and parsing.

# Wrapped repetitive operations (e.g., file writing) in reusable functions.

# Error handling is included for robust behavior.

# Output messages are clean and user-friendly.