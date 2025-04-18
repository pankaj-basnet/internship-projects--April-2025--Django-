print("===========================================")


# <!-- ASSINGMENT (5) -->

print("ASSINGMENT (5)")
# Chat Room Tracker
# Track users in chat rooms using dictionary + sets:

#     Add/Remove users

#     List users per room

#     Get common users in two rooms


print('----------')

users = [ "pankaj", "luckey", "biraj","biraj"]
rooms = [ "python", "node", "data",  "data"]
print(users)
print(rooms)

{"python" : ("luckey", "pankaj")}
print('----------')

users_in_room_init  = zip(users, rooms)
print(users_in_room_init)

unique_users_in_room = set()

for iii in users_in_room_init:
    unique_users_in_room.add(iii)

print(unique_users_in_room)

print('----------')

print(users)

### remove "biraj" of first occurence
users.remove("biraj")
print(users)

print('---------------------')


room = {  "pankaj" : "python",   "luckey" : "python",  "pankaj": "node",  "biraj": "node"} 
print(room)

### add "aayush" to rooms
room ["aayush"] = "data" 

room ["aayush"] = "mern" 
print(room)

### remove "aayush" from room
del room["aayush"] # "aayush" removed or deleted
print(room)

print("===========================================")

room_in_list = [{"pankaj"  :  "python"},   {"luckey"  :  "python"},  {"pankaj" :  "node"},  {"biraj" :  "node"}]
print(room_in_list)

room_in_list_unique = [{k: v for k, v in d.items() if (k != 'pankaj' )} for d in room_in_list]

print(room_in_list_unique)

print("========")

# deleting empty dictionary
unique_room_in_list = [val for val in room_in_list_unique if val != {}]
print(unique_room_in_list)


print(" ------ this solution has BUG ------ an user is removed from all rooms at once --- ")
print("===========================================")
print("===========================================")
