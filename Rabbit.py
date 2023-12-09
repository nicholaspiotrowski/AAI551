# Author: Siyuan Fang, Nicholas Piotrowski
# Date: December 8th, 2023
"""Description:
This file handles rabbit objects in the Captain Veggie game.
Subclass of Creature, rabbit objects need to have their symbol
defined as 'R' and need to be their own object type.
The Rabbit represents a game obstacle.
"""

from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, 'R', x, y)
