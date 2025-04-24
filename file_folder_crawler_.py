# import os
# current_file_path = os.path.abspath(__file__)
# print(current_file_path)


from pathlib import Path
import os
import shutil

def list_files_and_folders_recursively(start_path):
    """
    Recursively prints all files and folders starting from 'start_path'.
    Also prints all contents inside each folder.
    """
    start_path = Path(start_path)  # Ensure it's a Path object

    if not start_path.exists():
        print(f"Path does not exist: {start_path}")
        return

    print(f"\nStarting recursive listing from: {start_path.resolve()}\n")

    for current_path, dirnames, filenames in os.walk(start_path):
        current_path = Path(current_path)
        print(f"\n📁 Folder: {current_path.resolve()}")

        # List subdirectories in the current folder
        if dirnames:
            print("  ├─ Subfolders:")
            for dirname in dirnames:
                print(f"    └── {dirname}")
        else:
            print("  ├─ Subfolders: None")

        # List files in the current folder
        if filenames:
            print("  └─ Files:")
            for filename in filenames:
                print(f"    └── {filename}")
        else:
            print("  └─ Files: None")

# Example usage
if __name__ == "__main__":
    root_directory = "."  # Replace with your desired path, like "C:/Users/YourName/Documents"
    list_files_and_folders_recursively(root_directory)


# write python program to get filenames of all list of files recursively  with all files and folder's name inside each folder as well  and folders inside current filepath of python program  and move files to each folder named same as extension of the files. .py goes to py folder, .txt goes to text directory .