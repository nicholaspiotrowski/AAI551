# Author:
# Date:
"""Description:

"""

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, 'V', x, y)
        self._veggiesCollected = []

    def addVeggie(self, veg):
        """
        Adds veggie object to veggies collected list
        :param veg:
        :type veg: Veggie object
        :return: None
        """
        self._veggiesCollected.append(veg)

    def getVeggiesCollected(self):
        return self._veggiesCollected

    def setVeggiesCollected(self, newVeggiesCollected):
        self._veggiesCollected = newVeggiesCollected
