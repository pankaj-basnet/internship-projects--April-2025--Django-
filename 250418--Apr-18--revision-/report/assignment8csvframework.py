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
                durations = [float(entry.get("coding_duration")[:2]) for entry in reader]
                return sum(durations) / len(durations) if durations else 0.0
        except Exception as e:
            print(f"❌ Error calculating average coding time: {e}")
            return 0.0

    def calculate_streak(self):
        try:
            if not self.finished_date:
                return 0

            if (datetime.now() - self.finished_date) < timedelta(days=1):
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
                    print("----")
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
            "coding_duration": self.coding_duration
        }

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



