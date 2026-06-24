# File Renamer Tool - Suffix Renamer

A simple desktop application built using **Python** and **Tkinter** to rename multiple files by replacing an old suffix in filenames with a new suffix.

This tool helps users rename files safely by providing a **Preview** option before applying the actual rename operation.

---

##  Project Overview

The **Suffix Renamer Tool** is a lightweight file renaming utility.

It allows users to:
- Select a folder
- Enter an old suffix
- Enter a new suffix
- Preview rename results
- Rename matching files
- Include subfolders if required
- View activity logs after preview or execution

The tool only changes the **file name** and does not modify the file content.

---

## Features

- Easy-to-use desktop GUI
- Folder selection using Browse button
- Replace old suffix with new suffix
- Preview changes before renaming
- Execute actual rename operation
- Option to include subfolders
- Case-sensitive matching option
- Activity log area to show results
- Displays total files, success count, and failure count
- Preserves original file extension

---

##  Application Workflow

  text
Select Folder
     ↓
Enter Old Suffix
     ↓
Enter New Suffix
     ↓
Choose Options
     ↓
Preview Changes
     ↓
Execute Rename
     ↓
View Activity Log

## Technologies Used

Python
Tkinter - GUI development
os module - File handling and renaming
PyInstaller - EXE creation

##Project Structure
File-reanmer-tool/
│
├── suffix_app.py          # Main GUI application file
├── app_logic.py           # Core file renaming logic
├── suffix_renamer.ico     # Application icon
├── README.md              # Project documentation
├── .gitignore             # Ignored files and folders
│
└── screenshots/           # Application screenshots
    ├── initial_screen.png
    ├── preview_screen.png
    └── execution_screen.png

## Main Functionalities

1. Folder Selection
Users can select the folder that contains the files to be renamed.
2. Suffix Update
Users enter:

Old suffix to be replaced
New suffix to be added

3. Preview Mode
Preview mode shows expected rename results without changing any files.
4. Execute Mode
Execute mode performs the actual file rename operation.
5. Activity Log
The log area displays:

Preview results
Renamed file paths
Success count
Failure count
Error messages

## error Handling

The application handles common errors such as:
Folder not selected
Old suffix not entered
No matching files found
File rename failure
Permission issue
File already open or locked

## Future Enhancements

Possible future improvements:
Add undo rename option
Add prefix renaming support
Add file extension filter
Export preview results to CSV or text file
Add progress bar for large folders
Add duplicate filename warning
Add dark mode UI
Add standalone installer


##Final Note
The Suffix Renamer Tool is a simple and useful desktop utility for bulk file renaming.
Always use the Preview option before executing the rename operation.
