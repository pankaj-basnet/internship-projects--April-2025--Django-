

############ ADVANCED


############################################
# - (1) Mini file organizer that moves files by extension.
############################################

print("=======   task_1_b    =========")
print("================================")

from pathlib import Path
import os
import shutil

# Base path setup
filepath2 = 'moveit22.txt'  # not used in logic but retained for consistency
filepath = 'foldercreation/moveit.txt'  # not used but retained
destination = 'foldercreation/destination/'
source = './foldercreation'

# Convert to Path objects for filesystem operations
destination2 = Path(destination)
source2 = Path(source)

print(f"Destination folder name: {destination2.name}")
print(f"Source folder name: {source2.name}")

# Convert generators to list for reusability (generators are single-use)
generator_of_path_objects = list(destination2.iterdir())
generator_of_source_objects = list(source2.iterdir())

print(f"Destination contents: {[str(p) for p in generator_of_path_objects]}")
print(f"Source contents: {[str(p) for p in generator_of_source_objects]}")


def move_file_to_destination(type: str, file_path: str = 'foldercreation/moveit33.txt') -> None:
    """
    Moves the file at file_path to a subfolder named after its extension (type).
    If the subfolder doesn't exist, it's created.
    """
    type_path = Path(f'{destination}{type}')  # full path to the type-based folder

    # Create the folder if it doesn't exist
    if not type_path.exists():
        print(f"Folder '{type}' not found. Creating...")
        type_path.mkdir(parents=True, exist_ok=True)

    # Double-check that it's really a directory
    if type_path.is_dir():
        dest_file_path = type_path / Path(file_path).name

        if Path(file_path).exists():
            shutil.move(file_path, dest_file_path)
            print(f"✅ Successfully moved '{file_path}' to '{dest_file_path}'")
        else:
            print(f"❌ Move failed: source file '{file_path}' does not exist")
    else:
        print(f"❌ '{type_path}' is not a directory")


try:
    # Loop over all items in the source folder
    for file_folder in generator_of_source_objects:
        print("===============")
        print(f"Inspecting: {file_folder}")
        print("===============")

        ext_type = "default_ext_type"

        # Only act if it's a file
        if file_folder.is_file():
            # Split the filename by '.' to get extension
            parts = file_folder.name.split(".")
            ext_type = parts[-1] if len(parts) > 1 else "no_ext"
            print(f"Detected file extension: {ext_type}")

            # Build full file path to pass to move function
            file_path = f'foldercreation/{file_folder.name}'
            print(f"Constructed file path: {file_path}")

            # Only consider known extensions
            extension = ["txt", "py", "md"]
            if ext_type in extension:
                move_file_to_destination(type=ext_type, file_path=file_path)
            else:
                print(f"Extension '{ext_type}' not in supported list {extension}")

except Exception as e:
    print(f"⚠️ Error occurred during file move operation: {e}")

print("====================================")
print("=========== End of Program =========")
print("====================================")








# #################################################################
# #################################################################
# #################################################################
# ############################################
# # - (1) Mini file organizer that moves files by extension.
# ############################################

# # This script moves files from a source directory into separate folders based on their file extensions.

# print("=======   task_1_b    =========")
# print("================================")

# from pathlib import Path
# import os
# import shutil

# # Define paths
# filepath2 = 'moveit22.txt'  # Placeholder: Not used in final logic
# filepath = 'foldercreation/moveit.txt'  # Placeholder: Not used in final logic
# destination = 'foldercreation/destination/'
# source = './foldercreation'

# # Convert destination to Path object for iteration
# destination2 = Path(destination)
# print(destination2.name)  # prints folder name only

# # Create generator to list files/folders in destination
# generator_of_path_objects = list(destination2.iterdir())  # convert to list to avoid generator exhaustion
# print(type(generator_of_path_objects))

# # Just showing the Path.iterdir generator
# print(destination2.iterdir())

# # Convert source to Path object and show folder name
# source2 = Path(source)
# print(source2.name)

# # Create generator for source directory contents
# generator_of_source_objects = list(source2.iterdir())  # convert to list to allow re-use

# # Function to move a file based on extension
# def move_file_to_destination(type, file_path='foldercreation/moveit33.txt'):
#     # Create the expected destination folder path
#     type_path = Path(f'{destination}{type}')

#     # If folder for extension exists
#     if type_path.exists():
#         check = False
#         for folder in generator_of_path_objects:
#             print("--------")
#             print(folder)  # print every file/folder in the destination directory
#             print("--------")

#             # Check if current entry is a directory and its name matches the extension
#             if folder.is_dir() and folder.name == f"{type}":
#                 check = True
#                 print(check)  # show True when matched

#                 # Move file to destination subfolder if it exists
#                 if os.path.exists(file_path):
#                     shutil.move(file_path, f'{destination}/{folder.name}')
#                     print(f'Successfully moved {type} file to {type} folder')
#                 else:
#                     print("Moving failed: source file doesn't exist")

#                 print("Moving done/undone")

#     # If extension folder doesn't exist, create it and move the file
#     else:
#         try:
#             type_path.mkdir(parents=True, exist_ok=True)
#             if os.path.exists(file_path):
#                 shutil.move(file_path, f'{destination}/{type}/{Path(file_path).name}')
#                 print(f'Successfully created {type} folder and moved file')
#             else:
#                 print("Moving failed: source file doesn't exist")
#         except Exception as e:
#             print(f"Error while creating/moving to new extension folder: {e}")

# # Main logic to iterate over all items in source folder
# try:
#     for file_folder in generator_of_source_objects:
#         print("===============")
#         print(file_folder)  # print each file/folder from source
#         print("===============")

#         ext_type = "default_ext_type"

#         # Check if current entry is a file
#         if file_folder.is_file():
#             # Extract extension from file name
#             list_of_str = file_folder.name.split(".")
#             ext_type = list_of_str[-1] if len(list_of_str) > 1 else "no_ext"
#             print(ext_type)  # print the detected extension

#             # Define path string to pass to the move function
#             file_path = f'foldercreation/{file_folder.name}'
#             print(file_path)

#             # List of supported extensions to organize
#             extension = ["txt", "py", "md"]

#             # Only move if extension is in the predefined list
#             for ext in extension:
#                 if ext_type == ext:
#                     move_file_to_destination(type=ext, file_path=file_path)

# except Exception as e:
#     print(f"Error occurred while creating/moving file: {e}")

# print("====================================")
# print("=========== End of Program =========")
# print("====================================")

# # ✅ Fixes and Enhancements:
# # Converted generators to lists so they aren't exhausted after the first use.

# # Ensured move_file_to_destination() creates missing folders if not already present.

# # Made sure only files with matching extensions are moved.

# #################################################################
# #################################################################
# #################################################################