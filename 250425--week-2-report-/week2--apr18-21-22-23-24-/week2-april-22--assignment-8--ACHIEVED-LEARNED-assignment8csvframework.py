######################################################################
######################################################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\report\assignment8csvframework.py
######################################################################
######################################################################

import csv
import json
import os
import re
from datetime import datetime, timedelta

filename_of_csv = "assignment8_.csv"
filename_of_json = "assignment8_.json"

# CSV file headers
headings = [
    "id", "topic", "language", "start date", "subscribed",
    "due date", "average_coding_time", "finished date", "streak", "coding_duration"
]

class CodingRecord:
    _id_counter = 1  # Static counter for unique ID assignment

    def __init__(self, topic, language, start_date, subscribed, finished_date=None):
        self.id = CodingRecord._id_counter
        CodingRecord._id_counter += 1

        self.topic = topic
        self.language = language
        self.start_date = start_date
        self.subscribed = subscribed
        self.due_date = start_date + timedelta(days=30 if subscribed else 7)

        self.average_coding_time = self.calculate_average_coding_time()
        self.finished_date = finished_date
        self.streak = self.calculate_streak()
        self.coding_duration = self.calculate_coding_duration()

    def calculate_coding_duration(self):
        if self.finished_date and self.finished_date > self.start_date:
            return self.finished_date - self.start_date
        return timedelta(days=0)

    def calculate_average_coding_time(self):
        try:
            with open(filename_of_csv, 'r', newline='') as file:
                reader = csv.DictReader(file)

                # get "no. of days or (make no. of hours later) from string "coding_duration"
                durations = [float(entry.get("coding_duration")[:2]) for entry in reader]
                return sum(durations) / len(durations) if durations else 0.0
        except Exception as e:
            print(f"❌ Error calculating average coding time: {e}")
            return 0.0

    def calculate_streak(self):
        try:
            if not self.finished_date:
                print("since you didnot put finished date, streak will become 0. Do you want to input data again?")
                return 0

            if (datetime.now() - self.finished_date) < timedelta(days=1):
                print("you have started and finished another coding session or habit too soon (within 24 hours). ")
                print("streak = 0 . Do you want to report this bug to developer? (software error)")
                return 0

            previous_codings = search_codings(self.topic)
            finished_codings = []

            for coding in previous_codings:
                if coding.get("finished date"):
                    try:
                        finished_dt = datetime.strptime(coding["finished date"], "%Y-%m-%d %H:%M:%S")
                        finished_codings.append(finished_dt)
                    except Exception:
                        continue

            finished_codings.sort(reverse=True)
            streak = 1  # Currently hardcoded to 1; logic can be improved

            print("===============================")
            print(finished_codings)
            print("===============================")
            for i in range(len(finished_codings) - 1, 0, -1):
                diff = (finished_codings[i] - finished_codings[i - 1]).days
                print(streak, diff, "steak, diff")
                if 1 <= diff <= 1.5:
                    print(streak, diff, "steak, diff")
                    print("------------------")
                    streak += 1
                else:
                    # print(f" streak from {finished_codings[i]} calculated . Current streak is {streak} ")
                    break

            return streak

        except Exception as e:
            print(f"❌ Error in calculate_streak(): {e}")
            return 0

    def to_dict(self):
        return {
            "id": self.id,
            "topic": self.topic,
            "language": self.language,
            "start date": self.start_date.strftime("%Y-%m-%d %H:%M:%S"),
            "subscribed": self.subscribed,
            "due date": self.due_date.strftime("%Y-%m-%d %H:%M:%S"),
            "average_coding_time": self.average_coding_time,

            # if finished date is None, change to empty string to write to csv.( to avoid error mb=)
            "finished date": self.finished_date.strftime("%Y-%m-%d %H:%M:%S") if self.finished_date else "",
            "streak": self.streak,
            "coding_duration": self.coding_duration
        }

    ### not necessary until now because DictReader has all data as list of dictionaries
    @staticmethod
    def from_dict(data):
        return CodingRecord(
            topic=data["topic"],
            language=data["language"],
            start_date=datetime.strptime(data["start date"], "%Y-%m-%d %H:%M:%S"),
            subscribed=data["subscribed"] in ["True", True],
            finished_date=datetime.strptime(data["finished date"], "%Y-%m-%d %H:%M:%S") if data["finished date"] else None
        )

