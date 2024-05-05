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
    source_file_path = 'index.html'
    dest_directory = 'dist'
    file_name = 'index.html'

    copy_file(source_file_path, dest_directory, file_name)

if __name__ == "__main__":
    main()
