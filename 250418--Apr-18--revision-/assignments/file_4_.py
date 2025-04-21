# improved clean code (modular) in D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\file_2__CSV__improved__chatgpt_ 333__240521__.py

### =============================================
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\file_4_.py
### =============================================

# Assignment - 4
# Simple Inventory Manager

# Features:

#  (a)   Add product (name, quantity, price) --- done

#  (b)   Update product quantity

#  (c)   View product list with total value

#  (d)   Store in .csv file

#  (e)   Load existing inventory on startup --- done

# name,quantity,price,total
# rice,50,100,5000
# dal,10,150,1500

from datetime import datetime
import csv
import os

print("----------------------------------------")

##################################################################
##################################################################


csv_filename = 'file_4.csv'

# load products
def load_products():

    ### already made a 'file_4.csv' and added a dictionary with product info in a list to avoid any error (already created file manually) self note

    print("==============================")

    print("#  (e)   Load existing inventory on startup  ")

    #### later write code to check if file exist or not before reading csv file or loading data from csv file at the beginning of this program
    # if file.exist():
    #     ...
    #     dictreader()
    # else:
    #     with open() 'w'
    #     ...
    #     dictreader()

    try:
        with open(csv_filename) as ctx:


            headings = ["name", "quantity", "price", "total"]
            dict_reader = csv.DictReader(ctx, fieldnames= headings)
            next(ctx)

            product_list = []
            # product_list = list(dict_reader)
            # print(product_list)

            # next(ctx) # (function) def next( __i: , ) -> Return the next item from the iterator.

            for product in dict_reader:


                product_list.append(product)
                # print("============================")

            #     print(product)

                for field, value in product.items():
                    print(f'{field} : {value} ', end='   ')
                
            #     print("\n-----------")
                print("")

            # print(product_list)
                    
            return product_list


            print("===============================================")



    except Exception as e:
        print(f"❌ Error loading products: {e}")
        # print(f"❌ Error loading products: {e}") # ❌ Error loading products: [Errno 2] No such file or directory: 'file__4.csv'


print("----------------------------------------")

##################################################################
##################################################################


# headings variable already in def load_products(): (sn= con= )

headings = ["name", "quantity", "price", "total"] 
print("#  (a)   Add product (name, quantity, price)")

def add_product(product):
    """#  (a)   Add product (name, quantity, price)"""

    try:
        file_exists = os.path.exists(csv_filename)

        with open(csv_filename, 'a' if file_exists else 'w' , newline= '') as ctx:
        
            dict_writer = csv.DictWriter(ctx, fieldnames= headings)
                
            if not file_exists:
                dict_writer.writeheader()
            
            # convert datetime to string
            # product["no datetime field"]
            
            dict_writer.writerow(product)

                
    
    except Exception as e:
        print(f"❌ Error adding products: {e}")



print("----------------------------------------")

##################################################################
##################################################################

# print(" #  (b)   Update product quantity    ")


def update_product(name = "sugar222", quantity = 99):

    print(" #  (b)   Update product quantity    ")
    headings = ["name", "quantity", "price", "total"]

    product_list = []

    try:
        with open(csv_filename) as ctx:

            dict_reader = csv.DictReader(ctx, fieldnames= headings)
            next(ctx)

            product_list = list(dict_reader)
            
            # print(product_list) 
            # return product_list
        
        file_exists = os.path.exists(csv_filename)


        # with open(csv_filename, 'a' if file_exists else 'w' , newline= '') as ctx: ## always do write , not append to update existing value of csv
        with open(csv_filename, 'w' , newline= '') as ctx:
        
            dict_writer = csv.DictWriter(ctx, fieldnames= headings)
                
            # if not file_exists:
            #     dict_writer.writeheader()
            dict_writer.writeheader()
            
            # convert datetime to string
            # product["no datetime field"]
            
            for product in product_list:
                print("--------------")
                print(product)
                print("--------------")

                product_name = product.get("name") 
                print(product_name)
                if product_name == name:
                    print(product_name)
                    print("=======================")
                    product["quantity"] = quantity
                    print("=======================")
                    print(product)
                    print("=======================")

            
            dict_writer.writerow(product)
        
        
    except Exception as e:
        print(f"❌ Error updating products: {e}")



print("----------------------------------------")

##################################################################
##################################################################


print("----------------------------------------")

def main():

    load_products()

    product_one = {"name": "sugar", "quantity": 20, "price": 100, "total": (20 * 100)}
    add_product(product_one)

    update_product(name= "sugar222", quantity= 199)






main()

print("----------------------------------------")
