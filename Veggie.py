# Author: Siyuan Fang, Nicholas Piotrowski
# Date: December 8th, 2023
"""Description:
This file handles all veggie objects in the Captain Veggie game.
Subclass of FieldInhabitant, veggie objects need functionality for their name and points value.
Functionality includes get and set name, and a custom str output for the object for an easy-to-understand string
representing the object
The Veggie represents a game objective.
"""

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, symbol, name, points):
        FieldInhabitant.__init__(self, symbol)
        self.__name = name      # Name of the veggie
        self.__points = points  # Points the veggie is worth

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
