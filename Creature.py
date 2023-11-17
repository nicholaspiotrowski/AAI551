# Author: Siyuan Fang, Nicholas Piotrowski
# Date: 11/17/2023
"""Description:

"""

from FieldInhabitant import FieldInhabitant


class Creature(FieldInhabitant):
    def __init__(self, symbol, x, y):
        FieldInhabitant.__init__(self, symbol)
        self._x = x
        self._y = y

    def getXCoord(self):
        return self._x

    def getYCoord(self):
        return self._y

    def setXCoord(self, newX):
        self._x = newX

    def setYCoord(self, newY):
        self._y = newY
