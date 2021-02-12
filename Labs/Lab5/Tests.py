from unittest import TestCase, mock
from file_handler import FileHandler, InvalidFileTypeError
from dictionary import Dictionary
from file_handler import  FileExtensions
from os import path


def main():
    pass


if __name__ == '__main__':
    main()


class TestFileHandler(TestCase):

    def test_write_lines_txt(self):
        file = "test_write_lines.txt"
        data = ["firstline", "secondline", "thirdline"]

        FileHandler.write_lines(file, data)
        exists_non_empty = path.exists(file) and path.getsize(file) != 0
        self.assertTrue(exists_non_empty)

    def test_load_data_txt(self):
        ext = ".txt"
        file = "test_write_lines.txt"
        expected_data = ["firstline\n", "secondline\n", "thirdline"]
        actual_data = FileHandler.load_data(file, ext)
        self.assertEquals(expected_data, actual_data)

    def test_load_data_raises_InvalidFileTypeError(self):
        ext = ".unsupported"
        file = "test_write_lines.txt"
        expected_data = ["firstline\n", "secondline\n", "thirdline"]
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data, file, ext)


    def test_load_data_json(self):
        ext = ".txt"
        file = "test_write_lines.txt"
        expected_data = ["firstline\n", "secondline\n", "thirdline"]
        actual_data = FileHandler.load_data(file, ext)
        self.assertEquals(expected_data, actual_data)


class TestDictionary(TestCase):
    def test_load_dictionary(self):
        D = Dictionary()
        D.load_dictionary("data.json")
        self.assertTrue(D.is_loaded())

    def test_query_dictionary(self):
        D = Dictionary()
        D.load_dictionary("data.json")
        definition = D.query_definition()

    def test_query_word(self):
        D = Dictionary()
        D.load_dictionary("data.json")
        definition = D.query_definition('gobble')
        self.assertEquals(definition, ["To eat by swallowing large bits of food with little or no chewing."])

        pass





