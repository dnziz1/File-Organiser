'''
Empty Folder Cleaner - A Python script to clean up empty folders in a specified directory.
'''
import os

def find_empty_folders(directory):
    empty_folders = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        # Check if the folder is empty (no files and no subfolders)
        if not dirs and not files:
            empty_folders.append(root)

    return empty_folders

# Get the directory path from the user
folder = input("Enter the directory path to clean up empty folders: ")

# Find empty folders
empty_folders = find_empty_folders(folder)

if empty_folders:
    print(f"\nEmpty folders found in '{folder}':")
    for i, folder_path in enumerate(empty_folders, 1):
        print(f"{i}. {folder_path}")

    # Ask the user if they want to delete the empty folders
    confirm = input("\nDo you want to delete these empty folders? (yes/no): ")
    if confirm.lower() == 'yes':
        for folder_path in empty_folders:
            os.rmdir(folder_path)
            print(f"Deleted: {folder_path}")

else:
    print(f"No empty folders found in '{folder}'.")