# File Organizer Script

This Python script helps you organize files in a specified folder based on their file types. It categorizes files into different directories according to their extensions, making it easier to manage and find files.

## Features

- **Automatic File Categorization**: Organizes files into predefined categories such as Images, Text Files, Executable Files, Audio Files, Video Files, Spreadsheets, Presentations, Database Files, Web Files, and System Files.
- **Custom Directory Structure**: Creates a nested directory structure based on the file type and specific file name.
- **File Handling**: Moves files to their corresponding directories based on their extensions.

## Supported File Types

The script categorizes files into the following types:

- **Images**: Includes formats like JPEG, PNG, GIF, TIFF, and more.
- **Text Files**: Includes formats like DOC, PDF, TXT, and more.
- **Executable Files**: Includes formats like EXE, APK, PY, and more.
- **Audio Files**: Includes formats like MP3, WAV, MIDI, and more.
- **Video Files**: Includes formats like MP4, AVI, MKV, and more.
- **Spreadsheets**: Includes formats like XLS, XLSX, ODS, and more.
- **Presentations**: Includes formats like PPT, PPTX, KEY, and more.
- **Database Files**: Includes formats like CSV, SQL, MDB, and more.
- **Web Files**: Includes formats like HTML, CSS, JS, PHP, and more.
- **System Files**: Includes formats like DLL, SYS, CFG, and more.

## How It Works

1. **Scan Folder**: The script scans the specified folder for files.
2. **Identify File Type**: It identifies the file type by its extension.
3. **Create Directories**: If not already present, it creates a directory structure for the file type and specific file name.
4. **Move Files**: Files are then moved to their corresponding directories.

## Prerequisites

- Python 3.x
- `os` and `shutil` libraries (These are part of the Python Standard Library, so no additional installations are required).

## Usage

1. Clone or download the script to your local machine.
2. Set the `folder_path` variable in the script to the path of the folder you want to organize.
3. Run the script:

    ```bash
    python fileManagementSystem.py
    ```

4. The script will automatically organize the files in the specified folder.

## Example

If you have the following files in your `Downloads` folder:

- `example.jpg`
- `document.pdf`
- `script.py`

After running the script, the folder structure will be:

```
Downloads/
├── Images/
│   └── JPEG Image(jpg)/
│       └── example.jpg
├── Text Files/
│   └── Portable Document Format(pdf)/
│       └── document.pdf
├── Executable Files/
│   └── Python Script(py)/
│       └── script.py
```
