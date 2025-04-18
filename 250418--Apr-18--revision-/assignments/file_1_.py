# Assignment - 1
# To-Do List Manager

# Features:

#     Add a task (title, due date, priority)

#     Mark task as completed

#     List pending/completed tasks

#     Store tasks in a .json or .csv file

#     Load tasks on app start



print("============================================")
import enum
# class Color(enum.Enum): --- RED = 1 --- GREEN = 2 --- BLUE = 3
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)
# print(Color.RED())
# print(Color.RED[1])


# print("============================================")

# https://stackoverflow.com/questions/1871524/how-can-i-convert-json-to-csv
# [
# //     {
# //       "pk": 22,
# //       "model": "auth.permission",
# //       "fields": {
# //         "codename": "add_logentry",
# //         "name": "Can add log entry",
# //         "content_type": 8
# //       }
# //     },
# //     {
# //       "pk": 23,
# //       "model": "auth.permission",
# //       "fields": {
# //         "codename": "change_logentry",
# //         "name": "Can change log entry",
# //         "content_type": 8
# //       }
# //     }
# // ]


print("============================================")

print("============================================")
import datetime
import json

json_filename = 'data.json'

with open (json_filename, 'r') as json_file:

    print("loading all tasks")
    json_loaded = json.load(json_file)
    


    ######### -----------------------------------
    ## prac= tricky
    print(json_loaded)

    ## json value is made by sn= , may be incorrect form of data 
    """
    [
    {
      "pk": 22,
      "model": "auth.permission"
    },
    {
      "pk": 23,
      "model": "auth.permission"
      
    },

    {
    "title": "python", 
    "due_date": "18/04/25, 11:09:", 
    "is_completed": false
    }
]

    """

    # for iii in json_loaded:
    #     print(iii, type(iii))
    #     print("---------------")
    #     for k,v in iii.items():
    #         print(k, v, type(k), type(v))

    ## OUTPUT
        # {'pk': 22, 'model': 'auth.permission'} <class 'dict'>       
        # ---------------
        # pk 22 <class 'str'> <class 'int'>
        # model auth.permission <class 'str'> <class 'str'>
        # {'pk': 23, 'model': 'auth.permission'} <class 'dict'>       
        # ---------------
        # pk 23 <class 'str'> <class 'int'>
        # model auth.permission <class 'str'> <class 'str'>
        # {'title': 'python', 'due_date': '18/04/25, 11:09:', 'is_completed': False} <class 'dict'>
        # ---------------
        # title python <class 'str'> <class 'str'>
        # due_date 18/04/25, 11:09: <class 'str'> <class 'str'>       
        # is_completed False <class 'str'> <class 'bool'>
            
print("----------")

print("=================================================")
print("=================================================")
print("=================================================")
print("=================================================")
print(json_loaded) # <---------------------------------

print("=================================================")
print("=================================================")
print("=================================================")
print("=================================================")
# [
#     {
#         "title": "python",
#         "due_date": "18/04/26, 16:03:",
#         "priority": "low",
#         "is_completed": false
#     },
#     {
#         "title": "django",
#         "due_date": "18/04/25, 16:03:",
#         "priority": "high",
#         "is_completed": true
#     },
#     {
#         "title": "python",
#         "due_date": "18/04/29, 16:03:",
#         "priority": "low",
#         "is_completed": false
#     },
#     {
#         "title": "python",
#         "due_date": "18/04/25, 16:11:",
#         "priority": "low",
#         "is_completed": false
#     },
#     {
#         "title": "python",
#         "due_date": "18/04/25, 16:16:",
#         "priority": "low",
#         "is_completed": false
#     },
#     {
#         "title": "python",
#         "due_date": "18/04/25, 16:16:",
#         "priority": "low",
#         "is_completed": false
#     }
# ]
print("=================================================")
# [
#     {
#         "title": "python",
#         "due_date": "18/04/26, 16:03:",
#         "priority": "low",
#         "is_completed": false
#     },
#     {
#         "title": "django",
#         "due_date": "18/04/25, 16:03:",
#         "priority": "high",
#         "is_completed": true
#     },
#     {
#         "title": "python",
#         "due_date": "18/04/29, 16:03:",
#         "priority": "low",
#         "is_completed": false
#     }
# ]
print("=================================================")
print("=================================================")
print("=================================================")

import datetime
import json

json_filename = 'data.json'


# https://stackoverflow.com/questions/12994442/how-to-append-data-to-a-json-file # 

# json might not be the best choice for on-disk formats; The trouble it has with appending data is a good example of why this might be. 

# with open (json_filename, 'r') as json_file: # ERROR # io.UnsupportedOperation: not writable (( error because of 'r'))
# with open (json_filename, 'r') as json_file: # ERROR # 
# with open (json_filename, 'a') as json_file: # ERROR # append not possible to json file on disk #so= #rsn= prac=
with open (json_filename, 'w') as json_file:
    """
    Appending tasks to json file, after adding a task to python "list" containingg the tasks """

    print("loading all tasks")
    # json_loaded = json.load(json_file)
    
    print("----------------------")
    task = { "title": "python", "due_date": datetime.datetime.now().strftime(format='%d/%m/%y, %H:%M:'), "priority": "low", "is_completed" : False, }
    print(task)

    print("------------------")

    print(json_loaded)
    print("--------")
    for iii in json_loaded:
        print(iii)
    print("------------------")

    ## MARK TASK AS COMPLETED ------ UPDATE THE LIST OF DICTIONARY(TASK)

    for iii in json_loaded:

        # updating task as completed in task with due date ("18/04/29, 16:03:")
        if iii["due_date"] == "18/04/29, 16:03:":
            print(iii)
            iii["is_completed"] = True
            print(iii)

    print(json_loaded)
    print("--------")
    for iii in json_loaded:
        print(iii)
    print("------------------")

    json.dump(json_loaded, json_file)


    ## APPENDING THE TASK TO THE LIST OF TASK
    # json_loaded.append(task)
    # print(json_loaded)
    # print("------------------")

    # json.dump(json_loaded, json_file)

    


print("----------------------")
task = { "title": "python", "due_date": datetime.datetime.now().strftime(format='%d/%m/%y, %H:%M:'), "priority": "high", "is_completed" : False, }
print(task)



print("============================================")



print("============================================")


# print("============================================")


# print("============================================")