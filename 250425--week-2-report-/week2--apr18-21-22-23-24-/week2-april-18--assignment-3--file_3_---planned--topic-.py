print("=======================================")

# Assignment - 3
# Workout Logger

# Features:

#     Log a workout (type, duration in minutes, date)

#     View total minutes worked out today/this week

#     List all logged workouts

#     Store in .json file

#     Use datetime for calculations



from datetime import datetime, timedelta
import os
import json


########################################################
########################################################
########################################################

print("------    List all logged workouts     ------")

list_of_workout = []


# [
#     {
#         "type": "hiking",
#         "duration": "1:00:00",
#         "date": "2025-04-21"
#     },
#     {
#         "type": "running",
#         "duration": "0:25:00",
#         "date": "2025-04-21"
#     },
#     {
#         "type": "swimming",
#         "duration": "0:20:00",
#         "date": "2025-04-21"
#     }
# ]

try:
        
    with open('file_3.json', 'r') as json_file:

        json_file_to_read = json.load(json_file)

        ### following line causes error - Error while listing all logged workouts : Expecting value: line 1 column 1 (char 0)

        # for iii in json_file_to_read:
        #     print(iii)

        # for i, exercise in enumerate(exercises, start=1):

        for i, exercise in enumerate(json_file_to_read, start=1):
            print(f"{i}. {exercise['type']}, {exercise['duration']}, {exercise['date']}, ")

            list_of_workout.append(
                    { "type": exercise['type'], 
                    "duration": exercise['duration'] , 
                    "date" : datetime.strptime(exercise['date'], "%Y-%m-%d"),
                    }, 
                 )

except Exception as e:
    print(f"Error while listing all logged workouts : {e} ")
    

# TypeError: Object of type datetime is not JSON serializable



print("=======================================")


print("------    Log a workout (type, duration in minutes, date)     ------")

### making my own json file with some data (note:) 
# list_of_workout = []
# add_workout = { "type": "hiking", "duration": str(timedelta(minutes= 60)) , "date" : datetime.today().strftime(format="%Y-%m-%d")}
# list_of_workout.append(add_workout)
add_workout = { "type": "running", "duration": str(timedelta(minutes= 25)) , "date" : datetime.today().strftime(format="%Y-%m-%d")} # 2025-04-21
# list_of_workout.append(add_workout) 

# add_workout = { "type": "swimming", "duration": str(timedelta(minutes= 20)) , "date" : str(datetime.today())} # 2025-04-21 07:45:55.951902
# add_workout = { "type": "badminton", "duration": str(timedelta(minutes= 45)) , "date" : str(datetime.today().strftime(format="%Y-%m-%d"))} 
# list_of_workout.append(add_workout)

# add_workout = { "type": "running", "duration": timedelta(minutes= 30) , "date" : datetime.today().strftime(format="%Y-%m-%d")} # TypeError: Object of type timedelta is not JSON serializable
# add_workout = { "type": "running", "duration": timedelta(minutes= 30) , "date" : datetime.today()} # TypeError: Object of type timedelta is not JSON serializable

{
  "type": "running",
  "duration": "0:30:00",
  "date": "2025-04-21 07:39:51.866000"
}

print("================")

list_of_workout_copy__add = list_of_workout.copy()
print(list_of_workout_copy__add)

print("============================")
with open('file_3.json', 'w', newline='') as json_file:

    # json_file_loaded = json.load(json_file)

    # json.dump(add_workout, json_file)

    list_of_workout__edited = []

    for iii in list_of_workout_copy__add:

        print(iii)
    print("============================")

    list_of_workout_copy__add.append({
  "type": "running",
  "duration": "0:30:00",
  "date": "2025-04-21 07:39:51.866000"
})
    print(list_of_workout_copy__add)
    print("================")

    print(list_of_workout_copy__add)

    # json.dump(list_of_workout, json_file)

    print("---------------------------")


    # list_of_workout.append(add_workout)

    # list_of_workout_str = json.dumps(list_of_workout, indent=2)
    # print(list_of_workout_str)


print("=======================================")


print("=======================================")
