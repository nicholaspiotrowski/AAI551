# Author: Siyuan Fang, Nicholas Piotrowski
# Date: December 8th, 2023
"""Description:
This file handles all Creature objects in the Captain Veggie game.
Subclass of FieldInhabitant, veggie objects need functionality for their x and y coordinates.
Functionality includes getters and setters for these values
"""

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    def __init__(self, symbol, x, y):
        FieldInhabitant.__init__(self, symbol)
        self._x = x     # x coordinate of creature on field
        self._y = y     # y coordinate of creature on field

    def getXCoord(self):
        return self._x

    def getYCoord(self):
        return self._y

    def setXCoord(self, newX):
        self._x = newX

    def setYCoord(self, newY):
        self._y = newY
