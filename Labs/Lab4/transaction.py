from dataclasses import dataclass
import datetime as dt

class Transaction:
    """
    Represents a transaction Object.
    """
    def __init__(self, timestamp, dollar_amt, location, budget_category):
        """
        Instantiate a new Transaction
        :param timestamp: the time and date of the transaction as a datetime object
        :param dollar_amt: amount spent in the transaction as a float.
        :param location: where the transaction took place as a str.
        :param budget_category: the budget catagory this trans falls under as a str.
        """
        self._timestamp = timestamp
        self._dollar_amt = dollar_amt
        self._location = location
        self._budget_category = budget_category

    def __str__(self):
        return F"{self._dollar_amt} dollars spent at {self._location} on {self._timestamp} ({self._budget_category})"

