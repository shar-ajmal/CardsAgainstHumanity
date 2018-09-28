#import statements
import random
from Helper import createPlayers
from Helper import printPlayers
from Helper import inputInRange
from Helper import inputIsInt
from Helper import pressEnter
from Player import Player
from Helper import clearTerminal

#sets up the game
def gameSetup(prompt_cards, response_cards):
    random.shuffle(prompt_cards)
    random.shuffle(response_cards)
    print("Welcome to the console version of Cards Against Humanity!")
    pressEnter()

    #select the number of players
    print("How many people would you like to play. Minimum is 3, Maximum is 5")
    num_players = inputInRange(3,5)
    print(str(num_players) + " people are playing")

    #select how many points are needed
    print("How many points are needed to win?")
    max_points = inputIsInt()
    print("A player needs " + str(max_points) + " points to win")

    #name the players
    players = createPlayers(num_players)
    printPlayers(players)
    clearTerminal()
    return (players, response_cards, prompt_cards, max_points)