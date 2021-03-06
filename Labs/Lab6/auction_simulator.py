"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def get_highest_bid(self):
        return self._highest_bid

    def get_highest_bidder(self):
        return self._highest_bidder

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)
        pass

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = []
        self._highest_bid = 0

        pass

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            bidder(self)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """

        self._highest_bidder = bidder
        self._highest_bid = bid
        self._notify_bidders()

        # Every time the auctioneer accepts a bid, all bidders should be notified and given the chance
        # to retaliate by placing a new bid

    @property
    def highest_bidder(self):
        return self._highest_bidder

    @property
    def highest_bid(self):
        return self._highest_bid


class Bidder:

    def __init__(self, name=None, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        if not name:
            name = input("Please enter the name of the bidder")
        if not budget:
            budget = float(input("Please enter the budget of this bidder"))
        if not bid_probability:
            bid_probability = float(input("What is this bidders bid probability?"))
        if not bid_increase_perc:
            bid_increase_perc = float(input("What is this bidders bid_increase_percent?"))
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        bid = self.bid_increase_perc * auctioneer.get_highest_bid()

        if auctioneer.get_highest_bidder() is not self and bid <= self.budget and self.bid_probability >= random.random():
            self.highest_bid = bid
            print(
                f"{self.name} bid {bid} in response to {auctioneer.get_highest_bidder()}'s bid"
                f" of {auctioneer.get_highest_bid()} ")
            auctioneer.accept_bid(self.highest_bid, self)

    def __str__(self):
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder

        """
        #    self._observers = bidders
        self._core = Auctioneer()
        self._observers = bidders
        self.attach_bidders(self._core)

    def attach_bidders(self, auctioneer):
        """
        Attach observers to core.
        :param auctioneer: the core
        :return:
        """
        for bidder in self._observers:
            auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print(f"Auctioning {item} starting at {start_price}")
        start_bidder = Bidder("starting bidder", budget=start_price + 1, bid_probability=1.00, bid_increase_perc=1.0)
        self._core.accept_bid(start_price, start_bidder)
        print(f"\nThe winner of the auction is: {self._core.highest_bidder} at ${self._core.highest_bid}")
        print(f"\nHighest Bids per bidder:")
        for bidder in self._observers:
            print(f"Bidder: {bidder.name} Highest Bid: {bidder.highest_bid}")


def main():
    bidders = []

    item = input("Please enter the name of the item to aution")
    item_starting_price = float(input("Please enter the starting price"))


    bidder_type = input("Enter 1 for hardcoded bidders or 2 for custom bidders")
    while bidder_type not in ("1", "2"):
        bidder_type = input("Please choose a valid option")



    if bidder_type == "1":
      bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
      bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
      bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
      bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
      bidders.append(Bidder("Scott", 4000, random.random(), 2))

    elif bidder_type == "2":
        num_bidders = int(input("Please enter the number of bidders!"))

        for i in range(1, num_bidders + 1):
            print(f"Initializing bidder {i}")
            bidders.append(Bidder(name=None, bid_probability=None, bid_increase_perc=None, budget=None))


    print("\n\nStarting Auction!!")
    print("------------------")
    my_auction = Auction(bidders)
    my_auction.simulate_auction(item, item_starting_price)


if __name__ == '__main__':
    main()
