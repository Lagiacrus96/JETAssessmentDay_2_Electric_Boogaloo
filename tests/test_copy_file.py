import os
from unittest import mock
import pytest
from build import copy_file

def test_copy_file(tmpdir):
    # Prepare a temporary source file and destination directory
    source_file = tmpdir.join('source.html')
    source_file.write('<h1>Hello, World!</h1>')
    source = str(source_file)
    
    destination = str(tmpdir.mkdir('dest'))
    file_name = 'index.html'

    # Mock the print to avoid cluttering test output
    with mock.patch('builtins.print') as mocked_print:
        copy_file(source, destination, file_name)
    
    # Assert file was copied correctly
    dest_file_path = os.path.join(destination, file_name)
    assert os.path.exists(dest_file_path), "The file should have been copied to the destination."
    
    # Assert the contents are the same
    with open(dest_file_path, 'r') as file:
        contents = file.read()
    assert contents == '<h1>Hello, World!</h1>', "The contents of the destination file should match the source file."
    
    # Assert that 'Success :)' was printed
    mocked_print.assert_called_with('Success :)!')

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])
    
