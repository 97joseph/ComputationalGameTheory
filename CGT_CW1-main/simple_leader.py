"""
A simple leader for the Stackelberg game.
"""
from base_leader import Leader
import random

___author___ = "Rokas"


class SimpleLeader(Leader):
    def __init__(self, name):
        # If you want to initialize something here, do it before the super() call.
        super().__init__(name)

    def new_price(self, date: int) -> float:
        """
        A function for setting the new price of each day.
        :param date: date of the day to be updated
        :return: (float) price for the day
        """
        self.log(date)

        # returns a random number between [1.7, 1.8]
        return 1.7 + random.random() * 0.1

    def start_simulation(self):
        """
        A function run at the beginning of the simulation.
        """
        self.log("Start of simulation")

    def end_simulation(self):
        """
        A function run at the end of the simulation.
        """
        self.log("End of simulation")


if __name__ == '__main__':
    # Make sure you set this to your group number!
    SimpleLeader('1')
