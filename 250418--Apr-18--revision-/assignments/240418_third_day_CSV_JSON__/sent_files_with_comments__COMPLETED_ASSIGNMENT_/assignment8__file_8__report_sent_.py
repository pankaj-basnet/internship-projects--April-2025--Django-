#######################################################################################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\report\assignment8__file_8__report_sent_.py
#######################################################################################################
#######################################################################################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\240418_third_day_CSV_JSON__\sent_files_with_comments__COMPLETED_ASSIGNMENT_\assignment8__file_8__report_sent_ copy.py
#######################################################################################################
#######################################################################################################

# Assignment - 8
# Daily Coding Tracker

# Features:

#     Log daily coding sessions (topic, language, duration)

#     View streaks and average coding time

#     Track topics (DSA, system design, etc.)

    # Export stats to .csv


#########################################################################################################

print("=======================================")

# from pack.csvframework import append_coding_record, CodingRecord, group_codings_by_week
from assignment8csvframework import CodingRecord, append_coding_record, validate_input, update_coding_price, edit_coding_by_id, search_codings
from datetime import datetime

print("=======================================")


coding_record = CodingRecord(
    topic="sundayProject",
    language = "python",
    start_date=datetime(2025, 4, 10, 20, 30, 0),
    subscribed=False,
    # price_in_yen=175500.50,
    finished_date =datetime(2025, 4, 26, 19, 15, 0)
)
append_coding_record(coding_record)

coding_record = CodingRecord(
    topic="sundayProjectTWO",
    language = "java",
    start_date=datetime(2025, 4, 1, 20, 30, 0),
    subscribed=False,
    finished_date =datetime(2025, 4, 20, 19, 15, 0)
)
append_coding_record(coding_record)




print("------------------------------------------")   

validate_input("title", 508500)

print("------------------------------------------")

update_coding_price(coding_id= 1, new_avg= 10)  

print("------------------------------------------")

search_codings(keyword = "django")
search_codings(keyword = "2025-04")


print("========================================================")
