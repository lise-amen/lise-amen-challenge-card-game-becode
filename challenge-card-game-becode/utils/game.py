# game.py
from utils.player import Player

from utils.player import Deck

class Board():

    def __init__(self, players : list) :
        self.players = list()
        for name in players :
            self.players.append(Player(name)) #add name in self.players list
        self.turn_count = 0
        self.active_cards = list()
        self.history_cards  = list()

    def start_game(self) :
        create_deck = Deck() #create a deck in the deck class
        create_deck.fill_deck() #create cards in the deck
        create_deck.shuffle_deck() #shuffle cards in the deck
        create_deck.distribute(self.players) # Distribute the cards of the Deck to the players.
