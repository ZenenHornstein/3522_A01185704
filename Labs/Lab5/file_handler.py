import enum
import pathlib
import json
import abc


class FileHandler:
    """
    Utility class for reading and writing to a variety of files supported by
    """

    def __init__(self):
        pass

    @staticmethod
    def write_lines(path, lines):
        """
        Write lines to a text file located at filepath.
        The file will be created if it does not exist, otherwise appended too.


        :param path: the filepath of the text file
        :param lines: lines to write as a list.
        :return: None
        """
        with open(path, mode="a", encoding="utf-8") as outfile:
            for line in lines:
                outfile.write("\n" + line)

    @staticmethod
    def load_data(path, file_extension):
        """
        Loads a datafile based on its file Extension. Supported File extensions
        are described by FileExtension Enum.

        :param path: the filepath to the datafile as a str
        :param file_extension: an instance of FileExtensions
        :raises InvalidFileTypeError
        :return: the data
        """
        try:
            with open(path, mode="r+", encoding="utf-8") as infile:
                if file_extension == FileExtensions.JSON.value:
                    in_data = json.load(infile)
                elif file_extension == FileExtensions.TXT.value:
                    in_data = infile.readlines()
                else:
                    raise InvalidFileTypeError("We dont support that filetype!")
        except FileNotFoundError:
            print(f"Unable to find {path}")
        else:
            return in_data
        finally:
            infile.close()


class InvalidFileTypeError(Exception):
    """
    The exception to be raised if a extension not supported by File extensions is requested.
    """
    def __init__(self, my_msg):
        super().__init__(my_msg)


class FileExtensions(enum.Enum):
    """
    The types of extensions supported by FileHandler
    """
    TXT = ".txt"
    JSON = ".json"
