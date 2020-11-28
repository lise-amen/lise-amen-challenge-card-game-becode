
# game.py
from utils.player import Player

from utils.player import Deck

from utils.game import Board


if __name__ == "__main__":

    dictionnary_card = {'A ♥' : 14, '2 ♥' : 2, '3 ♥' : 3, '4 ♥' : 4, '5 ♥' : 5, '6 ♥' : 6, '7 ♥' : 7, '8 ♥' : 8, '9 ♥' : 9, '10 ♥' : 10,
     'J ♥' : 11, 'Q ♥' : 12, 'K ♥' : 13, 'A ♦' : 14, '2 ♦' : 2, '3 ♦' : 3, '4 ♦' : 4, '5 ♦' : 5, '6 ♦' : 6, '7 ♦' : 7, '8 ♦' : 8, '9 ♦' : 9,
     '10 ♦' : 10, 'J ♦' : 11, 'Q ♦' : 12, 'K ♦' : 13, 'A ♣' : 15, '2 ♣' : 2, '3 ♣' : 3, '4 ♣' : 4, '5 ♣' : 5, '6 ♣' : 6, '7 ♣' : 7, '8 ♣' : 8, 
     '9 ♣' : 9, '10 ♣' : 10, 'J ♣' : 11, 'Q ♣' : 12, 'K ♣' : 13, 'A ♠' : 14, '2 ♠' : 2, '3 ♠' : 3, '4 ♠' : 4, '5 ♠' : 5, '6 ♠' : 6, '7 ♠' : 7, 
     '8 ♠' : 8, '9 ♠' : 9, '10 ♠' : 10, 'J ♠' : 11, 'Q ♠' : 12, 'K ♠' : 13}

    name_players = ['J1','J2']

    create_board = Board(name_players) #création de l'objet create_board dans la classe board

    create_deck = Deck() #create create_deck in the deck class
    create_deck.fill_deck() #call method fill_deck to generate the card game
    create_deck.shuffle_deck() #call the method shuffle_deck to shuffle the card game

    create_deck.distribute(create_board.players)

    best_card = 0

    for i in range(26) :
        for i in range(len(name_players)) : 
            create_board.players[i].play() #call the method play for the player number
            value_card = create_board.players[i].play_card 
            if dictionnary_card[value_card] > best_card :
                best_card = dictionnary_card[value_card] 
        print('the player who play', best_card, 'win the turn !') 
        best_card = 0   
    
     
