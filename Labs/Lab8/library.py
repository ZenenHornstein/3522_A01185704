""" This module houses the library"""
from Labs.Lab8 import item
from Labs.Lab8.catalogue import Catalogue
import difflib
import sys


class Library:
    """
    The Library consists of a list of books and provides an
    interface for users to check out, return and find books.
    """

    def __init__(self, catalogue: Catalogue):
        """
        Intialize the library with a list of books.
        :param book_list: a sequence of book objects.
        """
        self._catalogue = catalogue

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of books, check out, return, find, add, remove a book.
        """

        function_lookup = {"1": self._catalogue.display_available_items,
                           "2": self._catalogue.check_out,
                           "3": self._catalogue.return_item,
                           "4": self._catalogue.find_item,
                           "5": self._catalogue.add_item,
                           "6": self._catalogue.remove_item,

                           }
        user_input = None
        while True:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all Items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")

            user_input = input("Please enter your choice")
            while user_input not in ("1", "2", "3", "4", "5", "6", "7"):
                user_input = input("Please enter a valid choice")

            if user_input == "7":
                print("Thanks for visiting!")
                sys.exit(0)

            function_lookup.get(user_input)()


def generate_test_books():
    """
    Return a set of books with dummy data.
    :return: a set
    """
    book_list = {
        item.Book("100.200.300", "Harry Potter 1", num_copies=2, author="J K Rowling"),
        item.Book("999.224.854", "Harry Potter 2", num_copies=5, author="J K Rowling"),
        item.Book("631.495.302", "Harry Potter 3", num_copies=4, author="J K Rowling"),
        item.Book("123.02.204", "The Cat in the Hat", num_copies=1, author="Dr. Seuss"),
    }

    return book_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    book_list = generate_test_books()
    my_epic_catalogue = Catalogue(book_list)
    my_epic_library = Library(my_epic_catalogue)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
