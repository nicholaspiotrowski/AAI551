# Author: Siyuan Fang, Nicholas Piotrowski
# Date: November 17th, 2023
"""Description:

"""

import os
import random
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit


class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self.__field = []
        self.__rabbits = []
        self.__captain = None

        self.__possibleVegetables = []
        self.__score = 0

    # Nick
    def initVeggies(self):
        pointsFileName = input("Please enter the name of the vegetable point file: ")
        while not os.path.exists(pointsFileName):
            print(pointsFileName, "does not exist! Please enter the name of the vegetable point file: ")

        with open(pointsFileName) as pointsFile:
            splitLine = pointsFile.readline().strip().split(',')
            self.__field = [[None for cols in range(int(splitLine[2]))] for rows in range(int(splitLine[1]))]

            line = pointsFile.readline()
            while line:
                splitLine = line.strip().split(',')
                self.__possibleVegetables.append(Veggie(splitLine[1], splitLine[0], splitLine[2]))
                line = pointsFile.readline()

            veggiesPlaced = 0
            while veggiesPlaced < self.__NUMBEROFVEGGIES:
                row = random.randrange(len(self.__field))
                col = random.randrange(len(self.__field[0]))
                if not isinstance(self.__field[row][col], Veggie): # SEE IF THIS CAN BE CHANGED TO IF NONE
                    self.__field[row][col] = self.__possibleVegetables[random.randrange(len(self.__possibleVegetables))]
                    veggiesPlaced += 1

    def initCaptain(self):
        captainPlaced = False
        while not captainPlaced:
            row = random.randrange(len(self.__field))
            col = random.randrange(len(self.__field[0]))
            if self.__field[row][col] is None:
                self.__captain = Captain(col, row)
                self.__field[row][col] = self.__captain
                captainPlaced = True

    def initRabbits(self):
        rabbitsPlaced = 0
        while rabbitsPlaced < self.__NUMBEROFRABBITS:
            row = random.randrange(len(self.__field))
            col = random.randrange(len(self.__field[0]))
            if self.__field[row][col] is None:
                self.__rabbits.append(Rabbit(col, row))
                self.__field[row][col] = self.__rabbits[-1]
                rabbitsPlaced += 1

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        veggiesLeftOnField = 0
        for row in range(len(self.__field)):
            for col in range(len(self.__field[row])):
                if isinstance(self.__field[row][col], Veggie):
                    veggiesLeftOnField += 1
        return veggiesLeftOnField

    def intro(self):
        print("\nWelcome to Captain Veggie!")
        print("\nThe rabbits have invaded your garden and you must harvest"
              "\nas many vegetables as possible before the rabbits eat them"
              "\nall! Each vegetable is worth a different number of points"
              "\nso go for the high score!")

        print("The vegetables are: ")
        for veg in range(len(self.__possibleVegetables)):
            print(self.__possibleVegetables[veg])

        print("Captain Veggie is V, and the rabbits are R's.")
        print("Good luck!")

    def printField(self):
        # Output top border
        for col in range(len(self.__field[0])*3+2):
            print('#', end='')
        print()

        # Output left and right borders, as well as field contents
        for row in range(len(self.__field)):
            print('#', end='')
            for col in range(len(self.__field[row])):
                if self.__field[row][col] is None:
                    print('   ', end='')
                else:
                    print('', self.__field[row][col].getSymbol(), '', end='')
            print('#')

        # Output bottom border
        for col in range(len(self.__field[0])*3+2):
            print('#', end='')
        print()

    # Siyuan
    def getScore(self):
        return self.__score

    def moveRabbits(self):
        moved_rabbits = 0
        for i in range(len(self.__rabbits)):
            rabbit = self.__rabbits[i]
            row_move = random.randint(-1, 1)
            col_move = random.randint(-1, 1)
            #move within the field
            if 0 <= rabbit[1] + row_move < len(self.__field) and 0 <= rabbit[0] + col_move < len(self.__field[0]):
                row = rabbit[1] + row_move
                col = rabbit[0] + col_move
                if not self.__field[row][col] or isinstance(self.__field[row][col], Veggie):
                    self.__field[rabbit[1]][rabbit[0]] = None
                    rabbit = Rabbit(col, row)
                    self.__rabbits[i] = rabbit
                    self.__field[row][col] = rabbit

    def moveCptVertical(self, direction):
        row = self.__captain[1]
        col = self.__captain[0]
        if 0 <= row + direction < len(self.__field):
            if isinstance(self.__field[row + direction][col], Rabbit):
                return
            else:
                if isinstance(self.__field[row + direction][col], Veggie):
                    veg = self.__field[row + direction][col]
                    print(f"Yummy! A delicious {veg.name}")
                    self.__captain.addVeggie(veg)
                    self.__score += veg.getPoints()
                vegcollected = self.__captain.setVeggiesCollected()
                newCap = Captain(col, row + direction)
                self.__field[row][col] = None
                self.__captain = newCap
                self.__captain.setVeggiesCollected(vegcollected)
                self.__field[row + direction][col] = self.__captain


    def moveCptHorizontal(self, direction):
        row = self.__captain[1]
        col = self.__captain[0]
        if 0 <= col + direction < len(self.__field):
            if isinstance(self.__field[row][col + direction], Rabbit):
                return
            else:
                if isinstance(self.__field[row][col + direction], Veggie):
                    veg = self.__field[row][col + direction]
                    print(f"Yummy! A delicious {veg.name}")
                    self.__captain.addVeggie(veg)
                    self.__score += veg.getPoints()
                vegcollected = self.__captain.setVeggiesCollected()
                newCap = Captain(col + direction, row)
                self.__field[row][col] = None
                self.__captain = newCap
                self.__captain.setVeggiesCollected(vegcollected)
                self.__field[row][col + direction] = self.__captain
    def moveCaptain(self):
        direction = input("Would you like to move up(W), down(S), left(A), or right(D):")
        direction = direction.lower()
        if direction == "w":
            self.moveCptVertical(1)
        elif direction == "s":
            self.moveCptVertical(-1)
        elif direction == "a":
            self.moveCptHorizontal(-1)
        elif direction == "a":
            self.moveCptHorizontal(1)
        else:
            print(f"{direction} is not a valid option")
        print(f"{self.remainingVeggies()} veggies remaining. Current score: {self.__score}")
    def gameOver(self):
        print("Game Over")
        print("You managed to harvest the following vegetables:")
        for veg in self.__captain.setVeggiesCollected():
            print(veg.getname)

     # def highScore(self):
        # if os.path.exists('highscore.data'):
        #     with open('highscore.data', 'rb') as file:
        #         high_scores = pickle.load(file)
