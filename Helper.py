#import statements
from Player import Player
import os

#clears the terminal
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#creates the players
def createPlayers(num_players):
    players = []
    for i in range(0, num_players):
        print("What is the name of player " + str(i+1))
        name = input()
        player = Player(name)
        players.append(player)
    return players 
    
#lists the players
def printPlayers(players):
    print("PLAYERS:")
    for player in players:
        print(player)
    print('\n\n\n')

#checks to see if input is in range
def inputInRange(min_val=False, max_val=False):
    while True:
        user_input = input()
        if not user_input.isdigit(): 
            print("Sorry, that input is incorrect")
            continue
        elif int(user_input) not in range(min_val, max_val + 1):
            print("Sorry, that input is out of range")
            continue
        else:
            return int(user_input)

#check to see if input is out of range
def inputIsInt():
    while True:
        user_input = input()
        if not user_input.isdigit(): 
            print("Sorry, that input is incorrect")
            continue
        else:
            return int(user_input)  

#prompts the user to press enter
def pressEnter():
    print("Press the 'Enter' key to continue")
    input()