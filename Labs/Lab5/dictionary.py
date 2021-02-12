"""
This module contains the dictionary class along with all driver methods.
"""
import os
from file_handler import FileHandler
from file_handler import InvalidFileTypeError


class Dictionary:
    """
    A dictionary contains words as keys and definitions lists as values..
    """

    def __init__(self):
        """
        Create an instance of Dictionary Object.
        """

        self._data = None

    def is_loaded(self):
        """
        Check to see wether this dictionary has been loaded or not.
        :return: true if loaded false otherwise.
        """
        return len(self._data) != 0

    @property
    def data(self):
        """
        The data of the Dictionary

        :return data: the data of the Dictionary, as a dict
        """
        return self._data

    @data.setter
    def data(self, new_data):
        """
        The setter for the dictionary Data

        :param new_data: the new data to be set
        :return: None
        """
        self._data = new_data

    def query_definition(self, word):
        """
        Searches in a case insensitive manner, for word inside of the loaded data.

        :param word: word as a string.
        :return: A list of definitions
        """
        results = self.data[word.lower()] if word.lower() in self.data.keys() else None
        if not results:
            print("Unable to find a definition of that word")
            return "No definition found."
        print("")
        for index, definition in enumerate(results):
            print(f"\t{index}. {definition}")
        print("")
        return results

    def load_dictionary(self, filepath):
        """
        Load data into this dictionary.

        :param filepath: the path of the data as a string
        :return: None
        """
        filename, file_extension = os.path.splitext(filepath)
        filename.strip()
        file_extension.strip()
        try:
            self.data = FileHandler.load_data(filepath, file_extension)
        except InvalidFileTypeError:
            print("That is not one of the supported formats!")

    def main_input_loop(self):
        """
        Drives the program.

        Repeatedly prompt the user to query definitions from a loaded dictionary.
        :return:
        """
        words_searched = {}
        print(25 * "*" + "Welcome to my dictionary Program!" + 25 * "*")
        while True:
            user_input = input("Please type:\n\tA word to query \n\tor 'exitprogram' to quit ")
            if user_input == "exitprogram":
                with open("user_queries.txt", 'w', encoding='utf-8') as outfile:
                    for word in words_searched:
                        outfile.write(f"\n{word}:")
                        for definitions in words_searched[word]:
                            outfile.write(f"\n\t{definitions}")
                print("Goodbye!")
                exit(0)
            else:
                definitions = self.query_definition(user_input)
                words_searched[user_input] = definitions


def main():
    d = Dictionary()
    d.load_dictionary(filepath="data.json")
    d.main_input_loop()


if __name__ == '__main__':
    main()
