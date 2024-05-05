"""This module handles the copying of files for deployment."""

import os
import shutil

def copy_file(source_path, destination_dir, file_name):
    """Copies a file from source_path to destination_dir."""
    # Make sure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # Full path for the destination file
    dest_file_path = os.path.join(destination_dir, file_name)
    
    # Copy the file
    shutil.copyfile(source_path, dest_file_path)
    
    # Success
    print('Success :)!')

def main():
    SOURCE_FILE_PATH = 'index.html'
    DEST_DIRECTORY = 'dist'
    FILE_NAME = 'index.html'

    copy_file(SOURCE_FILE_PATH, DEST_DIRECTORY, FILE_NAME)

if __name__ == "__main__":
    main()
