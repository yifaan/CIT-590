import random  # needed for shuffling a Deck


class Card(object):
    # the card has a suit which is one of 'S','C','H' or 'D'
    # the card has a rank

    def __init__(self, r, s):
        # implement
        # where r is the rank, s is suit
        if r == '11':
            r = ' J'
        elif r == '12':
            r = ' Q'
        elif r == '13':
            r = ' K'

        self.r = r
        self.s = s

    def __str__(self):
        return str(self.r) + str(self.s)

    def get_rank(self):
        return self.r

    def get_suit(self):
        return self.s


class Deck(object):

    """Denote a deck to play cards with"""

    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        # correct the code below
        self.__deck = []
        rank = [' A', ' 2', ' 3', ' 4', ' 5', ' 6',
                ' 7', ' 8', ' 9', '10', '11', '12', '13']
        suit = ['C', 'H', 'S', 'D']
        for s in suit:
            for r in rank:
                new_card = Card(r, s)
                self.__deck.append(new_card)

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.__deck)

    def get_deck(self):
        return self.__deck

    def deal(self):
        return self.__deck.pop()

    def __str__(self):
        """Represent the whole deck as a string for printing --
         very useful during code development"""
        deckstring = ''
        for i in self.__deck:
            deckstring += str(i) + '\n'
        return deckstring

       # the deck is a list of cards
       # this function just calls str(card) for each card in list
       # put a '\n' between them
