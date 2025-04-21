print("============================================")

import json
import datetime

json_filename = 'workouts.json'

"""
Reading workouts from JSON file
"""
with open(json_filename, 'r') as json_file:
    print("Loading all logged workouts...")
    workouts = json.load(json_file)

print("=================================================")
print("Current workou:")
print(json.dumps(workouts, indent=2)) 
print("=================================================")


# Log  new workout
"""
Append a new workout entry and write the updated list back to file
"""
with open(json_filename, 'w') as json_file:
    workout_entry = {
        "type": "Running",
        "duration": 45,  # in minutes
        "date": datetime.datetime.now().strftime('%Y-%m-%d')  # ISO date format
    }
    print("Logging new workout:")
    print(workout_entry)

    workouts.append(workout_entry)  # Add to the existing list
    json.dump(workouts, json_file, indent=2)  # Save back to file

print("=================================================")
print("Workout log updated with new entry.")
print(json.dumps(workouts, indent=2))
print("=================================================")


################## Calculate total minutes workout today only
today = datetime.datetime.now().date()
total_today = 0

for workout in workouts:
    workout_date = datetime.datetime.strptime(workout["date"], '%Y-%m-%d').date()
    if workout_date == today:
        print("------------------------------")
        # print(workout["duration"], type(workout["duration"]))
        # print("------------------------------")
        # print(workout["type"])
        # time_str = workout["duration"]  
        # print("------------------------------")
        total_today += workout["duration"]

print(f"Total workout duration today ({today}): {total_today} minutes")
print("=================================================")


# ################## Calculate total minutes worked out THIS WEEK
start_of_week = today - datetime.timedelta(days=today.weekday())  # Monday
total_week = 0

for workout in workouts:
    workout_date = datetime.datetime.strptime(workout["date"], '%Y-%m-%d').date()
    if start_of_week <= workout_date <= today:
        total_week += workout["duration"]

print(f"Total workout duration this week (from {start_of_week}): {total_week} minutes")
print("=================================================")


# ################## List all workouts
print("Listing all workouts:")
for i, workout in enumerate(workouts, start=1):
    print(f"{i}. {workout['type']} - {workout['duration']} mins on {workout['date']}")

print("=================================================")
