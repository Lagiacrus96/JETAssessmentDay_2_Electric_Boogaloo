import os
import shutil
import pytest

def copy_file(source, destination):
    os.makedirs(destination, exist_ok=True)
    dest_file_path = os.path.join(destination, os.path.basename(source))
    shutil.copyfile(source, dest_file_path)
    return dest_file_path

def test_copy_file(tmpdir):
    # Create a temporary source file
    source_file = tmpdir.join('source.html')
    source_file.write('<h1>Hello, World!</h1>')

    # Define source and destination
    source = str(source_file)
    destination = str(tmpdir.mkdir('dest'))

    # Copy the file
    copied_file = copy_file(source, destination)

    # Check that the copied file exists
    assert os.path.exists(copied_file), "The file should exist in the destination directory."

    # Check that the contents are the same
    with open(copied_file, 'r') as file:
        contents = file.read()
    assert contents == '<h1>Hello, World!</h1>', "The contents of the destination file should match the source file."

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])
