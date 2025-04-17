

# <!-- ASSINGMENT (5) -->

print("ASSINGMENT (5)")
# Chat Room Tracker
# Track users in chat rooms using dictionary + sets:

#     Add/Remove users

#     List users per room

#     Get common users in two rooms


print('----------')

# users = [ "pankaj", "luckey", "biraj"]
# rooms = [ "python", "node", "data"]

users = [ "pankaj", "luckey", "biraj","biraj"]
rooms = [ "python", "node", "data",  "data"]


# room_python = {"python": "pankaj", "python": "luckey", }
# room_node = {"node": "pankaj", "node": "biraj"}

# combo = zip(users, rooms)
users_in_room_init  = zip(users, rooms)

print(users_in_room_init)

unique_users_in_room = set()

for iii in users_in_room_init:
    unique_users_in_room.add(iii)
    print(f'{iii} added successfully')

print(unique_users_in_room)

print('----------')

### remove "biraj"
users.remove("biraj")

print('---------------------')


# room_python = {"python": "pankaj", "python": "luckey", }
# room_node = {"node": "pankaj", "node": "biraj"}
room = {  "pankaj" : "python",   "luckey" : "python",  "pankaj": "node",  "biraj": "node"} ## ( creating dict with duplicate keys)
print(room)
print(room ["pankaj"])

### add "aayush" to room
room ["aayush"] = "data" # update same as create in dictionary
print(room)

### add "aayush" to room (( xxx ----- BUG)) --- aayush is in two room-chat 
room ["aayush"] = "mern" # update same as create in dictionary
print(room)

### remove "aayush" from room
del room["aayush"] # "aayush" removed or deleted
print(room)

print("===========================================")

room_in_set = set(room)
print(room_in_set)

# room_in_set = {  {"pankaj"  :  "python"},   {"luckey"  :  "python"},  {"pankaj" :  "node"},  {"biraj" :  "node"}} # TypeError: unhashable type: 'dict'
# print(room_in_set)

print("==================")

# this solution has bug ------  "pankaj" deleted from both room at once
room_in_list = [{"pankaj"  :  "python"},   {"luckey"  :  "python"},  {"pankaj" :  "node"},  {"biraj" :  "node"}]
print(room_in_list)




room_in_list_unique = [{k: v for k, v in d.items() if (k != 'pankaj' )} for d in room_in_list] ## for logging out pankaj out of all room # "sign out done by pankaj"


### trying to delete {"pankaj" : "python"} from list of dictionaries (( using dictionary comprehension inside list comprehension))
# room_in_list_unique = [{k: v for k, v in d.items() if (k != 'pankaj' and v != "python")} for d in room_in_list] 
print(room_in_list_unique)
# print(room_in_list_unique.)

print("========")

# deleting empty dictionary
unique_room_in_list = [val for val in room_in_list_unique if val != {}]
print(unique_room_in_list)


print("===========================================")
print("===========================================")

# this solution has BUG ------ 


# expected output as follows :
# [{}, {'luckey': 'python'}, {}, {'biraj': 'node'}]       
# ========
# [{'luckey': 'python'}, {'biraj': 'node'}]


## actual output

room_in_list = [{"pankaj"  :  "python"},   {"luckey"  :  "python"},  {"pankaj" :  "node"},  {"biraj" :  "node"}]
print(room_in_list)

print("==================")
def new_dict(old_dict):
    print(old_dict, "----")
    n = old_dict.copy()

    # if n["pankaj"] == "node":
    if n.get("pankaj") == "node":
        n.pop('pankaj',None)
        # print(n) # after pop done , dictionary is empty

    # print(n)
    return n

new_list_of_dict = map(new_dict,room_in_list)
print("==================")
print(new_list_of_dict)
print(list(new_list_of_dict))
print("==================")


list_of__new_list_of_dict = list(new_list_of_dict)
print(list_of__new_list_of_dict)
# deleting empty dictionary
unique_room_in_list = [val for val in list_of__new_list_of_dict if val != {}]
print(unique_room_in_list)
print("==================")


unique_room_in_list = [val for val in new_list_of_dict if val == {}]
print(unique_room_in_list)

print("===========================================")




# print('----------')

# print("===========================================")


# print('----------')

# print("===========================================")


# print('----------')

# print("===========================================")


# print('----------')

# print("===========================================")


# print('----------')

# print("===========================================")


# print('----------')

# print("===========================================")


# print('----------')

# print("===========================================")


# print('----------')

# print("===========================================")


# print('----------')
