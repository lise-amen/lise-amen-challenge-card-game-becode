
# game.py
from utils.player import Player

from utils.player import Deck

from utils.game import Board


if __name__ == "__main__":

    name_players = ['J1','J2']

    create_board = Board(name_players) #création de l'objet create_board dans la classe board

    create_deck = Deck() #create create_deck in the deck class
    create_deck.fill_deck() #call method fill_deck to generate the card game
    create_deck.shuffle_deck() #call the method shuffle_deck to shuffle the card game

    #print(create_deck.cards)

    #print(create_board.players[0].name)
    #print(create_board.players[1].name)

    create_deck.distribute(create_board.players)

    for i in range(26) :
        for i in range(len(name_players)) : 
            create_board.players[i].play() #call the method play for the player number
            
    
     

print("my card", create_board.players[0].play_card)