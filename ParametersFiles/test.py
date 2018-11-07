"""
Homework 08 test file
"""

import unittest
from file import file_reader
from file import files_scanner

class FileReaderTest(unittest.TestCase):
    def test_file_reader(self):
        p = 'ss.txt'
        with self.assertRaises(StopIteration):
            next(file_reader(p, 3, ' '))

        path = "/Users/minghuijin/Desktop/student.csv"
        file1 = file_reader(path, 3, ' ')
        file2 = file_reader(path, 3, ' ', header = True)

        self.assertTrue(next(file1) == ('Minghui', '1', 'CS'))
        self.assertTrue(next(file1) == ('Yanyan', '2', 'CS'))
        self.assertTrue(next(file1) == ('Jiang', '4', 'EE'))

        self.assertTrue(next(file2) == ('Yanyan', '2', 'CS'))
        self.assertTrue(next(file2) == ('Jiang', '4', 'EE'))

class FilesScannerTest(unittest.TestCase):
    def test_files_scanner(self):
        dir = '/Users/minghuijin/Desktop'
        files = files_scanner(dir)
        self.assertEqual(files[0][0], '/Users/minghuijin/Desktop/0_defs_in_this_file.py')
        self.assertEqual(files[0][1], 0)
        self.assertEqual(files[0][2], 0)
        self.assertEqual(files[0][3], 3)
        self.assertEqual(files[0][4], 57)

        self.assertEqual(files[1][0], '/Users/minghuijin/Desktop/file1.py')
        self.assertEqual(files[1][1], 2)
        self.assertEqual(files[1][2], 4)
        self.assertEqual(files[1][3], 25)
        self.assertEqual(files[1][4], 270)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)