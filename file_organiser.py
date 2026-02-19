'''
File Organiser Script from Hackr.io Python Tutorial
'''
import os 
import shutil

FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Videos": ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.xlsx', '.doc', '.ppt'],
    "Audio": ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    "Archives": ['.zip', '.rar', '.tar', '.gz', '.7z'],
    "Data": ['.csv', '.json', '.xml', '.sql'],
    "Others": []
}

def organise_files(directory):
    """Organises files in the given directory by their file types.
    """
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return
    
    # Create folders for each category if they don't exist
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move files to their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Check the file extension and move to the appropriate folder
        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break

        # Move to "Others" if no category matched
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))

    print(f"Files in {directory} have been organised successfully.")

# Example usage
directory_to_organise = input("Enter the directory path to organise: ")
organise_files(directory_to_organise)