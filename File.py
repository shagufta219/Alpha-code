import os
import shutil

def organize_files(directory):
    # Create a dictionary to store file extensions as keys and their corresponding directories as values
    extension_dirs = {}

    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1][1:]

        # Create a directory for the file extension if it doesn't exist
        if file_ext not in extension_dirs:
            extension_dir = os.path.join(directory, file_ext)
            os.makedirs(extension_dir, exist_ok=True)
            extension_dirs[file_ext] = extension_dir

        # Move the file to its corresponding directory
        shutil.move(os.path.join(directory, filename), os.path.join(extension_dirs[file_ext], filename))

    print(f"Files organized in {directory}!")

# Example usage
organize_files("/path/to/directory")