import difflib
from Labs.Lab8.library_item_generator import LibraryItemGenerator
from Labs.Lab8 import item


class Catalogue:
    """
    Represents a catalogue that stores item of type Items.
    """

    def __init__(self, item_list):
        """
        Intialize the catalogue with a list of items.
        :param item_list: a sequence of objects which subclass item.
        """
        self._item_list = item_list

    def add_item(self):
        item_to_add = LibraryItemGenerator.generate_item(classes=[item.Book, item.Journal, item.DVD])
        self._item_list.append(item_to_add)

    @property
    def item_list(self):
        """
        The  item list of the Catalogue

        :return : the item list of the Catalogue, as a list
        """
        return self._item_list

    @item_list.setter
    def item_list(self, new_item_list):
        """
        Set the item list of the Catalogue

        :param new_item_list: the new item list of the Catalogue
        :precondition :
        """
        self._item_list = new_item_list

    def _retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an book with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        found_book = None
        for library_book in self._item_list:
            if library_book.call_number == call_number:
                found_book = library_book
                break
        return found_book

    def find_item(self, title):
        """
        Find books with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_book in self._item_list:
            title_list.append(library_book.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def remove_item(self, call_number):
        """
        Remove an existing book from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_book = self._retrieve_item_by_call_number(call_number)
        if found_book:
            self._item_list.remove(found_book)
            print(f"Successfully removed {found_book.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")

    def display_available_items(self):
        """
        Display all the books in the library.
        """
        print("Books List")
        print("--------------", end="\n\n")
        for library_book in self._item_list:
            print(library_book)

    def reduce_item_count(self, call_number):
        """
        Decrement the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_book = self._retrieve_item_by_call_number(call_number)
        if library_book:
            library_book.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_number):
        """
        Increment the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_book = self._retrieve_item_by_call_number(call_number)
        if library_book:
            library_book.increment_number_of_copies()
            return True
        else:
            return False

    def check_out(self, call_number):
        """
        Check out an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_book = self._retrieve_item_by_call_number(call_number)
        if library_book.check_availability():
            status = self.reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find book with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_item_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find book with call number {call_number}"
                  f". Return failed.")
