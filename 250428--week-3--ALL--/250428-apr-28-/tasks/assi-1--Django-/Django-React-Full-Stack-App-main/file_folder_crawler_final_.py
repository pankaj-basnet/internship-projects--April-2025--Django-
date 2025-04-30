from pathlib import Path
import os
import shutil

def list_files_and_folders_recursively(start_path, output_file, skip_folders=None):
    """
    Recursively lists all folders and files starting from 'start_path',
    writes the result to a text file, and skips folders in 'skip_folders' list.
    """
    start_path = Path(start_path)
    skip_folders = set(skip_folders or [])  # Convert to set for faster lookup

    if not start_path.exists():
        print(f"Path does not exist: {start_path}")
        return

    lines = []
    lines.append(f"\nStarting recursive listing from: {start_path.resolve()}\n")

    for current_path, dirnames, filenames in os.walk(start_path):
        current_path_pathlib = Path(current_path)
        folder_name = current_path_pathlib.name

        # Check if this folder (or any parent) should be skipped
        if folder_name in skip_folders:
            print(f"🚫 Skipping folder: {current_path_pathlib}")
            dirnames[:] = []  # Prevent descending into subfolders
            continue

        lines.append(f"\n📁 Folder: {current_path_pathlib.resolve()}")

        # Filter out subfolders that are in skip_folders
        filtered_dirnames = [d for d in dirnames if d not in skip_folders]
        skipped = set(dirnames) - set(filtered_dirnames)
        dirnames[:] = filtered_dirnames  # This modifies walk behavior (avoid going into skipped)

        # Log subfolders
        if dirnames:
            lines.append("  ├─ Subfolders:")
            for dirname in dirnames:
                lines.append(f"    └── {dirname}")
        else:
            lines.append("  ├─ Subfolders: None")

        # Log files
        if filenames:
            lines.append("  └─ Files:")
            for filename in filenames:
                lines.append(f"    └── {filename}")
        else:
            lines.append("  └─ Files: None")

    # Print and write to file
    result_text = "\n".join(lines)
    print(result_text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result_text)
    
    print(f"\n✅ Output written to: {output_file}")

# Example usage
if __name__ == "__main__":
    root_directory = "."  # Replace with your folder path
    output_txt_file = "result_of_all_files_and_folder.txt"
    # skip_these_folders = ['__pycache__', 'node_modules', '.git']  # Add your folders to skip
    skip_these_folders = ['.git', '250416-', '250417--data-structure-', 'venv-0428', 'node_modules']  # Add your folders to skip

    list_files_and_folders_recursively(root_directory, output_txt_file, skip_these_folders)
