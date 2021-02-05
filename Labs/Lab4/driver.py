import datetime as dt
from Labs.Lab4.transaction import Transaction
from Labs.Lab4.user_type import UserType
from Labs.Lab4.budget import Budget



def display_menu(acc_user):
    """
    Main loop. Drives the program.

    :param acc_user: the user who wished to interact with the FAM.
    :return: None
    """
    user_input = None
    while user_input != "7":
        print("\nWelcome to the FAM main loop")
        print("-----------------------")
        print("1. View Budgets ")
        print("2. Record Transaction(s)")
        print("3. View Transactions")
        print("4. View Bank Account Details")
        print("6. Quit")
        user_input = input("Please enter your choice (1-7)")

        if user_input == "2":
            acc_user.make_transaction()
        if user_input == "3":
            acc_user.view_transactions()
        if user_input == "6":
            print("Goodebye!")
            exit(0)


def main():
    test_user = UserType.create_test_user()
    display_menu(test_user)

    
if __name__ == '__main__':
    main()
