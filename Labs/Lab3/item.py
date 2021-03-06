import abc

class Item(abc.ABC):

    def __init__(self, call_number, title, num_copies=1):
        self._call_number = call_number
        self._num_copies = num_copies
        self._title = title

    def get_title(self):
        return self._title

    def increment_number_of_copies(self):
        """
        Set's the number of copies of an book
        :param value: a positive integer
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Set's the number of copies of an book
        :param value: a positive integer
        """
        self._num_copies -= 1

    @property
    def call_number(self):
        """
        The getter of the Item id number

        :return idNumber: the  id number of the Item, as an int
        """
        return self._call_number

    @call_number.setter
    def call_number(self, call_number: int) -> int:
        """

      :param call_number: the call number
      :return: none
      """
        self._call_number = call_number


class Book(Item):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, call_number=None, title=None, num_copies=1, author=None):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        if not call_number:
            call_number = input("Please enter a call number for the book ")
        if not title:
            title = input("Please enter a name for the book. ")
        if not num_copies:
            num_copies = int(input("How many copies are there? "))
        if not author:
            author = input("Who is the author of this book? ")

        super().__init__(call_number, title)
        self._author = author
        self._num_copies = num_copies

    # @property
    # def title(self):
    #     return self._title
    #
    # @title.setter
    # def title(self, new_title):
    #     self._title = new_title




    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific book.
        :return: an int
        """
        return self._num_copies

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self._call_number

    # @call_number.setter
    # def call_number(self, value):
    #     """
    #     This is the decorator way to create a SET property. This would
    #     allow us to invoke this method by simply saying
    #     my_book.call_number = "102.345.992". I've commented this out
    #     since call numbers should not need a setter.
    #     :param value: a string
    #     :precondition value: a unique call number identifier
    #     """
    #     self._call_num = value

    def check_availability(self):
        """
        Returns True if the book is available and False otherwise
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"---- Book: {self._title} ----\n" \
               f"Call Number: {self._call_number}\n" \
               f"Author: {self._author}\n" \
               f"Number of copies: {self._num_copies}"



class DVD(Item):
    def __init__(self, call_number=None, name=None, release_date=None, region_code=None):

        if not call_number:
            call_number = input("Please enter a call number ")

        if not name:
            name = input("Please enter a name ")

        if not release_date:
            release_date = input("Please enter a release date. ")

        if not region_code:
            region_code = input("Please enter a region code ")

        super().__init__(call_number, name)

        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Release data: {self._release_date}\n" \
               f"Region code: {self._region_code}\n"\
               f"Number of copies {self._num_copies}"

from item import Item

class Journal(Item):

    def __init__(self, call_number=None, name=None, issue_number=None, publisher=None):

        if not call_number:
            call_number = input("Please enter a call number for the journal. ")
        if not name:
            name = input("Please enter a name for the journal. ")
        if not publisher:
            publisher = input("Please enter a Publisher for the journal. ")
        if not issue_number:
            issue_number = int(input("Pleas enter a issue_number for the journal. "))

        super().__init__(call_number, name)
        self._publisher = publisher
        self._issue_number = issue_number




    def __str__(self):
        return f"---- Journal: {self._title} ----\n" \
               f"Call Number: {self._call_number}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}\n"\
               f"Number of copies : {self._num_copies}"

