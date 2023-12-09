# Author: Siyuan Fang, Nicholas Piotrowski
# Date: November 18th, 2023
"""Description:
Main file that calls appropriate functions from the Game Engine to run the Captain Veggie game for the user.
File that the user needs to run to play the game, this file utilizes all relevant game elements using the engine
"""
from GameEngine import GameEngine


def main():
    # Initialize the Captain Veggie game
    captainVeggieGame = GameEngine()
    captainVeggieGame.initializeGame()
    captainVeggieGame.intro()

    # Find out how many starting Veggies are in this game
    veggiesRemaining = captainVeggieGame.remainingVeggies()

    # While there are still veggies in the game, keep outputting field with its changes, calling the appropriate
    # functions for the game elements to move, interact, and develop. Keep track of and output the remaing veggies on
    # the field and the current score
    while veggiesRemaining > 0:
        print(f"{veggiesRemaining} veggies remaining. Current score: {captainVeggieGame.getScore()}")
        captainVeggieGame.printField()
        captainVeggieGame.moveRabbits()
        captainVeggieGame.moveCaptain()

        veggiesRemaining = captainVeggieGame.remainingVeggies()

    # Run the game's game over and high score protocols
    # This lets the player know how they did and lets them save their score to a list of high scores
    captainVeggieGame.gameOver()
    captainVeggieGame.highScore()


main()
