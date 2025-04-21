# Assignment - 1
# To-Do List Manager

# Features:

#     Add a task (title, due date, priority)

#     Mark task as completed

#     List pending/completed tasks

#     Store tasks in a .json or .csv file

#     Load tasks on app start

print("============================================")
import datetime
import json

json_filename = 'data.json'

 
with open (json_filename, 'r') as json_file:
    """
    read from json file  and display, and store it in a variable
    """

    print("loading all tasks")
    json_loaded = json.load(json_file)
    
print("=================================================")
print("=================================================")
json_loaded_str = json.dumps(json_loaded, indent=2) # <-----------
print(json_loaded_str)
print("=================================================")
print("=================================================")

import datetime
import json

json_filename = 'data.json'

with open (json_filename, 'w') as json_file:
    """
    update json object (note: temporary hack is to update already created global variable "json_loaded" and write (not append) the value of the variable to the JSON file)
    """

    ## MARK TASK AS COMPLETED ------ UPDATE THE LIST OF DICTIONARY(TASK)
    for iii in json_loaded:

        # updating task as completed in task with due date ("18/04/29, 16:03:")
        if iii["due_date"] == "18/04/26, 16:03:":
            print(iii)
            iii["is_completed"] = True
            # print(iii)

    json.dump(json_loaded, json_file)

print("----------------------------------------")
json_loaded_str = json.dumps(json_loaded, indent=2) # <-----------
print(json_loaded_str)
print('["is_completed"] = True  done')
print("----------------------------------------")


with open (json_filename, 'w') as json_file:
    """
    appending json object (note: temporary hack is to append to already created global variable "json_loaded" and write (not append) the value of the variable to the JSON file)
    
    """
    task = { "title": "python", "due_date": datetime.datetime.now().strftime(format='%d/%m/%y, %H:%M:'), "priority": "low", "is_completed" : False, }
    print(task)

    print("------------------")

    json_loaded.append(task)
    print(json_loaded)
    print("------------------")

    json.dump(json_loaded, json_file)



print("----------------------------------------")
json_loaded_str = json.dumps(json_loaded, indent=2) # <-----------
print(json_loaded_str)
print('json_loaded.append(task)')
print("----------------------------------------")



# with open (json_filename, 'w') as json_file:
with open (json_filename, 'r') as json_file:
    """
    list pending task
    """

    print("loading all  pending tasks")
    json_loaded = json.load(json_file)

    # print(json_loaded)
    tasks_pending = []
    for task in json_loaded:
        if task["is_completed"] == False:
            tasks_pending.append(task)
    print(tasks_pending)

json_formatted_str = json.dumps(tasks_pending, indent=2)
print(json_formatted_str)


print("============================================")



