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

    print("loading all tasks")
    json_loaded = json.load(json_file)
    
 
    print(json_loaded)
print("=================================================")
print("=================================================")
print(json_loaded) # <---------------------------------

print("=================================================")
print("=================================================")

import datetime
import json

json_filename = 'data.json'

with open (json_filename, 'w') as json_file:
    """
    Appending tasks to json file, after adding a task to python "list" containingg the tasks """

    print("----------------------")
    

    print(json_loaded)
    print("--------")
    for iii in json_loaded:
        print(iii)
    print("------------------")

    ## MARK TASK AS COMPLETED ------ UPDATE THE LIST OF DICTIONARY(TASK)

    for iii in json_loaded:

        # updating task as completed in task with due date ("18/04/29, 16:03:")
        if iii["due_date"] == "18/04/26, 16:03:":
            print(iii)
            iii["is_completed"] = True
            # print(iii)

    print(json_loaded)
    print("--------")
    for iii in json_loaded:
        print(iii)
    print("------------------")

    json.dump(json_loaded, json_file)

with open (json_filename, 'w') as json_file:

    ## APPENDING THE TASK TO THE LIST OF TASK

    """
    appendin
    
    """
    task = { "title": "python", "due_date": datetime.datetime.now().strftime(format='%d/%m/%y, %H:%M:'), "priority": "low", "is_completed" : False, }
    print(task)

    print("------------------")

    json_loaded.append(task)
    print(json_loaded)
    print("------------------")

    json.dump(json_loaded, json_file)


print("============================================")
print(json_loaded)
print("--------")
for iii in json_loaded:
    print(iii)
print("------------------")
print("============================================")

# with open (json_filename, 'w') as json_file:
    
with open (json_filename, 'r') as json_file:
    """
    list pending task
    """


    print("loading all tasks")
    json_loaded = json.load(json_file)


    # print(json_loaded)
    tasks_pending = []
    for task in json_loaded:
        if task["is_completed"] == False:
            tasks_pending.append(task)
    print(tasks_pending)




print("============================================")

"""
open() function to open json file for read, write or append purposes
appending to json file on disk is not recommended. Use csv instead (source: stackoverflow)
temporary solution to appending json file is to "add to list of tasks" and, overwrite json file with whole the list
update value of json data after converting json data to python object

json module for json file manipulation
iterate over data structures inside json file to access members
convert datetime object to string using strftime() method
"""


# print("============================================")


# print("============================================")