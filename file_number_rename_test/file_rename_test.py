import unittest
import os
import shutil
import sys
from file_number_rename.file_rename import rename_files, rename_file_name, parse_arguments


class NumberRenameTestCase(unittest.TestCase):

    def setUp(self):
        self.clean_up_test_dir()

    file_name = "_test_file.txt"

    def touch(self, file_path, times=None):
        with open(file_path, 'a'):
            os.utime(file_path, times)

    def prepare_test_dir(self):
        test_dir = os.path.join(os.path.dirname(__file__), "test")
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)
        for index in range(5,10):

            file_path = os.path.join(test_dir, str(index) + self.file_name)
            self.touch(file_path)

        return test_dir

    def clean_up_test_dir(self):
        test_dir = os.path.join(os.path.dirname(__file__), "test")
        if os.path.isdir(test_dir):
            shutil.rmtree(test_dir)

    def test_rename_file_name(self):
        self.assertEqual("01_my_file_name", rename_file_name('23_my_file_name', 1, padding=2))
        self.assertEqual("02_my_file_name", rename_file_name('23_my_file_name', 2, padding=2))
        self.assertEqual("10_my_file_name", rename_file_name('23_my_file_name', 10, padding=2))
        self.assertEqual("123_my_file_name", rename_file_name('23_my_file_name', 123, padding=2))

    def test_rename_file_name_ignore_non_number_file(self):
        self.assertEqual("my_file_name", rename_file_name('my_file_name', 1, padding=2))

    def test_rename_file_different_separators(self):
        self.assertEqual("01.my.file.name", rename_file_name('23.my.file.name', 1, padding=2))
        self.assertEqual("01.my_file.name", rename_file_name('23.my_file.name', 1, padding=2))

    def test_rename_file_name_different_beginning(self):
        self.assertEqual("01_my_file_name", rename_file_name('123_my_file_name', 1, padding=2))

    def test_rename_file_name_different_padding(self):
        self.assertEqual("0001_my_file_name", rename_file_name('123_my_file_name', 1, padding=4))

    def test_rename_files(self):
        test_dir = self.prepare_test_dir()

        after_renaming_list = []
        after_renaming_list.append("01" + self.file_name)
        after_renaming_list.append("02" + self.file_name)
        after_renaming_list.append("03" + self.file_name)
        after_renaming_list.append("04" + self.file_name)
        after_renaming_list.append("05" + self.file_name)

        rename_files(test_dir, 1, padding=2)
        sorted_directory = os.listdir(test_dir)
        sorted_directory.sort()
        self.assertListEqual(after_renaming_list, sorted_directory)

        self.clean_up_test_dir()

    def test_rename_files_different_start(self):
        test_dir = self.prepare_test_dir()

        after_renaming_list = []
        after_renaming_list.append("09" + self.file_name)
        after_renaming_list.append("10" + self.file_name)
        after_renaming_list.append("11" + self.file_name)
        after_renaming_list.append("12" + self.file_name)
        after_renaming_list.append("13" + self.file_name)

        rename_files(test_dir, 9, padding=2)
        sorted_directory = os.listdir(test_dir)
        sorted_directory.sort()
        self.assertListEqual(after_renaming_list, sorted_directory)

        self.clean_up_test_dir()

#    def test_parse_arguments(self):
#        sys.argv.append("--start")
#        sys.argv.append("10")
#        args = parse_arguments()
#        self.assertEqual(args.start, 10)


if __name__ == '__main__':
    unittest.main()

