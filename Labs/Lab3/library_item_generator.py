class LibraryItemGenerator:

    @staticmethod
    def generate_item(classes=None):
        """
        A static method which accepts a list of Class types, prompts the user for a class to create
        then generates that class with inputs from the user.

        :param classes: a list of Classes
        :return: instance of an type contained in classes
        """

        choices = [x.__name__ for x in classes]

        # Print user options
        print("\nWelcome to the Item Generator!")

        for index, choice in enumerate(choices):
            print(f"{index} for {choice} ")
        print("or 7 to quit.")

        user_input = int(input("Please enter your choice "))

        while user_input not in (0, 1, 2, 7):
            user_input = int(input("Please enter a valid choice "))

        if user_input == 7:
            print("Thank you come again!")
            exit(0)

        return classes[user_input]()
