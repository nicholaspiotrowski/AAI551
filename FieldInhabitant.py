# Author: Siyuan Fang, Nicholas Piotrowski
# Date: December 8th, 2023
"""Description:
Superclass used for all field inhabitants objects of the Captain Veggie game
All inhabitants have a symbol and this file handles that functionality
"""


class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol   # Symbol is character that represents inhabitant on field graphic output

    def getSymbol(self):
        return self._symbol

    def setSymbol(self, newSymbol):
        self._symbol = newSymbol
