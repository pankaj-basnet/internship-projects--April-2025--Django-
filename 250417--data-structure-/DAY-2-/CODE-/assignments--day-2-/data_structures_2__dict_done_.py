
print("===========================================")


# <!-- ASSINGMENT (4) -->

# Inventory Management System

# You are building a mini system for a small shop to track inventory.

#     Create a dictionary where keys are item names and values are stock counts.

#     Write functions to:

#         Add a new item

#         Restock existing item

#         Sell item (reduce count)

#         Print all inventory sorted by name

#         Add a loop that takes commands (add, sell, print, exit) via input() to simulate usage


shop_items = { "coffee": 500, "milk": 50, "sugar": 100}


def display_name():
    print(f"displaying name of items ... )")
    for item_name in sorted(shop_items):
        print(item_name, shop_items[item_name])

display_name()
print('-----------------------')

def add_new_product_to_inventory ( item_name, number_of_items):
    print(f"addition's processing ... ({item_name} --> {number_of_items}) units")

    if item_name in shop_items:
        raise ValueError('item already exist. use "restock_item_to_inventory" functionality')
    
    shop_items[item_name] = number_of_items
    print(shop_items[item_name])

add_new_product_to_inventory("tea", 60)
    

def restock_item_to_inventory ( item_name, number_of_items):
    print(f"restock's processing ... ({item_name} --> {number_of_items}) units")

    shop_items[item_name] += number_of_items
    print(shop_items[item_name])

restock_item_to_inventory("coffee", 100)
    

def sell_item_to_inventory ( item_name, number_of_items):
    print(f"sale's processing ... ({item_name} --> {number_of_items}) units")

    shop_items[item_name] -= number_of_items
    print(shop_items[item_name])

sell_item_to_inventory("coffee", 50)

print('----------')

while True:

    choose = input("choose: (1) sell  (2) add new product  (3) restock  (4) exit : ")
    
    match choose:
        case "sell" :
            item = "coffee"
            sell_item_to_inventory(item_name=item, number_of_items=200)
            print(shop_items)

        case "add":
            # item = "coffee" # ValueError: item already exist.
            item = "drinks"
            add_new_product_to_inventory(item_name = item, number_of_items = 100)
            print(shop_items)

        case "restock":
            
            item = "drinks"

            restock_item_to_inventory(item_name = item, number_of_items = 100)
            print(shop_items)
        
        case "exit":
            break




print("===========================================")
