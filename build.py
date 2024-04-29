import os
import shutil

# Choose source file path
source_file_path = 'index.html'

# Choose destination directory path
dest_directory = 'dist'

# Make sure the destination directory exists
os.makedirs(dest_directory, exist_ok=True)

# Choose destination file path
dest_file_path = os.path.join(dest_directory, 'index.html')

# Copy the file
shutil.copyfile(source_file_path, dest_file_path)

# Success
print('Success :)!')
