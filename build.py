"""This module handles the copying of files for deployment."""

import os
import shutil

# Choose source file path
SOURCE_FILE_PATH = 'index.html'

# Choose destination directory path
DEST_DIRECTORY = 'dist'

# Make sure the destination directory exists
os.makedirs(DEST_DIRECTORY, exist_ok=True)

# Choose destination file path
dest_file_path = os.path.join(DEST_DIRECTORY, 'index.html')

# Copy the file
shutil.copyfile(SOURCE_FILE_PATH, dest_file_path)

# Success
print('Success :)!')
