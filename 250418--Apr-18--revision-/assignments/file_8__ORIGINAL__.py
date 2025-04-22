#####################################################
#####################################################
# file_8__ORIGINAL__.py # #  pack\assignment8m4d22csvframework__ORIGINAL_250422__.py
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\file_8__ORIGINAL__.py
#####################################################

#  D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\pack\assignment8m4d22csvframework__ORIGINAL_250422__.py
#####################################################
#####################################################
#####################################################
# Assignment - 8
# Daily Coding Tracker

# Features:

#     Log daily coding sessions (topic, language, duration)

#     View streaks and average coding time

#     Track topics (DSA, system design, etc.)

    # Export stats to .csv



print("=======================================")

# from pack.csvframework import append_book_record, BookRecord, group_books_by_week
from pack.assignment8m4d22csvframework__ORIGINAL_250422__ import BookRecord, append_book_record, validate_input, update_book_price, edit_book_by_id, search_books
from datetime import datetime

print("=======================================")


book_record = BookRecord(
    topic="django",
    start_date=datetime(2025, 4, 10, 20, 30, 0),
    subscribed=False,
    price_in_yen=175500.50,
    finished_date =datetime(2025, 4, 26, 19, 15, 0)
)

book_record = BookRecord(
    topic="data science",
    start_date=datetime(2025, 4, 1, 20, 30, 0),
    subscribed=False,
    price_in_yen=175500.50,
    finished_date =datetime(2025, 5, 26, 19, 15, 0)
)

append_book_record(book_record)
# group_books_by_week()

print("------------------------------------------")   
# # def validate_input(title, price):
validate_input("title", 508500)
print("------------------------------------------")
# # def append_book_record(book: BookRecord):
# # append_book_record(book: BookRecord)
# print("------------------------------------------")
# # def export_to_json():
# export_to_json()
# print("------------------------------------------")
# # def update_book_price(book_id: int, new_price: float):
update_book_price(book_id= 2, new_price= 99999)
print("------------------------------------------")
# # def delete_book_by_id(book_id: int):
# delete_book_by_id(book_id = 1)
# print("------------------------------------------")
# # def edit_book_by_id(book_id: int, field: str, new_value):
# edit_book_by_id(book_id= 1, field= "topic" , new_value= False)
edit_book_by_id(book_id= 1, field= "topic" , new_value= "replace_topic")
print("------------------------------------------")
# # def search_books(keyword: str):
search_books(keyword = "djan")
search_books(keyword = "2025-04")
# search_books(keyword = "apyth") # ❌ Error searching books: 'started date'
# print("------------------------------------------")
# # def group_books_by_week():
# group_books_by_week()


print("========================================================")
