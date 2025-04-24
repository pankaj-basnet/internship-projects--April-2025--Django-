##################################################
##################################################
# # Assignment - 6
# Habit Tracker

# Features:

#     Add a habit (name, frequency: daily/weekly)

#     Mark habit as done for today

#     View streak for each habit

#     Store data in .txt or .json (sn=)

#     Use datetime for streak calculation
##################################################
##################################################

# Assignment 6 - Habit Tracker

import json
import os
import re
from datetime import datetime, timedelta

filename_of_json = "file_6_extra__assignment6_habits.json"

print("==========================================")
# JSON file structure: each record is a habit dict
# {
#     "id": 1,
#     "habit": "Exercise",
#     "frequency": "daily",
#     "created_date": "2025-04-20 10:00:00",
#     "history": ["2025-04-21", "2025-04-22"],  # YYYY-MM-DD only
#     "streak": 2
# }

class HabitRecord:
    _id_counter = 1  # static counter for unique ID

    def __init__(self, habit, frequency, created_date=None, history=None):
        self.id = HabitRecord._id_counter
        HabitRecord._id_counter += 1

        self.habit = habit
        self.frequency = frequency
        self.created_date = created_date or datetime.now()
        self.history = history or []  # list of "YYYY-MM-DD" strings
        self.streak = self.calculate_streak()

    def calculate_streak(self):
        try:
            if not self.history:
                return 0

            # Convert history strings to datetime and sort descending
            history_dates = [datetime.strptime(date, "%Y-%m-%d") for date in self.history]
            history_dates.sort(reverse=True)

            streak = 1
            for i in range(len(history_dates) - 1):
                delta = (history_dates[i] - history_dates[i+1]).days
                expected = 1 if self.frequency == "daily" else 7
                if 0 < delta <= expected + 1:  # allow 1 day buffer
                    streak += 1
                else:
                    break

            return streak
        except Exception as e:
            print(f"❌ Error calculating streak: {e}")
            return 0

    def to_dict(self):
        return {
            "id": self.id,
            "habit": self.habit,
            "frequency": self.frequency,
            "created_date": self.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            "history": self.history,
            "streak": self.streak
        }

    @staticmethod
    def from_dict(data):
        return HabitRecord(
            habit=data["habit"],
            frequency=data["frequency"],
            created_date=datetime.strptime(data["created_date"], "%Y-%m-%d %H:%M:%S"),
            history=data.get("history", [])
        )

def validate_habit_input(habit, frequency):
    if not re.match(r"^[A-Za-z\s]+$", habit):
        raise ValueError("❌ Habit name must contain only letters and spaces.")
    if frequency not in ["daily", "weekly"]:
        raise ValueError("❌ Frequency must be either 'daily' or 'weekly'.")

def read_all_habits():
    if not os.path.exists(filename_of_json):
        return []

    try:
        with open(filename_of_json, "r") as file:
            habits = json.load(file)
            return habits
    except Exception as e:
        print(f"❌ Error reading habits: {e}")
        return []

def write_all_habits(habits):
    try:
        with open(filename_of_json, "w") as file:
            json.dump(habits, file, indent=4)
    except Exception as e:
        print(f"❌ Error writing habits: {e}")

def append_habit_record(habit: HabitRecord):
    validate_habit_input(habit.habit, habit.frequency)
    habits = read_all_habits()
    habits.append(habit.to_dict())
    write_all_habits(habits)

def mark_habit_done(habit_id: int):
    try:
        habits = read_all_habits()
        today_str = datetime.now().strftime("%Y-%m-%d")
        for habit in habits:
            if habit["id"] == habit_id:
                if today_str not in habit["history"]:
                    habit["history"].append(today_str)
                    temp_obj = HabitRecord.from_dict(habit)
                    habit["streak"] = temp_obj.calculate_streak()
                    print(f"✅ Marked habit '{habit['habit']}' as done for today.")
                else:
                    print("⚠️ Already marked as done for today.")
                break
        else:
            print(f"❌ No habit with ID {habit_id} found.")

        write_all_habits(habits)
    except Exception as e:
        print(f"❌ Error marking habit: {e}")

def view_streaks():
    habits = read_all_habits()
    for habit in habits:
        print(f"📌 {habit['habit']} | Frequency: {habit['frequency']} | Streak: {habit['streak']} days")

def search_habits(keyword: str):
    try:
        habits = read_all_habits()
        results = [h for h in habits if keyword.lower() in h["habit"].lower()]
        return results
    except Exception as e:
        print(f"❌ Error in search_habits(): {e}")
        return []

habit11 = HabitRecord.from_dict(
    {
    "id": 1,
    "habit": "Exercise",
    "frequency": "daily",
    "created_date": "2025-04-20 10:00:00",
    "history": ["2025-04-21", "2025-04-22"],  # YYYY-MM-DD only 

    "streak": 2
}
    )
append_habit_record(habit11)
search_habits("exe")
view_streaks()
mark_habit_done(1 )
# write_all_habits(habits)
# validate_habit_input(habit, frequency)
read_all_habits()


# json --- list of dictionary --- list of dates (sn=)    # "history": ["2025-04-21", "2025-04-22"],  # YYYY-MM-DD only  ## pitfall= beginners= junior programmer=