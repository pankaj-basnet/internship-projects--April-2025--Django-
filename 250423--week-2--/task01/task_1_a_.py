

############################################
# - (1) Write a mini file organizer that moves files by extension.
############################################
import shutil

import logging

# move file to a destination folder
try:

    filepath = 'foldercreation/moveit.txt'
    destination = 'foldercreation/destination'

    print("====================================")
    print("=========     OUTPUT    =========")
    print("====================================")
    print(f"moving from {filepath} to {destination}")
    # move_command = shutil.move(filepath, destination) # shutil.Error: Destination path 'foldercreation/destination\moveit.txt' already exists
    move_command = shutil.move(filepath, destination)
    print("====================================")
    print("done.")
    print("====================================")
except shutil.Error as e:
    print(f"Error while moving : {e}")
except Exception as e:
    print(f"catching all exceptions: {e}")
else:
    print("exception did not happen.")


print("====================================")
# print("done.") # else in try/ except
print("====================================")

    # ====================================
    # =========     OUTPUT    =========
    # ====================================
    # moving from foldercreation/moveit.txt to foldercreation/destination
    # ====================================
    # done.
    # ====================================
    # exception did not happen.
    # ====================================


    # ====================================
    # =========     OUTPUT    =========
    # ====================================
    # moving from foldercreation/moveit.txt to foldercreation/destination
    # Error while moving : Destination path 'foldercreation/destination\moveit.txt' already exists
    # ====================================

print("====================================")



print("====================================")
print("====================================")

# print("====================================")

# print("====================================")

# print("====================================")

# print("====================================")

# print("====================================")