# Author:
# Date:
"""Description:

"""

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, symbol, name, points):
        FieldInhabitant.__init__(self, symbol)
        self.__name = name
        self.__points = points

    def getName(self):
        return self.__name

    def getPoints(self):
        return self.__points

    def setName(self, newName):
        self.__name = newName

    def setPoints(self, newPoints):
        self.__points = newPoints

    def __str__(self):
        return f"{self._symbol}: \t{self.__name}\t {self.__points} points"
