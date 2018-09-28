#this object represents a player
class Player(object):
    def __init__(self, name):
        #instance variables
        self.name = name
        self.prompt_deck = []
        self.response_deck = []
        self.points = 0
        
    #toString method of user
    def __str__(self):
        return self.name

    #gets the specific card from user's deck
    def pickCard(self, card_index):
        return response_deck[card_index]

    #adds a response card to user's deck
    def addResponseCard(self, response_card):
        self.response_deck.append(response_card)

    #adds a prompt card to user's deck
    def addPromptCard(self, prompt_card):
        self.prompt_deck.append(prompt_card)

    #adds a list of response cards to user's deck
    def addMultipleCards(self, cards):
        for card in cards:
            self.addResponseCard(card)

    #removes a response card from user's deck
    def removeResponseCard(self, card_index):
        return self.response_deck.pop(card_index)

    #adds a point to the user
    def addPoint(self):
        self.points += 1

    #gets the user's name
    def getName(self):
        return self.name

    #get's the user's score
    def getScore(self):
        return self.points

    #get's the user's prompt deck
    def getPromptDeck(self):
        return self.prompt_deck

    #get's the user's response deck
    def getResponseDeck(self):
        return self.response_deck