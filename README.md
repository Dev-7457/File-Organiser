📁 File Organizer
A simple Python script that organizes files in a given directory into categorized subfolders based on file extensions. Makes your messy folders neat and tidy in seconds!

🚀 Features
Automatically categorizes files into:

Documents

Images

Music

Videos

Archives

Executables

Others

Uses logging to track activities in files.log

Skips folders and processes only files

Cross-platform compatible (Windows, Linux, macOS)

📂 Categories Handled

Category	File Extensions
Documents	.pdf, .docx, .txt, .xlsx
Images	.jpg, .jpeg, .png, .gif
Music	.mp3, .wav, .aac
Videos	.mp4, .mkv, .mov
Archives	.zip, .rar, .tar
Executables	.exe, .sh, .bat
Others	Any file types not matching the above
🛠️ Requirements
Python 3.x

No external packages required — uses built-in Python modules (os, shutil, logging, sys)

🧠 How It Works
You enter a folder path.

The script reads all files (ignores folders).

Based on the file extension, each file is moved into a categorized subfolder.

All actions are logged in files.log.


📜 Sample Output

📂 Welcome to File Organizer 📂

Enter the folder path to organize: /Users/you/Downloads

Moved: invoice.pdf → Documents
Moved: photo.png → Images
Moved: song.mp3 → Music
Moved: archive.zip → Archives

✅ File organization completed!
🐞 Logging
All logs are saved in a files.log file with timestamps, actions performed, and any errors encountered.
