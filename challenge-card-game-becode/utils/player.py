# player.py
from card import Card

from card import Symbol

import random

class Player():
    """ Player defining the game intructions characterized by :
        - a player name
        - a list of card
        - a count
        - a number of cards
        - a history """

    def __init__(self, name : str) :
        self.name = name
        self.cards = list()
        self.turn_count = 0
        self.card_number = 0
        self.history = list()

    def play(self):
        play_card = random.choice(self.cards)  # pick a card randomly in cards
        print(play_card)
        self.cards.remove(play_card) # remove the pick card
        print(self.cards)
        self.history.append(play_card) # add the card played in the history
        print(self.name[0],"turn number" ,self.turn_count,"played:", play_card)
        #return the Card


class Deck():

    def __init__(self):
        self.cards = list() #contain a list of instances of Cards

    #generate the card game
    def fill_deck(self) :
        for i in Symbol.icon_card :
            for j in Card.value_card :
                self.cards.append(j+ ' ' + i)

    #shuffle all the Card instances of cards
    def shuffle_deck(self) :
        random.shuffle(self.cards) #mélanger les cartes du dek

    #distribute the cards evenly between all the players.
    def distribute(self, players : list) :
        step = len(self.cards)//len(players)
        i=0
        for player in players :
            player.cards.extend(self.cards[i*step:step*(i+1)])
            i+=1
            print(player.cards)
            print(player.name)
