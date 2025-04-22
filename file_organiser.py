# Import necessary modules
import logging  # Used for logging information/errors
import os  # For interacting with the operating system
import shutil  # For moving files
import sys  # For exiting the script if the directory is invalid

# Configure logging: Store logs in 'files.log' file
logging.basicConfig(
    filename="files.log",  # Log file name
    level=logging.INFO,  # Logging level (INFO)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format (timestamp, level, message)
)
logging.info("File Organizer Started")  # Log when the script starts

# Define categories and associated file extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".tar"],
    "Executables": [".exe", ".sh", ".bat"]
}

# Function to determine the category of a file
def get_category(file_name):
    
    # Extracts the file extension and matches it with predefined categories.
    # Returns the category name or 'Others' if no match is found.
   
    # _ stores the filename (example.pdf), which we don’t need.
    # ext stores the extension (.pdf), which we need.
    
    _, ext = os.path.splitext(file_name)  # Get file extension (ignores the file name)
    logging.info(f"File extension for '{file_name}' is '{ext}'")  # Log extension
    
    # Check if extension matches any category
    for category, extensions in FILE_CATEGORIES.items():
        if ext.lower() in extensions:  # Convert extension to lowercase for case insensitivity
            logging.info(f"File '{file_name}' categorized as '{category}'")
            return category  # Return the matched category
    
    logging.info(f"File '{file_name}' categorized as 'Others'")
    return "Others"  # If no category is found, assign it to 'Others'

# Function to organize files into categorized folders
def organize_files(directory):
    
    # Organizes files in the given directory by moving them into categorized subfolders.
   
    if not os.path.exists(directory):  # Check if the directory exists
        print("Directory not found.")  # Print error message
        logging.error("Directory not found")  # Log error
        return  # Exit function

    # Loop through all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)  # Get full file path

        if os.path.isdir(file_path):  # Skip directories (only process files)
            continue

        category = get_category(file_name)  # Determine category
        category_path = os.path.join(directory, category)  # Create path for category folder
        
        # If the category folder doesn't exist, create it
        if not os.path.exists(category_path):
            os.mkdir(category_path)  # Create folder

        # Move the file to its respective category folder
        new_path = os.path.join(category_path, file_name)
        shutil.move(file_path, new_path)  # Move file
        logging.info(f"Moved {file_name} to {category_path}")  # Log movement
        print(f"Moved: {file_name} → {category}")  # Print movement message

# Function to clear the screen (for better UI)
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # Windows → 'cls', macOS/Linux → 'clear'

# Main function to execute the program
def main():
    
    # Main function that takes user input for directory path and calls organize_files().
   
    clear_screen()  # Clear the screen
    print("📂 Welcome to File Organizer 📂\n")  # Print welcome message

    directory = input("Enter the folder path to organize: ")  # Get folder path from user

    if not os.path.exists(directory):  # Validate folder path
        print("Invalid directory path.")  # Print error
        sys.exit(1)  # Exit with error code 1

    organize_files(directory)  # Call function to organize files
    print("\n✅ File organization completed!")  # Print success message

# Run the script if executed directly
if __name__ == "__main__":
    main()