"""Users to participate in and an Auction to run a second-price auction.

Classes:

    Auction
    User

Functions:

    execute_round()
    show_ad() -> bool
"""

import numpy as np


class Auction:
    """Class to represent an online second-price ad auction"""
    def __init__(self, users, bidders):
        """Initializing users (list), bidders (list), and dictionary to store balances for each bidder in the auction"""
        self.users = users
        self.bidders = bidders
        # balances for each bidder in the auction
        self.balances = {bidder: 0 for bidder in self.bidders}
        self.qualified_bidders = [bidder for bidder, balance in self.balances.items() if balance > -1000]

    def __repr__(self):
        """Return auction object with users and qualified bidders"""
        return f'Auction with users={self.users} and self.bidders={self.qualified_bidders}'

    def __str__(self):
        """Return auction object with users and qualified bidders"""
        return self.__repr__()

    def execute_round(self):
        """Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price
            """
        # choose a user at random
        user_id = np.random.randint(0, len(self.users))
        user_prob = self.users[user_id]

        # collect bids from every qualified bidder in the auction
        bids = {}
        for bidder in self.balances:
            if self.balances[bidder] > -1000:
                bids[bidder] = bidder.bid(user_id)

        # select winning bidder    
        winning_bid = max(bids.values())
        # determine which bidder(s) are associated with max bid
        winning_bidders = [bidder for bidder, bid in bids.items() if bid == winning_bid]
        # break a tie
        if len(winning_bidders) == 1:
            winner = winning_bidders[0]
            bids.pop(winner)
        else:
            winners_index = np.random.randint(0, len(winning_bidders))
            winner = winning_bidders[winners_index]
            bids.pop(winner)

        # selection of actual price
        if len(bids) == 0:
            price = winning_bid
        else:
            price = max(bids.values())

        # show ad to user and find out whether or not they click
        did_user_click = user_prob.show_ad()
        # update Auction balances
        self.balances[winner] -= price
        if did_user_click:
            self.balances[winner] += 1

        # notify winner of its new balance
        winner.balance = self.balances[winner]

        # notify bidders of price
        for bidder in self.bidders:
            if bidder != winner:
                auction_winner = False
                did_user_click = None
            elif bidder == winner:
                auction_winner = True
            bidder.notify(auction_winner, price, did_user_click)


class User:
    """Class to represent a user with a secret probability of clicking an ad."""

    def __init__(self):
        self.__probability = np.random.uniform()

    def __repr__(self):
        return str(self.__probability)

    def __str__(self):
        """User object with a secret likelihood of clicking on an ad"""
        return self.__repr__()

    def show_ad(self):
        """Returns True to represent the user clicking on an ad or False otherwise"""
        result = np.random.choice([True, False], p=[self.__probability, 1 - self.__probability])
        return result
    