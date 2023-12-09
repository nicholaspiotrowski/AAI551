# Author: Siyuan Fang, Nicholas Piotrowski
# Date: November 17th, 2023
"""Description:
This file handles the entirety of how the game runs - the game's engine.
This file manipulates objects and variables to make it so that game elements can change and move around,
thus allowing the game to progress and important details to be saved.
"""

import os
import random
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit


class GameEngine:
    __NUMBEROFVEGGIES = 30  # Number of Veggie objects to put into the game
    __NUMBEROFRABBITS = 5   # Number of Rabbit objects to put into the game
    __HIGHSCOREFILE = "highscore.data"  # Stores the name of the high score file

    def __init__(self):
        self.__field = []   # Represents the game field
        self.__rabbits = []     # Represents the rabbits in the game field
        self.__captain = None   # Represents the Captain object in the game field
        self.__possibleVegetables = []  # Represents all possible vegetables in the game
        self.__score = 0

    def initVeggies(self):
        """
        Uses a user-designated file to initialize the field with specific dimensions,
        then populate that field with __NUMBEROFVEGGIES veggie objects based on a pool of possible veggies given in the
        file
        :return: Nothing, no return
        """

        # Prompt user for an existing file with game details
        pointsFileName = input("Please enter the name of the vegetable point file: ")
        while not os.path.exists(pointsFileName):
            print(pointsFileName, "does not exist! Please enter the name of the vegetable point file: ")

        # Open user file to interact with it
        with open(pointsFileName) as pointsFile:
            # Initialize field with correct dimensions, all spaces set to None
            splitLine = pointsFile.readline().strip().split(',')
            self.__field = [[None for cols in range(int(splitLine[2]))] for rows in range(int(splitLine[1]))]

            # Read in and store details of possible Veggie objects that can populate the field from the file
            line = pointsFile.readline()
            while line:
                splitLine = line.strip().split(',')
                self.__possibleVegetables.append(Veggie(splitLine[1], splitLine[0], int(splitLine[2])))
                line = pointsFile.readline()

            # Populate field with __NUMBEROFVEGGIES veggie objects, each having their own unique field location and
            # being chosen from the list of possible veggies obtained from the user-designated file details
            veggiesPlaced = 0
            while veggiesPlaced < self.__NUMBEROFVEGGIES:
                # Generate a random row and column location to try in the field
                row = random.randrange(len(self.__field))
                col = random.randrange(len(self.__field[0]))
                # If field location does not contain a veggie object, populate it with a random veggie and update the
                # veggiesPlaced counter
                if not isinstance(self.__field[row][col], Veggie):
                    self.__field[row][col] = self.__possibleVegetables[random.randrange(len(self.__possibleVegetables))]
                    veggiesPlaced += 1

    def initCaptain(self):
        """
        Initialize the Captain object to a random, non-populated location in the field
        :return: Nothing, no return
        """
        # Keep trying to place the captain until successful
        captainPlaced = False
        while not captainPlaced:
            # Generate random location within the field's bounds
            row = random.randrange(len(self.__field))
            col = random.randrange(len(self.__field[0]))
            # If location is not populated, initialize a new Captain object there.
            if self.__field[row][col] is None:
                self.__captain = Captain(col, row)
                # Update field to reflect captain existing in the space. Update loop end condition variable.
                self.__field[row][col] = self.__captain
                captainPlaced = True

    def initRabbits(self):
        """
        Initialize __NUMBEROFRABBITS into unpopulated spots on the game field. Save these rabbits into the __rabbits
        list.
        :return: Nothing, no return
        """
        rabbitsPlaced = 0
        # While rabbits placed is less than NUMBEROFRABBITS that we want placed, keep generating random locations in an
        # attempt to find unpopulated spots to place new rabbits into
        while rabbitsPlaced < self.__NUMBEROFRABBITS:
            row = random.randrange(len(self.__field))
            col = random.randrange(len(self.__field[0]))
            if self.__field[row][col] is None:
                self.__rabbits.append(Rabbit(col, row))
                self.__field[row][col] = self.__rabbits[-1]
                rabbitsPlaced += 1

    def initializeGame(self):
        """
        Initialize the Captain Veggie game to have a complete starting board with the required pieces.
        Game elements initialized include Veggies, Captain, and Rabbits
        :return: Nothing, no return
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()

    def remainingVeggies(self):
        """
        Iterate through every space on the game field to count how many veggie objects are still on the game field.
        :return: Number of veggie objects left on the game field
        """
        veggiesLeftOnField = 0
        for row in range(len(self.__field)):
            for col in range(len(self.__field[row])):
                if isinstance(self.__field[row][col], Veggie):
                    veggiesLeftOnField += 1
        return veggiesLeftOnField

    def intro(self):
        """
        Output game information that will welcome and inform the user what the game pieces are and mean.
        :return: Nothing, no return
        """
        # Print welcome message explaining game premise
        print("\nWelcome to Captain Veggie!")
        print("\nThe rabbits have invaded your garden and you must harvest"
              "\nas many vegetables as possible before the rabbits eat them"
              "\nall! Each vegetable is worth a different number of points"
              "\nso go for the high score!")

        # Tell user about the game's vegetables, including name, symbol, and points
        print("The vegetables are: ")
        for veg in range(len(self.__possibleVegetables)):
            print(self.__possibleVegetables[veg])

        # Tell user what Captain Veggie's symbol is and what the rabbits' symbols are
        print("Captain Veggie is V, and the rabbits are R's.")
        print("Good luck!")

    def printField(self):
        """
        Output game field to user.
        :return: Nothing, no return
        """
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
        """
        Returns current game score
        :return: current game score
        """
        return self.__score

    def moveRabbits(self):
        """
        Move each rabbit in the list of rabbits up to 1 space in a random x, y direction.
        Rabbit movement can be up, down, left, right, diagonal, or none.  Cannot escape bounds of game field.
        :return: Nothing, no return
        """
        # For each rabbit in the list
        for i in range(len(self.__rabbits)):
            # Determine current rabbit position
            rabbit_x = self.__rabbits[i].getXCoord()
            rabbit_y = self.__rabbits[i].getYCoord()
            # Generate a random set of numbers for movement in x and y axes
            row_move = random.randint(-1, 1)
            col_move = random.randint(-1, 1)
            # Determine new hypothetical location
            newRow = rabbit_y + row_move
            newCol = rabbit_x + col_move
            # Only move if new location would be within the field bounds
            if 0 <= newRow < len(self.__field) and 0 <= newCol < len(self.__field[0]):
                # Only move if new location is not a Rabbit or Captain object
                if not isinstance(self.__field[newRow][newCol], Rabbit) and not isinstance(self.__field[newRow][newCol], Captain):
                    # Place rabbit in new field location, overwriting whatever was previously there.  This includes
                    # overwriting None or Veggie objects.  Save movement details in field object and in rabbit object in
                    # the rabbits list.
                    self.__field[newRow][newCol] = self.__rabbits[i]
                    self.__rabbits[i].setXCoord(newCol)
                    self.__rabbits[i].setYCoord(newRow)
                    # Set previous rabbit location to None
                    self.__field[rabbit_y][rabbit_x] = None

    def moveCptVertical(self, direction):
        """
        Move the captain in a vertical direction, reflecting this movement in the captain object and field list
        :param direction: integer representing how much to move captain on the y-axis
        :type direction: int
        :return: Nothing, no return
        """
        # Save current captain position in variables, as well as hypothetical new y position
        row = self.__captain.getYCoord()
        col = self.__captain.getXCoord()
        newRow = row + direction

        # If new position is empty, update Captain object and field list to reflect Captain moving into new space
        if self.__field[newRow][col] is None:
            self.__captain.setYCoord(newRow)
            self.__field[newRow][col] = self.__captain
        # If new position contains Veggie object, update Captain object to reflect new location and collection of the
        # new veggie.  Output message reflecting collection of game objective piece. Update current score based on
        # Veggie collected. Update field to reflect new Captain position.
        elif isinstance(self.__field[newRow][col], Veggie):
            self.__captain.setYCoord(newRow)
            print(f"Yummy! A delicious {self.__field[newRow][col].getName()}")
            self.__captain.addVeggie(self.__field[newRow][col])
            self.__score += self.__field[newRow][col].getPoints()
            self.__field[newRow][col] = self.__captain
        # If new position contains Rabbit object, do not move Captain and output appropriate message
        elif isinstance(self.__field[newRow][col], Rabbit):
            print("Don't step on the bunnies!")
        # If the Captain object is in a new location, update its previous location to None
        if self.__captain.getYCoord() == newRow:
            self.__field[row][col] = None

    def moveCptHorizontal(self, direction):
        """
        Move the captain in a vertical direction, reflecting this movement in the captain object and field list
        :param direction: integer representing how much to move captain on the y-axis
        :type direction: int
        :return: Nothing, no return
        """
        # Save current captain position in variables, as well as hypothetical new y position
        row = self.__captain.getYCoord()
        col = self.__captain.getXCoord()
        newCol = col + direction

        # If new position is empty, update Captain object and field list to reflect Captain moving into new space
        if self.__field[row][newCol] is None:
            self.__captain.setXCoord(newCol)
            self.__field[row][newCol] = self.__captain
        # If new position contains Veggie object, update Captain object to reflect new location and collection of the
        # new veggie.  Output message reflecting collection of game objective piece. Update current score based on
        # Veggie collected. Update field to reflect new Captain position.
        elif isinstance(self.__field[row][newCol], Veggie):
            self.__captain.setXCoord(newCol)
            print(f"Yummy! A delicious {self.__field[row][newCol].getName()}")
            self.__captain.addVeggie(self.__field[row][newCol])
            self.__score += self.__field[row][newCol].getPoints()
            self.__field[row][newCol] = self.__captain
        # If new position contains Rabbit object, do not move Captain and output appropriate message
        elif isinstance(self.__field[row][newCol], Rabbit):
            print("Don't step on the bunnies!")
        # If the Captain object is in a new location, update its previous location to None
        if self.__captain.getXCoord() == newCol:
            self.__field[row][col] = None

    def moveCaptain(self):
        """
        Allow for user to input desired Captain movement. Call appropriate function based on user input to move Captain
        to a new location.  Do not move captain if user input is invalid or new location is out of bounds.
        :return: Nothing, no return
        """
        direction = input("Would you like to move up(W), down(S), left(A), or right(D):")
        direction = direction.lower()
        match direction:
            case 'w':
                if self.__captain.getYCoord() - 1 >= 0:
                    self.moveCptVertical(-1)
                else:
                    print("You can't move that way!")
            case 'a':
                if self.__captain.getXCoord() - 1 >= 0:
                    self.moveCptHorizontal(-1)
                else:
                    print("You can't move that way!")
            case 's':
                if self.__captain.getYCoord() + 1 < len(self.__field):
                    self.moveCptVertical(1)
                else:
                    print("You can't move that way!")
            case 'd':
                if self.__captain.getXCoord() + 1 < len(self.__field[0]):
                    self.moveCptHorizontal(1)
                else:
                    print("You can't move that way!")
            case _:
                print(f"{direction} is not a valid option")

    def gameOver(self):
        """
        Output game over message, telling the user what Veggies they managed to harvest and their final score.
        :return: Nothing, no return
        """
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for veg in self.__captain.getVeggiesCollected():
            print(veg.getName())
        print(f"Your score was: {self.__score}")

    def highScore(self):
        """
        Handles the high score functionality of the game.  Allows user to record their initials and score into a high
        score pickle file. Reads file for existing scores, updates scores to include current player's details in the
        appropriate spot of the sorted scores, then saves all changes in the high scores file.
        Outputs all existing high score data for the user to see
        :return:
        """

        high_scores = []
        # Check if any high scores have been saved. If so, load the data into a list of tuples
        if os.path.exists(self.__HIGHSCOREFILE):
            with open(self.__HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)

        # Save first three initials of player
        player_initials = input("Please enter your three initials to go on the scoreboard: ")
        player_initials = player_initials[:3]

        # Create tuple for current player's initials and score
        current_player = (player_initials, self.__score)

        # If no pre-existing high scores exist, simply append current player's data to the high scores list
        if not high_scores:
            high_scores.append(current_player)
        # If at least one high score already exists, iterate through the list of all high scores to put the current
        # player's details into the correct spot on the list. List saves high scores by descending order of scores.
        else:
            for player_index in range(len(high_scores)):
                if current_player[1] >= high_scores[player_index][1]:
                    high_scores.insert(player_index, current_player)
                    break
        # Output all saved high scores
        print("HIGH SCORES"
              "\nName\tScore")
        for player in high_scores:
            print(f"{player[0]}\t\t{player[1]}")

        # Save all high scores to the appropriate file using pickling
        with open(self.__HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)
