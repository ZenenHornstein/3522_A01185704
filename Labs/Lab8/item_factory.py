import abc
from Labs.Lab8.item import Book
from Labs.Lab8.item import Journal
from Labs.Lab8.item import DVD


class ItemFactory(abc.ABC):

    def __init__(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def create_item():
        pass


class BookFactory(ItemFactory):
    @staticmethod
    def create_item():
        call_number = input("Please enter a call number for the book. ")
        title = input("Please enter a title for the book. ")
        author = input("Please enter an author for the book. ")
        return Book(call_number=call_number, title=title, author=author)


class JournalFactory(ItemFactory):
    @staticmethod
    def create_item():
        call_number = input("Please enter a call number for the journal. ")
        name = input("Please enter a name for the journal. ")
        publisher = input("Please enter a Publisher for the journal. ")
        issue_number = int(input("Pleas enter a issue_number for the journal. "))
        return Journal(call_number=call_number, name=name, publisher=publisher, issue_number=issue_number)


class DVDFactory(ItemFactory):
    @staticmethod
    def create_item():
        call_number = input("Please enter a call number for the DVD ")
        name = input("Please enter a name for the DVD")
        release_date = input("Please enter a release date for the DVD. ")
        region_code = input("Please enter a region code for the DVD ")
        return DVD(call_number=call_number, name=name, release_date=release_date, region_code=region_code)
