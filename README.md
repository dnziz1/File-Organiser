# Python File Management Tools
An ongoing collection of practical Python scripts for file organisation. These tools are aimed to help maintain a clean and organised file system through automation.
This began from following a tutorial on [hackr.io](https://hackr.io/blog/how-to-create-a-python-file-organizer) to improve my understanding of python and I will add more tools focused on file management.

## Tools
### 1. File Organiser
Automatically organises files into categorised folders based on their extensions.

**Categories:**
- Images (.jpg, .jpeg, .png, .gif, .bmp, .tiff)
- Videos (.mp4, .avi, .mkv, .mov, .flv)
- Documents (.pdf, .docx, .txt, .xlsx, .pptx, .doc, .ppt)
- Audio (.mp3, .wav, .aac, .flac, .ogg)
- Archives (.zip, .rar, .tar, .gz, .7z)
- Data (.csv, .json, .xml, .sql)
- Others (files with unrecognized extensions)

**Usage**
```
python file_organiser.py
# Then enter the directory path you want to organise
```

### 2. Empty Folder Cleaner
Automatically finds empty folders and deletes them.

**Features:**
- Recursively searches for empty folders
- Shows list before deletion
- Asks for confirmation before removing