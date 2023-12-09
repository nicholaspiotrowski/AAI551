# Author: Siyuan Fang, Nicholas Piotrowski
# Date: December 8th
"""Description:
This file handles the captain object in the Captain Veggie game.
Subclass of Creature, the captain object need functionality for their veggies collected.
Functionality includes a getter and setter, and a way to add new veggies to their list.
The captain represents the playable character
"""

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, 'V', x, y)
        self._veggiesCollected = []     # List representing all veggies the captain manages to collect in the game

    def addVeggie(self, veg):
        """
        Adds veggie object to veggies collected list
        :param veg: Veggie object that captain managed to get. Contains a name, symbol, and points.
        :type veg: Veggie object
        :return: None
        """
        self._veggiesCollected.append(veg)

    def getVeggiesCollected(self):
        return self._veggiesCollected

    def setVeggiesCollected(self, newVeggiesCollected):
        self._veggiesCollected = newVeggiesCollected
