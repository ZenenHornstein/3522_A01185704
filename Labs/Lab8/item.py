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
        Increment's the number of copies of an book

        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        reduce the number of copies of an book
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
    def call_number(self, call_number: int):
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

    def __init__(self, call_number, title, author, num_copies=1):
        """
        :param call_number: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """

        super().__init__(call_number, title, num_copies)
        self._author = author

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

    def check_availability(self):
        """
        Returns True if the book is available and False otherwise
        :return: A Boolean
        """
        if self.get_num_copies() > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"---- Book: {self._title} ----\n" \
               f"Call Number: {self._call_number}\n" \
               f"Author: {self._author}\n" \
               f"Number of copies: {self._num_copies}\n"


class DVD(Item):
    def __init__(self, call_number, name, release_date, region_code):
        super().__init__(call_number, name)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Release data: {self._release_date}\n" \
               f"Region code: {self._region_code}\n" \
               f"Number of copies {self._num_copies}"


class Journal(Item):

    def __init__(self, call_number, name, issue_number, publisher):
        super().__init__(call_number, name)
        self._publisher = publisher
        self._issue_number = issue_number

    def __str__(self):
        return f"---- Journal: {self._title} ----\n" \
               f"Call Number: {self._call_number}\n" \
               f"Issue Number: {self._issue_number}\n" \
               f"Publisher: {self._publisher}\n" \
               f"Number of copies : {self._num_copies}"
