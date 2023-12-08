# Author: Siyuan Fang, Nicholas Piotrowski
# Date: November 18th, 2023
"""Description:

"""

from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, 'R', x, y)
