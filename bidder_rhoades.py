"""A random bidder for a second-price auction.

Classes:

    Bidder

Functions:

    bid(user_id) -> float
    notify(auction_winner, price, clicked)
"""

import numpy as np

class Bidder:
    """Class to represent a bidder in an online second-price ad auction"""
    def __init__(self, num_users, num_rounds):
        """Setting number of users (int), number of rounds (int), and round counter"""
        self.__num_users = num_users
        self.__num_rounds = num_rounds
        # each Bidder begins with a balance of 0 dollars
        self.__balance = 0.0
        self.__history = []

    def __repr__(self):
        """Return Bidder object"""
        return f'''Random Bidder with balance = {self.__balance}
        in auction with {self.__num_users} users and {self.__num_rounds} rounds'''

    def __str__(self):
        """Return Bidder object"""
        return self.__repr__()

    def bid(self, user_id):
        """Returns a non-negative bid amount"""
        # a bid is any non-negative amount of money in dollars rounded to 3 decimal places
        self.__user_id = user_id
        self.__history.append(self.__user_id)
        return round(np.random.uniform(0,1), 3)

    def notify(self, auction_winner, price, clicked):
        """Updates bidder attributes based on results from an auction round"""
