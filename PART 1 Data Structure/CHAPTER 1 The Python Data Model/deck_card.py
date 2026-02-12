import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


# example 1
deck = FrenchDeck()
print(len(deck))
print(deck[0])


# example 2
from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))


# example 3
print(deck[:3])
print(deck[12::13])


# example 4
for card in deck:
    print(card)

print('\n\n\n\n')

# example 5
for card in reversed(deck):
    print(card)


# example 6
"""
This module defines a function `spades_high` that takes a `Card` object as input and returns an integer
representing the rank of the card in a spades-high deck.

The function first gets the index of the card's rank in the list of ranks defined in the `FrenchDeck` class.
Next, it calculates a suit value by looking up the card's suit in the `suit_values` dictionary.
Finally, it returns the rank value multiplied by the number of suit values (which is 4 in this case)
plus the suit value.

The `suit_values` dictionary maps each suit to an integer value, where the spades have the highest value.
"""

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]




