# Author: Siyuan Fang, Nicholas Piotrowski
# Date: November 18th, 2023
"""Description:

"""

from GameEngine import GameEngine


def main():
    captainVeggieGame = GameEngine()
    captainVeggieGame.initializeGame()
    captainVeggieGame.intro()

    veggiesRemaining = captainVeggieGame.remainingVeggies()

    while veggiesRemaining > 0:
        print(f"{veggiesRemaining} veggies remaining. Current score: ")  # INSERT SCORE HERE
        captainVeggieGame.printField()
        veggiesRemaining -= 10
        # MOVE RABBITS HERE
        captainVeggieGame.moveRabbits()
        # MOVE CAPTAIN HERE
        captainVeggieGame.moveCaptain()
        # DETERMINE NEW NUMBER OF REMAINING VEGGIES HERE
        veggiesRemaining = captainVeggieGame.remainingVeggies()
    # Display Game Over info here
    captainVeggieGame.gameOver()
    # Handle High Score functionality here
    captainVeggieGame.highScore()

main()
