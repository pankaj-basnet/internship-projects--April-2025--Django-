# improve code (modular) for json file handling in D:\GROW_CTS\PANKAJ-PROJECTS-\250418--Apr-18--revision-\assignments\file_1_b_done__chatgpt__cleaned_.py


# # Assignment - 6
# Habit Tracker

# Features:

#     Add a habit (name, frequency: daily/weekly)

#     Mark habit as done for today

#     View streak for each habit

#     Store data in .txt or .json (sn=)

#     Use datetime for streak calculation


# streak = []



#########################################################


# Assignment 6 - Habit Tracker (TXT version)

import os
import re
from datetime import datetime, timedelta

filename_of_txt = "file_6_assignment6_habits.txt"

# TXT file format:
# One habit per line, pipe-separated:
# id|habit|frequency|created_date|history (comma separated)|streak
# Example:
# 1|Exercise|daily|2025-04-20 10:00:00|2025-04-21,2025-04-22|2

class HabitRecord:
    _id_counter = 1  # class-level counter to assign unique IDs

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

            dates = [datetime.strptime(d, "%Y-%m-%d") for d in self.history]
            dates.sort(reverse=True)

            streak = 1
            for i in range(len(dates) - 1):
                delta = (dates[i] - dates[i + 1]).days
                expected_gap = 1 if self.frequency == "daily" else 7
                if 0 < delta <= expected_gap + 1:
                    streak += 1
                else:
                    break

            return streak
        except Exception as e:
            print(f"❌ Error calculating streak: {e}")
            return 0

    def to_line(self):
        # Convert habit data into a single line for writing to file
        created = self.created_date.strftime("%Y-%m-%d %H:%M:%S")
        history_str = ",".join(self.history)
        return f"{self.id}|{self.habit}|{self.frequency}|{created}|{history_str}|{self.streak}"

    @staticmethod
    def from_line(line):
        try:
            parts = line.strip().split("|")
            if len(parts) < 6:
                raise ValueError("❌ Malformed line.")

            habit_id = int(parts[0])
            habit = parts[1]
            frequency = parts[2]
            created_date = datetime.strptime(parts[3], "%Y-%m-%d %H:%M:%S")
            history = parts[4].split(",") if parts[4] else []
            streak = int(parts[5])

            habit_obj = HabitRecord(habit, frequency, created_date, history)
            habit_obj.id = habit_id
            habit_obj.streak = streak

            # Update the global counter to avoid duplicate IDs
            if habit_id >= HabitRecord._id_counter:
                HabitRecord._id_counter = habit_id + 1

            return habit_obj
        except Exception as e:
            print(f"❌ Error parsing line: {line} - {e}")
            return None

def validate_habit_input(habit, frequency):
    if not re.match(r"^[A-Za-z\s]+$", habit):
        raise ValueError("❌ Habit must contain only letters and spaces.")
    if frequency not in ["daily", "weekly"]:
        raise ValueError("❌ Frequency must be 'daily' or 'weekly'.")

def read_all_habits():
    habits = []
    if not os.path.exists(filename_of_txt):
        return habits

    try:
        with open(filename_of_txt, "r") as file:
            for line in file:
                habit = HabitRecord.from_line(line)
                if habit:
                    habits.append(habit)
        return habits
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []

def write_all_habits(habits):
    try:
        with open(filename_of_txt, "w") as file:
            for habit in habits:
                file.write(habit.to_line() + "\n")
    except Exception as e:
        print(f"❌ Error writing file: {e}")

def append_habit_record(habit: HabitRecord):
    validate_habit_input(habit.habit, habit.frequency)
    habits = read_all_habits()
    habits.append(habit)
    write_all_habits(habits)

def mark_habit_done(habit_id: int):
    try:
        habits = read_all_habits()
        today = datetime.now().strftime("%Y-%m-%d")
        found = False

        for habit in habits:
            if habit.id == habit_id:
                if today not in habit.history:
                    habit.history.append(today)
                    habit.streak = habit.calculate_streak()
                    print(f"✅ Marked habit '{habit.habit}' as done for today.")
                else:
                    print("⚠️ Already marked as done for today.")
                found = True
                break

        if not found:
            print(f"❌ No habit with ID {habit_id} found.")

        write_all_habits(habits)
    except Exception as e:
        print(f"❌ Error marking habit as done: {e}")

def view_streaks():
    habits = read_all_habits()
    for habit in habits:
        print(f"📌 {habit.habit} | Frequency: {habit.frequency} | Streak: {habit.streak} days")

def search_habits(keyword: str):
    try:
        habits = read_all_habits()
        return [h for h in habits if keyword.lower() in h.habit.lower()]
    except Exception as e:
        print(f"❌ Error in search_habits(): {e}")
        return []



#########################################################
print("\n================= ✅ Test 1: Add Habits =================")
habit1 = HabitRecord("Meditation", "daily", datetime(2025, 4, 20, 7, 0, 0), ["2025-04-21", "2025-04-22"])
habit2 = HabitRecord("Jogging", "daily", datetime(2025, 4, 19, 6, 0, 0), ["2025-04-20"])
habit3 = HabitRecord("Call Parents", "weekly", datetime(2025, 4, 1, 12, 0, 0), ["2025-04-07", "2025-04-14"])

append_habit_record(habit1)
append_habit_record(habit2)
append_habit_record(habit3)

print("\n================= ✅ Test 2: View All Habits =================")
habits = read_all_habits()
for h in habits:
    print(f"{h.id} | {h.habit} | {h.frequency} | Created: {h.created_date} | Streak: {h.streak}")

print("\n================= ✅ Test 3: Mark Habit Done =================")
mark_habit_done(habit_id=1)  # Should add today if not already marked
mark_habit_done(habit_id=3)  # Weekly habit
mark_habit_done(habit_id=99)  # Invalid ID

print("\n================= ✅ Test 4: View Updated Streaks =================")
view_streaks()

print("\n================= ✅ Test 5: Search Habits =================")
results = search_habits("med")
for r in results:
    print(f"🔍 Found: {r.habit} | ID: {r.id} | Frequency: {r.frequency}")

print("\n================= ✅ Test 6: Write and Re-Read =================")
write_all_habits(habits)  # Overwrite current file
refreshed = read_all_habits()
for r in refreshed:
    print(f"🔄 Reloaded: {r.habit} | Streak: {r.streak}")

print("\n================= ✅ Test 7: Input Validation =================")
try:
    validate_habit_input("123Invalid!", "daily")
except ValueError as e:
    print(e)

try:
    validate_habit_input("Walking", "hourly")
except ValueError as e:
    print(e)

try:
    validate_habit_input("Walking", "weekly")  # ✅ Valid
    print("✔️ Valid input passed!")
except ValueError as e:
    print(e)
#########################################################
#########################################################
#########################################################