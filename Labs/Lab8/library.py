""" This module houses the library"""
from Labs.Lab8 import item
from Labs.Lab8.catalogue import Catalogue
import difflib

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
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all Items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            #handle user pressing only enter in menu
            if(string_input == ''):
                continue

            user_input = int(string_input)

            if user_input == 1:
                self._catalogue.display_available_items()
               # self.display_available_books()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self._catalogue.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self._catalogue.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self._catalogue.find_item(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item to remove")
                self._catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")




def generate_test_books():
    """
    Return a set of books with dummy data.
    :return: a set
    """
    book_list = {
        item.Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        item.Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        item.Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        item.Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss"),
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
