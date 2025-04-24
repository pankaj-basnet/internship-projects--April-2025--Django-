print("===========================================")


# <!-- ASSINGMENT (5) -->

print("ASSINGMENT (5)")
# Chat Room Tracker
# Track users in chat rooms using dictionary + sets:

#     Add/Remove users

#     List users per room

#     Get common users in two rooms


print('----------')

print("===========================================")
print("===========================================")

# 📌 Chat Room Tracker using Dictionary and Sets

# Dictionary to hold chat rooms and their users
# Key = Room name (str), Value = Set of users in that room
chat_rooms = {}

def add_user(room, user):
    """
    Add a user to a chat room.
    If the room doesn't exist, it will be created.
    """
    # Use setdefault to create room if missing
    chat_rooms.setdefault(room, set()).add(user)
    print(f"✅ {user} added to {room}")

def remove_user(room, user):
    """
    Remove a user from a chat room.
    If room or user doesn't exist, print warning.
    """
    if room in chat_rooms and user in chat_rooms[room]:
        chat_rooms[room].remove(user)
        print(f"🗑️ {user} removed from {room}")
        # Optionally clean up empty room
        if not chat_rooms[room]:
            del chat_rooms[room]
            print(f"🚫 Room {room} deleted (no users left)")
    else:
        print(f"⚠️ {user} not found in {room}")

def list_users(room):
    """
    List all users in a specific room.
    """
    if room in chat_rooms:
        users = chat_rooms[room]
        print(f"👥 Users in {room}: {', '.join(users)}")
    else:
        print(f"🚫 Room '{room}' does not exist")

def common_users(room1, room2):
    """
    Show users who are in both rooms.
    """
    if room1 in chat_rooms and room2 in chat_rooms:
        common = chat_rooms[room1].intersection(chat_rooms[room2])
        if common:
            print(f"🔁 Common users in {room1} and {room2}: {', '.join(common)}")
        else:
            print(f"🚫 No common users between {room1} and {room2}")
    else:
        print(f"⚠️ One or both rooms don't exist")

def display_all_rooms():
    """
    Print all rooms and their users.
    """
    print("\n📊 Current Chat Room State:")
    print("---------------------------")
    print(chat_rooms)
    print("---------------------------")
    for room, users in chat_rooms.items():
        print(f"  {room}: {', '.join(users)}")
    print()

# ✅ Sample Function Calls for Testing
if __name__ == "__main__":
    add_user("python", "alice")
    add_user("python", "bob")
    add_user("java", "alice")
    add_user("java", "dave")
    add_user("html", "carol")

    list_users("python")
    list_users("html")

    common_users("python", "java")
    common_users("python", "html")

    remove_user("html", "carol")
    list_users("html")

    display_all_rooms()
# display_all_rooms()

print("===========================================")
print("===========================================")


print("===========================================")
print("===========================================")



print("===========================================")
print("===========================================")
print(" ------ this solution has BUG ------ an user is removed from all rooms at once --- ")

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
