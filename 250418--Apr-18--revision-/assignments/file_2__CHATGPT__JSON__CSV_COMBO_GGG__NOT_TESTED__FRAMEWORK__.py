# write code for create, update and delete and read json file handling in python like class bases solution given by you chatgpt for  original function based csv file handling code . dont change logic or variable name

import os
from datetime import datetime , timedelta
import json
import re

import csv

##############      NOT INIT FUNCTION -------- LITTLE ERROR BY CHATGPT

def add_book(self, data):
    # 📋 Check if the CSV file already exists to decide on writing headers
    file_exists = os.path.exists(self.filename_of_csv)

    with open(self.filename_of_csv, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "title", "price_in_yen", "borrowed date", "subscribed", "fine_in_yen"])

        if not file_exists:
            # ✍️ Write headers only if file is new
            writer.writeheader()

        # 🔁 Convert price from string to float (if needed)
        price = float(data["price_in_yen"])

        # ✅ Ensure subscribed is a boolean, handles both True and "True"
        subscribed = data["subscribed"] in ["True", True]

        # 📆 Use current date as borrowed date, formatted nicely
        borrowed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow({
            "id": data["id"],
            "title": data["title"],
            "price_in_yen": price,
            "borrowed date": borrowed_date,
            "subscribed": subscribed,
            "fine_in_yen": ""
        })

def update_book(self, book_id, field, new_value):
    with open(self.filename_of_csv, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # 🧺 Convert to list so we can modify it

    for book in data:
        if int(book["id"]) == book_id:  # ✅ Convert ID from string to int for comparison
            book[field] = new_value  # 📝 Dynamic update using variable field name
            break

    with open(self.filename_of_csv, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(data)

def group_books_by_week(self):
    grouped_books = {}

    with open(self.filename_of_csv, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # 📅 Convert borrowed date from string to datetime object
            borrow_dt = datetime.strptime(row["borrowed date"], "%Y-%m-%d %H:%M:%S")

            # 🗓️ Get year and week number
            year = borrow_dt.year
            week_num = borrow_dt.strftime("%U")
            week_key = f"{year}-W{week_num}"

            if week_key not in grouped_books:
                # 📚 Create a new list for the week if not already present
                grouped_books[week_key] = []

            grouped_books[week_key].append(row)

    return grouped_books

def export_to_json(self, output_filename):
    with open(self.filename_of_csv, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    with open(output_filename, 'w') as file:
        # 📝 Export CSV data to JSON format
        json.dump(data, file, indent=4)

def calculate_total_fines(self):
    total_fine = 0.0

    with open(self.filename_of_csv, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 💰 Convert fine or treat empty string as 0.0 safely
            total_fine += float(row["fine_in_yen"] or 0.0)

    # 🧾 Print total fine formatted to 2 decimal places
    print(f"💰 Total Fine Collected: ¥{total_fine:.2f}")

def calculate_fines(self):
    updated_data = []

    with open(self.filename_of_csv, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # 📅 Convert borrowed date string to datetime object
            borrowed_date = datetime.strptime(row["borrowed date"], "%Y-%m-%d %H:%M:%S")

            # ✅ Normalize and convert subscribed to boolean
            subscribed = row["subscribed"].strip().lower() == 'true'

            # ⏳ Calculate allowed return days: 30 for subscribers, 7 otherwise
            allowed_return_date = borrowed_date + timedelta(days=30 if subscribed else 7)

            if datetime.now() > allowed_return_date:
                # 🔥 Fine is 1% of price if overdue
                fine = 0.01 * float(row["price_in_yen"])
            else:
                fine = 0.0

            row["fine_in_yen"] = str(fine)
            updated_data.append(row)

    with open(self.filename_of_csv, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)

def search_books(self, keyword):
    result = []

    with open(self.filename_of_csv, 'r') as file:
        reader = csv.DictReader(file)

        for b in reader:
            # 🔍 Case-insensitive keyword search in title
            if keyword.lower() in b['title'].lower():
                result.append(b)

    return result

def sort_books_by_price(self, descending=False):
    with open(self.filename_of_csv, 'r') as file:
        reader = csv.DictReader(file)
        books = list(reader)

    # ⬇️ Sort by price, default ascending unless descending=True
    sorted_books = sorted(books, key=lambda b: float(b["price_in_yen"]), reverse=descending)

    return sorted_books

def validate_title(self, title):
    # 🥪 Title must only contain letters and spaces
    return bool(re.match(r"^[A-Za-z\s]+$", title))

# 📂 JSON File Handling Methods
def create_json_file(self, json_filename, data):
    # 📑 Create a new JSON file with provided data
    with open(json_filename, 'w') as file:
        json.dump(data, file, indent=4)

def read_json_file(self, json_filename):
    # 📝 Read and return JSON content from file
    with open(json_filename, 'r') as file:
        return json.load(file)

def update_json_file(self, json_filename, updated_data):
    # ✍️ Overwrite JSON file with new data
    with open(json_filename, 'w') as file:
        json.dump(updated_data, file, indent=4)

def delete_json_file(self, json_filename):
    # 🔎 Check if JSON file exists before deleting
    if os.path.exists(json_filename):
        os.remove(json_filename)
    else:
        print("❌ File does not exist!")