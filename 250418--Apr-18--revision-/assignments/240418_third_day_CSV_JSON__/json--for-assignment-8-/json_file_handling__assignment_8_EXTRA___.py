#############################################################
#############################################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\240418_third_day_CSV_JSON__\json--for-assignment-8-\json_file_handling__assignment_8_EXTRA___.py
#############################################################
#############################################################
### D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\240418_third_day_CSV_JSON__\json--for-assignment-8-\json__DIFFICULT__FILE_HANDLING__250423__not_tested___not_checked__.py
## D:\src\PY\MIT-python-2022\code-only--lec-book--\code---edited---copied\growcts_python_django\presentation\chatgpt-prompt\json__DIFFICULT__FILE_HANDLING__250423__not_tested___not_checked__.py
### D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\240418_third_day_CSV_JSON__\json--for-assignment-8-\json__DIFFICULT__FILE_HANDLING__250423__not_tested___not_checked__.py --- chatgpt-prompt\json__DIFFICULT__FILE_HANDLING__250423__not_tested___not_checked__.py
## D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\240418_third_day_CSV_JSON__\json--for-assignment-8-\json_file_handling__assignment_8_EXTRA___.py
#############################################################
#############################################################

import json
import os
import re
from datetime import datetime, timedelta

filename_of_json = "json_assignment8_.json"

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

        self.average_coding_time = self.calculate_average_coding_time() # 0.0  # 🤖 Placeholder, can be updated later
        self.finished_date = finished_date
        self.streak = self.calculate_streak() # 1  # 🔁 Default streak = 1, may be updated dynamically
        self.coding_duration = self.calculate_coding_duration()
        self.finished_dates = [] if not finished_date else [[finished_date.strftime("%Y-%m-%d %H:%M:%S")]]  # 🆕✨

    def calculate_coding_duration(self):
        if self.finished_date and self.finished_date > self.start_date:
            return (self.finished_date - self.start_date).days
        return 0
    
    def calculate_average_coding_time(self):
        try:
            records = read_all_json()
            for rec in records:
 
                durations = [float(entry.get("coding_duration")[:2]) for entry in rec]
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

            previous_codings = search_codings_json(self.topic)
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
            "finished date": self.finished_date.strftime("%Y-%m-%d %H:%M:%S") if self.finished_date else "",
            "streak": self.streak,
            "coding_duration": self.coding_duration,
            "finished_dates": self.finished_dates  # 🆕
        }

    @staticmethod
    def from_dict(data):
        return CodingRecord(
            topic=data["topic"],
            language=data["language"],
            start_date=datetime.strptime(data["start date"], "%Y-%m-%d %H:%M:%S"),
            subscribed=data["subscribed"] in [True, "True"],
            finished_date=datetime.strptime(data["finished date"], "%Y-%m-%d %H:%M:%S") if data["finished date"] else None
        )

def validate_input(topic, average_coding_time):
    if not re.match(r"^[A-Za-z\s]+$", topic):
        raise ValueError("Invalid topic. Only alphabets and spaces are allowed.")
    if not isinstance(average_coding_time, (float, int)):
        raise ValueError("average_coding_time must be a number.")

def read_all_json():
    if not os.path.exists(filename_of_json):
        return []
    with open(filename_of_json, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # 🧠 Common pitfall: empty or malformed JSON file

def write_all_json(records):
    with open(filename_of_json, 'w') as file:
        json.dump(records, file, indent=4)

def append_coding_record_json(coding):
    validate_input(coding.topic,  float(0.0 if coding.average_coding_time is None else coding.average_coding_time) or 0.0)
    records = read_all_json()
    records.append(coding.to_dict())
    write_all_json(records)
    print(f"✅ Appended record with ID {coding.id} to JSON file.")

def update_average_json(coding_id, new_avg):
    records = read_all_json()
    for rec in records:
        if rec["id"] == coding_id:
            rec["average_coding_time"] = new_avg
            print(f"✅ Updated average_coding_time for ID {coding_id}.")
            break
    write_all_json(records)


# edit_coding_json() delegates tasks to read_all_json() and write_all_json(records) # modular # beginners= # self note=
# def edit_coding_json()  --- better than --- edit_coding_json() : (self note sn=) # beginner's pitfall
def edit_coding_json(coding_id, field, new_value):
    records = read_all_json()
    for rec in records:
        if rec["id"] == coding_id:
            rec[field] = new_value
            print(f"✅ Updated field '{field}' for ID {coding_id}.")
            break
    write_all_json(records)

def search_codings_json(keyword):
    result = []
    records = read_all_json()
    for rec in records:
        if keyword.lower() in rec["topic"].lower() or keyword in rec["start date"]:
            result.append(rec)
    print(f"🔍 Found {len(result)} matching records for keyword '{keyword}'.")
    return result

# ✅ Demo usage (remove or comment during module import)
if __name__ == "__main__":
    print("\n🔧 Demo run for JSON coding tracker framework\n")

    coding_record = CodingRecord(
        topic="JSONSessionOne",
        language="python",
        start_date=datetime(2025, 4, 15, 10, 0, 0),
        subscribed=True,
        finished_date=datetime(2025, 4, 22, 23, 0, 0)
    )
    append_coding_record_json(coding_record)

    update_average_json(coding_id=1, new_avg=3.5)
    edit_coding_json(coding_id=1, field="language", new_value="Python3")
    search_codings_json("JSON")
