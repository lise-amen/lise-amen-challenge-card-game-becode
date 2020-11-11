# card.py

class Symbol():
    """ Symbol defining a card characterized by :
        - a color
        - a icon """

    icon_card = ['♥', '♦', '♣', '♠'] #attribut from Symbol class
    color_card = ['black','red'] #attribut from Symbol class

class Card(Symbol): # class Card inherits from Symbol
    """ Card defining value' card"""

    value_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] #attribut from Card class
