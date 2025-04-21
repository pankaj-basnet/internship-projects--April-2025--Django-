import csv
import os

print('----------------------------------------------')
print('----------------------------------------------')

############# Define inventory CSV file name
inventory_file = "inventory.csv"

############# Load and display inventory if file exists
if os.path.exists(inventory_file):
    print("**** Existing Inventory ****")
    with open(inventory_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        total_value = 0
        for row in reader:
            # calculate total value for each item and display
            item_value = int(row['quantity']) * float(row['price'])
            print(row['name'], row['quantity'], row['price'], f"Value: {item_value}")
            total_value += item_value
        print(f"**** Total Inventory Value: {total_value} ****")
else:
    print("**** No existing inventory found. ****")

print('----------------------------------------------')

############# Ask user if they want to add a new product
add_product = input("Do you want to add a new product? (y/n): ")

if add_product.lower() in ['y', 'yes']:
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))

    # If inventory file doesn't exist, create it and write headers
    if not os.path.exists(inventory_file):
        with open(inventory_file, 'w', newline='') as f:
            fieldnames = ['name', 'quantity', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name': name, 'quantity': quantity, 'price': price})
    else:
        # Append to existing inventory
        with open(inventory_file, 'a', newline='') as f:
            fieldnames = ['name', 'quantity', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({'name': name, 'quantity': quantity, 'price': price})

print('----------------------------------------------')

############# Ask user if they want to update quantity
update_product = input("Do you want to update a product quantity? (y/n): ")

if update_product.lower() in ['y', 'yes']:
    update_name = input("Enter product name to update: ")
    new_quantity = int(input("Enter new quantity: "))

    updated_rows = []
    found = False

    with open(inventory_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['name'] == update_name:
                row['quantity'] = str(new_quantity)
                found = True
            updated_rows.append(row)

    if found:
        # Rewrite updated data to file
        with open(inventory_file, 'w', newline='') as f:
            fieldnames = ['name', 'quantity', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)
        print("**** Product updated successfully ****")
    else:
        print("**** Product not found ****")

print('----------------------------------------------')
print('----------------------------------------------')
