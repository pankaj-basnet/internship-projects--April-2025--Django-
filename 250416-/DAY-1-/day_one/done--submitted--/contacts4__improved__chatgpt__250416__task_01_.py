import csv
import os

csv_file = "day-1-fair-2-.csv"
print('----------------------------------------------')

# Function to display all contacts
def display_contacts():
    if not os.path.exists(csv_file):
        print("**** You have no contacts ****")
        return

    with open(csv_file, 'r', newline='') as csv_file_reader:
        contact_reader = csv.DictReader(csv_file_reader)
        print("**** Your all contacts: ****")
        for row in contact_reader:
            print(row["number"], row["name"], row["date"], row["email"])
        print("--------------------------------------")

# Function to search a contact by name
def search_contact():
    if not os.path.exists(csv_file):
        print("**** You have no contacts ****")
        return

    with open(csv_file, 'r', newline='') as csv_file_reader:
        contact_reader = csv.DictReader(csv_file_reader)
        print("**** Searching for a contact: ****")
        question = input("Do you want to search for a name? (y/n): ").lower()

        if question in ["y", "yes"]:
            search_name = input("Enter name to search: ")
            found = False
            for row in contact_reader:
                if row["name"].lower() == search_name.lower():
                    print(row["number"], row["name"], row["date"], row["email"])
                    found = True
                    break
            if not found:
                print("No contact found with that name.")

# Function to add a new contact
def add_contact():
    number = int(input("Enter a number to add to contacts: "))
    name = input("Enter a name: ")
    date = input("Enter a date (e.g., 25/04/16): ")
    email = input("Enter an email: ")

    new_contact = {
        "number": number,
        "name": name,
        "date": date,
        "email": email
    }

    headings = ["number", "name", "date", "email"]

    if not os.path.exists(csv_file):
        with open(csv_file, 'w', newline='') as csv_file_write:
            contact_writer = csv.DictWriter(csv_file_write, fieldnames=headings)
            contact_writer.writeheader()
            contact_writer.writerow(new_contact)
    else:
        with open(csv_file, 'a', newline='') as csv_file_write:
            contact_writer = csv.DictWriter(csv_file_write, fieldnames=headings)
            contact_writer.writerow(new_contact)

# Main logic
def main():
    display_contacts()
    search_contact()
    add_contact()
    print("Contact added successfully!")

if __name__ == "__main__":
    main()

print('----------------------------------------------')