def validate_input(topic, average_coding_time):
    if not re.match(r"^[A-Za-z\s]+$", topic):
        raise ValueError("Invalid topic. Only alphabets and spaces are allowed.")
    if not isinstance(average_coding_time, (float, int)):
        raise ValueError("average_coding_time must be a number.")
    

def read_all_csv():
    if not os.path.exists(filename_of_csv):
        return []
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            codings = list(reader)
    except Exception as e:
        return []  # 🧠 Common pitfall: empty or malformed CSV file # self note sn= mb-

def write_all_csv(codings):
    with open(filename_of_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(codings)


def append_coding_record(coding: CodingRecord):
    validate_input(coding.topic, float(0.0 if coding.average_coding_time is None else coding.average_coding_time) or 0.0)
    file_exists = os.path.exists(filename_of_csv)
    with open(filename_of_csv, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headings)
        if not file_exists:
            writer.writeheader()
        writer.writerow(coding.to_dict())


def update_coding_price(coding_id: int, new_avg: float):
    try:
        with open(filename_of_csv, 'r', newline='') as file:
            reader = csv.DictReader(file)
            codings = list(reader)

        for coding in codings:
            if int(coding["id"]) == coding_id:
                coding["average_coding_time"] = new_avg

        # with open(filename_of_csv, 'w', newline='') as file:
        #     writer = csv.DictWriter(file, fieldnames=headings)
        #     writer.writeheader()
        #     writer.writerows(codings)
                
        with open(filename_of_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(codings)


    except Exception as e:
        print(f"❌ Error updating price: {e}")


# def edit_coding_by_id() --- better than --- update_coding_price : (self note sn=) # beginner's pitfall
def edit_coding_by_id(coding_id: int, field: str, new_value):
    try:
        with open(filename_of_csv, 'r') as file:
            codings = list(csv.DictReader(file))
        for coding in codings:
            if int(coding['id']) == coding_id:
                coding[field] = new_value
        with open(filename_of_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headings)
            writer.writeheader()
            writer.writerows(codings)
    except Exception as e:
        print(f"❌ Error editing coding: {e}")


def search_codings(keyword: str):
    try:
        with open(filename_of_csv, 'r') as file:
            codings = list(csv.DictReader(file))
        return [b for b in codings if keyword.lower() in b['topic'].lower() or keyword in b['start date']]
    except Exception as e:
        print(f"❌ Error searching codings: {e}")
        return []






#########################################################
#########################################################
    
# import functions in report\assignment8__file_8__report_sent_.py ((  # modular # beginners= # self note= ))

#########################################################
#########################################################
    





    
#######################################################################################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\report\assignment8__file_8__report_sent_.py
#######################################################################################################

# Assignment - 8
# Daily Coding Tracker

# Features:

#     Log daily coding sessions (topic, language, duration)

#     View streaks and average coding time

#     Track topics (DSA, system design, etc.)

    # Export stats to .csv


#########################################################################################################

# print("=======================================")
# print("""D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\report\assignment8__file_8__report_sent_.py""")
# print("=======================================")

# # from pack.csvframework import append_coding_record, CodingRecord, group_codings_by_week
# from assignment8csvframework import CodingRecord, append_coding_record, validate_input, update_coding_price, edit_coding_by_id, search_codings
# from datetime import datetime

# print("=======================================")


# # coding_record = CodingRecord(
# #     topic="sundayProject",
# #     language = "python",
# #     start_date=datetime(2025, 4, 10, 20, 30, 0),
# #     subscribed=False,
# #     # price_in_yen=175500.50,
# #     finished_date =datetime(2025, 4, 21, 20, 15, 0)
# # )
# # append_coding_record(coding_record)


# coding_record = CodingRecord(
#     topic="sundayProject",
#     language = "python",
#     start_date=datetime(2025, 4, 10, 20, 30, 0),
#     subscribed=False,
#     # price_in_yen=175500.50,
#     finished_date =datetime(2025, 4, 22, 22, 15, 0)
# )
# append_coding_record(coding_record)

# coding_record = CodingRecord(
#     topic="sundayProject",
#     language = "java",
#     start_date=datetime(2025, 4, 1, 20, 30, 0),
#     subscribed=False,
#     finished_date =datetime(2025, 4, 23, 24, 15, 0)
# )
# append_coding_record(coding_record)




# print("------------------------------------------")   

# validate_input("title", 508500)

# print("------------------------------------------")

# update_coding_price(coding_id= 1, new_avg= 10)  

# print("------------------------------------------")

# search_codings(keyword = "django")
# search_codings(keyword = "2025-04")


# print("========================================================")



