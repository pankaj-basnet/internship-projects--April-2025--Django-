# ===============================================
# Assignment - 2: Library Book Tracker
# ===============================================
# Features:
#   - Add a book (title, author, genre, borrowed date)
#   - Mark book as returned
#   - List currently borrowed books
#   - Show overdue books (based on borrow date)
#   - Data stored in CSV file (file2.csv)
# ===============================================


print("--------------------------------------")


import csv
import datetime
import os

filename_of_csv = 'file2_improved_.csv'  # CSV file to store book information
headings = ["title", "author", "genre", "borrowed date", "returned"]

# ===============================================
# Add a new book to the CSV file
# ===============================================
def add_book(book):
    """Appends a book dictionary to the CSV file, with header check."""
    try:
        file_exists = os.path.exists(filename_of_csv)

        with open(filename_of_csv, 'a' if file_exists else 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings)

            if not file_exists:
                writer.writeheader()

            # Convert datetime object to string for CSV compatibility
            book["borrowed date"] = book["borrowed date"].strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(book)

        print(f"✅ Book '{book['title']}' added successfully.")

    except Exception as e:
        print(f"❌ Error adding book: {e}")

# Example usage
add_book({
    "title": "Sherlock Holmes",
    "author": "Arthur Conan Doyle",
    "genre": "Mystery",
    "borrowed date": datetime.datetime.now(),
    "returned": False
})


print("--------------------------------------")


# ===============================================
# List currently borrowed books
# ===============================================
def list_borrowed_books():
    """Displays all books not yet returned."""
    print("\n📚 Currently Borrowed Books:")
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["returned"].strip().lower() == 'false':
                    print(f"- {row['title']} (Borrowed on: {row['borrowed date'][:10]})")
    except Exception as e:
        print(f"❌ Error reading borrowed books: {e}")

list_borrowed_books()

# ===============================================
# Mark a book as returned by a partial borrow date match
# ===============================================
def mark_book_as_returned(borrowed_partial_datetime):
    """
    Updates the 'returned' field to True for books matching a specific borrow datetime (partial match).
    """
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            books = list(reader)  # Load all data into memory

        for book in books:
            # if borrowed_partial_datetime in book["borrowed date"]:
            if borrowed_partial_datetime == book["borrowed date"]:
                book["returned"] = "True"

        with open(filename_of_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings)
            writer.writeheader()
            writer.writerows(books)

        print(f"✅ Book marked as returned (Borrowed on: {borrowed_partial_datetime})")

    except Exception as e:
        print(f"❌ Error marking book as returned: {e}")

# Example usage
mark_book_as_returned("2025-04-12 21:22:39")



print("--------------------------------------")



# ===============================================
# Show due dates and overdue books
# ===============================================
def show_due_dates():
    """Calculates and displays due dates for borrowed books."""
    print("\n📅 Book Due Dates:")
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                borrow_date_str = row["borrowed date"]
                try:
                    borrow_date = datetime.datetime.strptime(borrow_date_str[:19], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"⚠️ Skipping invalid date format: {borrow_date_str}")
                    continue

                due_date = borrow_date + datetime.timedelta(days=7)
                print(f"- {row['title']} → Due by: {due_date.strftime('%Y-%m-%d')}")

    except Exception as e:
        print(f"❌ Error calculating due dates: {e}")

show_due_dates()




print("--------------------------------------")


