############################################
############################################
############################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250423--week-2--\task01\task_1_e__SEND_FOR_REPORT_.py
############################################
# __FINAL__COMPLETE_SOLUTION_.py
############################################
############################################
############################################





############################################
# - (1) Mini file organizer that moves files by extension.
############################################

# This script moves files from a source directory into separate folders based on their file extensions.

print("=======   task_1_b    =========")
print("================================")

from pathlib import Path
import os
import shutil

# Define paths
filepath2 = 'moveit22.txt' 
filepath = 'foldercreation/moveit.txt' 
destination = 'foldercreation/destination/'
source = './foldercreation'

# Convert destination to Path object for iteration
destination2 = Path(destination)
print(destination2.name) 

# Create generator to list files/folders in destination
generator_of_path_objects = list(destination2.iterdir()) 
print(type(generator_of_path_objects))

# Just showing the Path.iterdir generator
print(destination2.iterdir())

# Convert source to Path object and show folder name
source2 = Path(source)
print(source2.name)

#
generator_of_source_objects = list(source2.iterdir())  


def move_file_to_destination(type, file_path='foldercreation/moveit33.txt'):
    
    type_path = Path(f'{destination}{type}')

    
    if type_path.exists():
        check = False
        for folder in generator_of_path_objects:
            print("--------")
            print(folder)  
            print("--------")

            
            if folder.is_dir() and folder.name == f"{type}":
                check = True
                print(check)  

                
                if os.path.exists(file_path):
                    shutil.move(file_path, f'{destination}/{folder.name}')
                    print(f'Successfully moved {type} file to {type} folder')
                else:
                    print("Moving failed: source file doesn't exist")

                print("Moving done/undone")

    
    else:
        try:
            type_path.mkdir(parents=True, exist_ok=True)
            if os.path.exists(file_path):
                shutil.move(file_path, f'{destination}/{type}/{Path(file_path).name}')
                print(f'Successfully created {type} folder and moved file')
            else:
                print("Moving failed: source file doesn't exist")
        except Exception as e:
            print(f"Error while creating/moving to new extension folder: {e}")


try:
    for file_folder in generator_of_source_objects:
        print("===============")
        print(file_folder)  # print each file/folder from source
        print("===============")

        ext_type = "default_ext_type"

        # Check if current entry is a file
        if file_folder.is_file():
            # Extract extension from file name
            list_of_str = file_folder.name.split(".")
            ext_type = list_of_str[-1] if len(list_of_str) > 1 else "no_ext"
            print(ext_type) 

           
            file_path = f'foldercreation/{file_folder.name}'
            print(file_path)

           
            extension = ["txt", "py", "md"]

           
            for ext in extension:
                if ext_type == ext:
                    move_file_to_destination(type=ext, file_path=file_path)

except Exception as e:
    print(f"Error occurred while creating/moving file: {e}")

print("====================================")
print("=========== End of Program =========")
print("====================================")

# ✅ Fixes and Enhancements:
# Converted generators to lists so they aren't exhausted after the first use.

# Ensured move_file_to_destination() creates missing folders if not already present.

# Made sure only files with matching extensions are moved.
