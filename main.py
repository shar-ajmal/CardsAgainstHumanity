#import statements
import pickle
from GameSetup import gameSetup
from Game import Game
prompt_cards = []
response_cards = []

#load the prompt cards
with open('./DataClean/prompt_cards_b', 'rb') as f:
    prompt_cards = pickle.load(f)

#load the response cards
with open('./DataClean/response_cards_b', 'rb') as f:
    response_cards = pickle.load(f)

#set up the game
players, response_cards_shuffled, prompt_cards_shuffled, max_points = gameSetup(prompt_cards, response_cards)

#start the game
game = Game(players, response_cards_shuffled, prompt_cards_shuffled, max_points)
game.start()