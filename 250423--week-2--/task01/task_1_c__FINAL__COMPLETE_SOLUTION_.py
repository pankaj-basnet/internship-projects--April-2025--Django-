############################################
############################################
# D:\GROW_CTS\PANKAJ-PROJECTS-\250423--week-2--\task01\task_1_c__FINAL__COMPLETE_SOLUTION_.py
# D:\GROW_CTS\PANKAJ-PROJECTS-\250423--week-2--\task01\task_1_d___FINAL__COMPLETE_SOLUTION_.py
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
filepath2 = 'moveit22.txt'  # Placeholder: Not used in final logic
filepath = 'foldercreation/moveit.txt'  # Placeholder: Not used in final logic
destination = 'foldercreation/destination/'
source = './foldercreation'

# Convert destination to Path object for iteration
destination2 = Path(destination)
print(destination2.name)  # prints folder name only

# Create generator to list files/folders in destination
generator_of_path_objects = list(destination2.iterdir())  # convert to list to avoid generator exhaustion
print(type(generator_of_path_objects))

# Just showing the Path.iterdir generator
print(destination2.iterdir())

# Convert source to Path object and show folder name
source2 = Path(source)
print(source2.name)

# Create generator for source directory contents
generator_of_source_objects = list(source2.iterdir())  # convert to list to allow re-use

# Function to move a file based on extension
def move_file_to_destination(type, file_path='foldercreation/moveit33.txt'):
    # Create the expected destination folder path
    type_path = Path(f'{destination}{type}')

    # If folder for extension exists
    if type_path.exists():
        check = False
        for folder in generator_of_path_objects:
            print("--------")
            print(folder)  # print every file/folder in the destination directory
            print("--------")

            # Check if current entry is a directory and its name matches the extension
            if folder.is_dir() and folder.name == f"{type}":
                check = True
                print(check)  # show True when matched

                # Move file to destination subfolder if it exists
                if os.path.exists(file_path):
                    shutil.move(file_path, f'{destination}/{folder.name}')
                    print(f'Successfully moved {type} file to {type} folder')
                else:
                    print("Moving failed: source file doesn't exist")

                print("Moving done/undone")
            else :
                print("is not directory ")
    
    # else:
        # print(" type path doesnot exit")

    # If extension folder doesn't exist, create it and move the file
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

# Main logic to iterate over all items in source folder
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
            print(ext_type)  # print the detected extension

            # Define path string to pass to the move function
            file_path = f'foldercreation/{file_folder.name}'
            print(file_path)

            # List of supported extensions to organize
            extension = ["txt", "py", "md"]

            # Only move if extension is in the predefined list
            for ext in extension:
                if ext_type == ext:
                    move_file_to_destination(type=ext, file_path=file_path)

except Exception as e:
    print(f"Error occurred while creating/moving file: {e}")

print("====================================")
print("=========== End of Program =========")
print("====================================")
