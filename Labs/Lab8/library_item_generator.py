from Labs.Lab8.item_factory import BookFactory
from Labs.Lab8.item_factory import DVDFactory
from Labs.Lab8.item_factory import JournalFactory

class LibraryItemGenerator:

    @staticmethod
    def generate_item(classes=None):
        """
        A static method which accepts a list of Factory Classes , prompts the user for a factory to use and create
        the item generated by that factory.

        :param classes: a list of factory classes
        :return: instance of an type contained in classes
        """

        if classes is None:
            classes = [BookFactory, DVDFactory, JournalFactory]
        factories = [x.__name__ for x in classes]

        # Print user options
        print("\nWelcome to the Item Generator!")

        for index, choice in enumerate(factories):
            print(f"{index} for {choice} ")
        print("or 7 to quit.")

        user_input = int(input("Please enter your choice "))

        while user_input not in {0, 1, 2, 7}:
            user_input = int(input("Please enter a valid choice "))

        if user_input == 7:
            print("Thank you come again!")
            exit(0)

        return classes[user_input].create_item()
