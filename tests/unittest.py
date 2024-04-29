import os
import unittest
from build import copy_file

class TestBuildScript(unittest.TestCase):

    def test_copy_file(self):
        # Test copying a file
        source_file = 'index.html'
        dest_directory = 'dist'
        copy_file(source_file, dest_directory)
        
        # Assert that the file was copied successfully
        dest_file = os.path.join(dest_directory, source_file)
        self.assertTrue(os.path.exists(dest_file), f"{source_file} was not copied to {dest_directory}")

        # Clean up: remove the copied file
        os.remove(dest_file)

if __name__ == '__main__':
    unittest.main()
