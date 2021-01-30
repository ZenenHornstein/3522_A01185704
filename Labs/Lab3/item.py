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
