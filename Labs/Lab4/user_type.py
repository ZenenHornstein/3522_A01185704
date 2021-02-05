from Labs.Lab4.transaction import Transaction
from Labs.Lab4.budget import Budget
import abc
import datetime as dt

class UserType(abc.ABC):
    """
    The abstract Base Class, for which all of the other user Types will be derived.
    Angel, Troublemaker and Rebel will all subclass this Class.

    """

    id = 0

    @staticmethod
    def generate_id() -> int:
        """
        Generate a unique ID for this User
        :return: a new unique sequential ID number.
        """
        UserType.id = UserType.id + 1
        return UserType.id

    @staticmethod
    def create_test_user():
        """
        Creates a hard coded test user for testing. This user has no prior transactions.
        :return:
        """
        return UserType(age=19,
                        name="BigTurkey",
                        bank_name="TD Amitrade",
                        bank_balance=20000,
                        bank_account_number=70.0,
                        budgets=Budget.create_test_budget(),
                        transactions=[
                            Transaction(timestamp=dt.datetime.now().date(),
                                        location="London Drugs", dollar_amt=50.0,
                                        budget_category="games and entertainment")
                        ])

    def __init__(self, name, age, bank_account_number, bank_name, bank_balance, budgets, transactions):
        """

        :param name: name as str
        :param age: age as int
        :param bank_account_number: bank_account_number as int
        :param bank_name: bank_name as str
        :param bank_balance: balance as a float
        :param budgets: an instance of class Budget
        :param transactions: a list of instances of class Transaction
        """
        if transactions is None:
            transactions = []
        self._name = name
        self._age = age
        self._bank_account_number = bank_account_number
        self._bank_name = bank_name
        self.bank_balance = bank_balance
        self._id = UserType.generate_id()
        self._budgets = budgets
        self._transactions = transactions

    @property
    def name(self):
        """
        Get the name of the UserType

        :return name: the name of the UserType, as a str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Set the name of the UserType

        :param name: the name of the UserType
        :precondition name: a str
        """
        self._name = name

    @property
    def age(self):
        """
        The age of the UserType

        :return age: the age of the UserType, as a int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """
        Set the age of the UserType

        :param age: the age of the UserType
        :precondition age: a nonzero int
        """
        self._age = age

    @property
    def bank_account_number(self):
        """
        The bank account number of the UserType

        :return bank_account_number: the bank account number of the UserType, as an int
        """
        return self._bank_account_number

    @bank_account_number.setter
    def bank_account_number(self, bank_account_number:int):
        """
        Set the bank account number of the UserType

        :param bank_account_number: the bank account number of the UserType
        :precondition bank_account_number: a positive nonZero int
        """

        self._bank_account_number = bank_account_number

    @property
    def bank_name(self):
        """
        The name of the bank which the user uses.

        :return bank_name: the name of the bank, as a str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name:str ):
        """
        Set the name of the bank of the UserType

        :param bank_name: the name of the bank of the UserType
        :precondition bank_name: a str
        """
        self._bank_name = bank_name

    @property
    def balance(self):
        """
        The balance of the userTypes bank account

        :return balance: the balance of the userTypes bank account, as a float
        """
        return self._balance

    @balance.setter
    def balance(self, balance: float):
        """
        Set the balance of the userTypes bank account

        :param balance: the balance of the userTypes bank account
        :precondition balance: a positive float
        """
        self._balance = balance

    @property
    def budgets(self):
        return self._budgets


    def issue_warning(self):
        pass

    def check_lock(self):
        pass

    def view_transactions(self):
        """
        Prints a list of this users past transactions.
        :return:
        """
        for t in self._transactions:
            print(t)

    def make_transaction(self):
        """
        Prompt user for transaction details and carry out the transaction if viable.
        :return: None
        """
        dollar_amt = float(input("What is the dollar amount of the transaction"))
        print("1. Games and Entertainment")
        print("2. Clothing and Accesories")
        print("3. Eating Out")
        print("4. Miscellaneous")
        budget_cat = input("What budget category does this transaction fall under?")
        loc = input("Where did this transaction t ake place?")

        if budget_cat == "1":
            budget_cat = "games and entertainment"

        if budget_cat == "2":
            budget_cat = "Clothing and Accessories"

        if budget_cat == "3":
            budget_cat = "Eating Out"

        if budget_cat == "4":
            budget_cat ="Misc"

        transac = Transaction(budget_category=budget_cat,
                              location=loc,
                              timestamp=dt.datetime.now().date(),
                              dollar_amt=dollar_amt)

        if dollar_amt > self.bank_balance:
            print("Unable to carry out this transaction, not enough funds!")
            return
        else:
            self._transactions.append(transac)
            print("transaction completed!")




class UserTypeAngel(UserType):

    def __init__(self, name, age, user_type, bank_account_number, bank_name, bank_balance, budgets, transactions):
        super().__init__(name, age, user_type, bank_account_number, bank_name, bank_balance, budgets, transactions)

    def make_transaction(self):
       # do_transaction()
       self.check_lock()
       pass

    def issue_warning(self):
        print("It seems you have exceed more than 90% of a budget")
        pass

    def check_lock(self):
        # Warning if budget catagory exceed by 90%
        # Polite notification if budget catagory exceeded.
        pass


class UserTypeTroubleMaker(UserType):

    def make_transaction(self):
        pass

    def issue_warning(self):
        #if any budget catagory exceed by 25% issue polite warning
        pass

    def check_lock(self):
        # Warning if budget catagory exceed by 75%
        # Polite notification if budget catagory exceeded.
        # Locked out of budget catagory if exeeded by 120%
        pass


class UserTypeRebel(UserType):

    def make_transaction(self):
        # do_transaction()
        # Ruthelessly notified if a budget catagoriy is exceeded
        pass

    def issue_warning(self):
        # Warning for every Transaction after bidget exceeded by 50%
        pass

    def check_lock(self):
        # Locked out of budget catagory if exeeded by 120%
        # Locked out completely if two budgets exceede
        pass








