# Assignment - 2
# Library Book Tracker

# Features:
#     Add a book (title, author, genre, borrowed date)
#     Mark book as returned
#     List currently borrowed books
#     Show overdue books (based on borrow date)
#     Store in .csv file

print("=================================================")

import csv
import datetime
import os

# with open('file2.json') as file2: # io.UnsupportedOperation: not writable # missing 'r' mode

########################################################
## adding a book (title, author, genre, borrowed date) 


print("---------    adding a book (title, author, genre, borrowed date)   --------  ")


filename_of_csv = 'file2.csv'

try:
    if os.path.exists(filename_of_csv):
        with open(filename_of_csv, 'a', newline='') as file2:

            # Error writing/appending csv file : dict contains fields not in fieldnames:
            # headings = ["title",  "date", "returned"]
            headings = ["title", "author", "genre", "borrowed date", "returned"]
            file_writer = csv.DictWriter(file2, headings)

            # book = {"title" : "rich dad", "date": datetime.date.today(), "returned": False} # datetime converted to string in csv
            book = {"title" : "disney", "author" : "many disney ", "genre": "childewn", "borrowed date": datetime.datetime.now(),  "returned": True}

            # file_writer.writeheader()
            file_writer.writerow(book)

    else:
            
        with open('file2.csv', 'w', newline = '') as file2:
            

            # headings = ["title", "date", "returned"]
            headings = ["title", "author", "genre", "borrowed date", "returned"]
            dict_writer = csv.DictWriter(file2, fieldnames= headings)

            # book = {"title" : "sherlock", "date": datetime.datetime.now(),  "returned": False}
            book = {"title" : "sherlock", "author" : "many,, authors ", "genre": "fantansy", "borrowed date": datetime.datetime.now(),  "returned": False}

            dict_writer.writeheader()
            dict_writer.writerow(book)

except Exception as e:
    print(f"Error writing/appending csv file : {e}")

print("=================================================")


########################################################
########################################################
### read csv and list currently borrowed books 


try:
    
    with open('file2.csv', 'r', newline= '') as file2:
        dict_reader = csv.DictReader(file2)

        print("----------      currently borrowed books     ----------")

        for row in dict_reader:
            # print(row) # print whole data of a book in a row


            is_returned = row.get("returned")
            # print(is_returned)

            # if not is_returned:
            # print(is_returned, type(is_returned))
            # print(not is_returned)
            # print("------")
            

            # print(is_returned, type(is_returned))
            # print(not is_returned)

            # if is_returned == False:
            # if is_returned == False or is_returned == 'False':

                # print(row["title"] , f' :  Borrowed on - {row["borrowed date"]}')

            # print("=============================")
            # if is_returned == False:
            if is_returned == 'False':
            # if is_returned == False or is_returned == 'False':

                print(row["title"] , f' :  Borrowed on - {row["borrowed date"][:10]}')
            # print("=============================")

            
            
            # is_returned = False
            # print(is_returned, type(is_returned))
            # print(not is_returned)

            # if not is_returned:
            # # if is_returned == False:
            # # if is_returned == False or is_returned == 'False':

            #     print(row["title"] , f' :  Borrowed on - {row["borrowed date"]}')

            # print("-------------------------------")


except Exception as e:
    print(f"there is some error in reading file2 : {e}")



print("=================================================")


########################################################
########################################################
### Mark book as returned (update field value in csv )

try:
    with open(filename_of_csv, 'r', newline='' ) as ctx:

        headings = ["title", "author", "genre", "borrowed date", "returned"]
        marker_reader = csv.DictReader(ctx, fieldnames= headings )

        read_all_rows = []

        # print(marker_reader)

        for row in marker_reader:
            # print(row['borrowed date'][:16])

            # updating returned as "True" if borrowed on "2025-04-12 21:22"
            if row['borrowed date'][:16] == "2025-04-12 21:22": 
                row["returned"] = True
                # print("2025-04-12 21:22")
            
            read_all_rows.append(row)
        
        print("marking book as returned ...")


except Exception as e:
    print(f"Error while marking book as returned (reading csv): {e}")


### write to the csv file
try:
    with open(filename_of_csv, 'w', newline='' ) as ctx:

        headings = ["title", "author", "genre", "borrowed date", "returned"]
        marker_writer = csv.DictWriter(ctx, fieldnames= headings )


        marker_writer.writerows(read_all_rows)


