#import statements
from Helper import inputInRange
from Helper import inputIsInt
from Helper import pressEnter
from Helper import clearTerminal
from Player import Player

#This is the game board
class Game(object):
    def __init__(self, players, response_cards, prompt_cards, max_points):
        #instance variables
        self.players = players
        self.response_cards = response_cards
        self.prompt_cards = prompt_cards
        self.max_points = max_points
        self.used_prompt_cards = []
        self.used_response_cards = []
        self.current_prompt_card = None
        self.card_czar = None
        self.card_czar_index = 0

    #method which starts and runs the game    
    def start(self): 
        self.handOutCards()
        #keep gaming continuing until winner
        while not self.isWinner():
            self.displayScore()
            self.rotateCardCzar()
            self.selectPromptCard()
            responses = self.getPlayerResponseCards()
            self.chooseWinningCard(responses)
        self.winningMessage(self.isWinner())

    #hand out starter cards to players
    def handOutCards(self):
        for player in self.players:
            player.addMultipleCards(self.response_cards[:5])
            self.response_cards = self.response_cards[5:]

    #rotate card czar every round
    def rotateCardCzar(self):
        new_czar_index = self.card_czar_index % len(self.players)
        self.card_czar = self.players[new_czar_index]
        self.card_czar_index += 1
        print("CARD CZAR ROTATION: " + self.card_czar.getName() + " is now the Card Czar\n")

    #returns the winner if they acheive points needed
    def isWinner(self):
        for player in self.players:
            if player.getScore() == self.max_points:
                return player
        return ""

    #selects the prompt card for the round
    def selectPromptCard(self):
        self.current_prompt_card = self.prompt_cards.pop(0)
        print(self.card_czar.getName() + " selected the prompt card\n")
        self.displayPromptCard()
        pressEnter()

    #prints prompt card
    def displayPromptCard(self):
        print("PROMPT")
        print(self.current_prompt_card + "\n")

    #rotate through players and get their responses to prompt
    def getPlayerResponseCards(self):
        playerResponses = []
        for i in range(0, len(self.players) - 1):
            #get next player
            player = self.rotatePlayer(i)
            print(player.getName() + "'s response selection is next")
            pressEnter()
            clearTerminal()
            print(player.getName() + "'s Response Selection\n")
            self.displayPromptCard()
            player_deck = player.getResponseDeck()
            #ask player for their response
            self.printPlayerResponseDeck(player_deck)
            card_index = self.askPlayerInput(player_deck)
            player_card = player_deck[card_index]
            print("You've selected " + player_card + "\n")
            playerResponses.append({'player': player, 'response': player_card})
            #player picks up a new card from the response deck
            self.pickUpNewCard(player, card_index)
        clearTerminal()
        return playerResponses

    #selects the next player for their responses
    def rotatePlayer(self, index):
        new_player_index = (self.card_czar_index + index) % len(self.players)
        return self.players[new_player_index]

    #prints a players response deck
    def printPlayerResponseDeck(self, player_deck):
        print("The option's\n")
        for index, card in enumerate(player_deck):
            print(str(index) + ": " + card + "")
        print("\n")

    #ask a player for their input to a question
    def askPlayerInput(self, player_deck):
        print("Which card do you want to select? Enter the card's number")
        user_val = inputInRange(0, len(player_deck) - 1)
        return int(user_val)
        print("\n")

    #player picks up a new card
    def pickUpNewCard(self, player, card_index):
        used_card = player.removeResponseCard(card_index)
        self.used_response_cards.append(used_card)
        player.addResponseCard(self.response_cards.pop(0))

    #card czar chooses his favorite card
    def chooseWinningCard(self, responses):
        print("CARD CZAR SELECTION\n")
        print(self.card_czar.getName() + ", please select your favorite card\n")
        self.displayPromptCard()
        listOfResponses = [d['response'] for d in responses]
        self.printPlayerResponseDeck(listOfResponses)
        user_val = self.askPlayerInput(listOfResponses)
        winning_card = listOfResponses[user_val]
        winner = responses[user_val]['player']
        print("The winning card is " + winning_card + "\n")
        print(winner.getName() + " won this round!\n")
        winner.addPromptCard(self.current_prompt_card)
        self.updateScore(winner)
        pressEnter()
        clearTerminal()

    #updates the scoreboard
    def updateScore(self, winner):
        winner.addPoint()

    #displays the scoreboard
    def displayScore(self):
        print("\n\nSCOREBOARD")
        for player in self.players:
            print("Player: " + player.getName() + "\tScore: " + str(player.getScore()))
        print("\n")

    #displays the winner and their won cards
    def winningMessage(self, winner):
        self.displayScore()
        print(winner.getName() + " is the winner!\n")
        print(winner.getName() + " won the cards: ")
        for card in winner.getPromptDeck():
            print(card)