except Exception as e:
    print(f"Error while marking book as returned (writing csv) : {e}")


print("====================================================")


############################################################
############################################################



try:
    with open(filename_of_csv, 'r', newline='' ) as ctx:

        headings = ["title", "author", "genre", "borrowed date", "returned"]
        marker_reader = csv.DictReader(ctx, fieldnames= headings )

        next(marker_reader)

        for row in marker_reader:
            # print("***********************")

            # for key, value in row.items():
            #     print(key, value)
            #     print(row)
            #     date_in_row = row.get("borrowed date")
            #     print(date_in_row)

            #     if date_in_row:
            #         date_in_row = date_in_row[:10]
            #         print(date_in_row)
            #         date = datetime.datetime.strptime(date_in_row, "%Y-%m-%d")
            #         print(date, type(date))


            date_in_row = row.get("borrowed date")
            # print(date_in_row)

            if date_in_row:
                date_in_row = date_in_row[:10]
                # print(date_in_row)
                date = datetime.datetime.strptime(date_in_row, "%Y-%m-%d")
                # print(date, type(date))
            # print("--------------------------")
            
            # if row['borrowed date'][:16] == "2025-04-12 21:22": 
            #     print("2025-04-12 21:22", "--------------")

            due_date = date + datetime.timedelta(days=7)

            title = row.get("title")
            print(title ,  " : due date : ", due_date.strftime(format="%Y/%m/%d")[:10])



            # date_diff = datetime.datetime.now() - date
            # print(date_diff)

            # if date_diff > datetime.timedelta.days(7) :
            #     pass
            # print("----------------------")
            # print((datetime.datetime.now() - date))
            


except Exception as e:
    print(f"Error while finding duedate: {e}")


print("=======================================")

############################################################
############################################################

##################### 
# extra notes

# https://docs.python.org/3/library/csv.html#csv.DictReader
# If a row has more fields than fieldnames, the remaining data is put in a list and stored with the fieldname specified by restkey (which defaults to None).

### reading boolean values from a CSV in Python
# False <class 'str'>
# When reading boolean values from a CSV in Python, the values are read as **strings**, not actual booleans. For example, `False` in CSV becomes `"False"` (a non-empty string), which evaluates to `True` in conditionals — a common beginner pitfall. To convert correctly, use `value.lower() == 'true'` or compare directly: `value == 'True'`. Be cautious of inconsistent casing or spacing (`" false"`, `"TRUE"`), which can break your logic. It’s also wise to strip whitespace and normalize case: `value.strip().lower() == 'true'`. Always validate or sanitize input before converting for safe and predictable behavior.
    # https://stackoverflow.com/questions/50867308/pandas-read-csv-interprets-true-as-boolean-i-need-a-string


# print(not "is_returned") # False # https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/

# https://stackoverflow.com/questions/39010449/does-csv-dictreader-store-file-in-memory




###############################################
### additional notes
###############################################
    
# https://stackoverflow.com/questions/54816169/how-to-keep-null-values-when-writing-to-csv
        
    # You have two options here: change the csv.writing quoting option in Python, or tell PostgreSQL to accept quoted strings as possible NULLs (requires PostgreSQL 9.4 or newer)
    # Python csv.writer() and quoting

    # On the Python side, you are telling the csv.writer() object to add quotes, because you configured it to use csv.QUOTE_NONNUMERIC:

    #     Instructs writer objects to quote all non-numeric fields.

    # None values are non-numeric, so result in "" being written.

    # Switch to using csv.QUOTE_MINIMAL or csv.QUOTE_NONE:

    #     csv.QUOTE_MINIMAL
    #     Instructs writer objects to only quote those fields which contain special characters such as delimiter, quotechar or any of the characters in lineterminator.

    #     csv.QUOTE_NONE
    #     Instructs writer objects to never quote fields. When the current delimiter occurs in output data it is preceded by the current escapechar character.

    # Since all you are writing is longitude and latitude values, you don't need any quoting here, there are no delimiters or quotecharacters present in your data.

    # With either option, the CSV output for None values is simple an empty string:


# https://stackoverflow.com/questions/73493406/how-do-i-update-every-row-of-one-column-of-a-csv-with-python