from Cards import *
import unittest


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card(' 1', 'H')
        self.card_2 = Card('11', 'C')

    def testcard(self):
        '''Test the initialization of Card class'''
        self.assertEqual(self.card_1.s, 'H')
        self.assertEqual(self.card_2.s, 'C')
        self.assertEqual(self.card_1.r, ' 1')
        self.assertEqual(self.card_2.r, ' J')

    def test_get_rank(self):
        '''Test get_rank function'''
        self.assertEqual(self.card_1.get_rank(), ' 1')
        self.assertEqual(self.card_2.get_rank(), ' J')

    def test_get_suit(self):
        '''Test get_suit function'''
        self.assertEqual(self.card_1.get_suit(), 'H')
        self.assertEqual(self.card_2.get_suit(), 'C')


class TestDeck(unittest.TestCase):

    def setUp(self):
        self.Deck_1 = Deck()

    def testDeckinit(self):
        '''Test initialization of Deck class'''
        self.assertEqual(len(self.Deck_1.get_deck()), 52)
        self.assertEqual(self.Deck_1.get_deck()[0].r, ' A')
        self.assertEqual(self.Deck_1.get_deck()[12].r, ' K')
        self.assertEqual(self.Deck_1.get_deck()[14].r, ' 2')
        self.assertEqual(self.Deck_1.get_deck()[0].s, 'C')
        self.assertEqual(self.Deck_1.get_deck()[14].s, 'H')

    def testShuffle(self):
        '''Test shuffle function'''
        deck_2 = self.Deck_1.get_deck()[:]
        self.Deck_1.shuffle()
        self.assertNotEqual(deck_2, self.Deck_1.get_deck())
        deck_3 = self.Deck_1.get_deck()[:]
        self.Deck_1.shuffle()
        self.assertNotEqual(deck_3, self.Deck_1.get_deck())

    def testDeal(self):
        '''Test Deal Function'''
        card1 = self.Deck_1.get_deck()[-1]
        card2 = self.Deck_1.get_deck()[-2]
        self.assertEqual(self.Deck_1.deal(), card1)
        self.assertEqual(len(self.Deck_1.get_deck()), 51)
        self.assertEqual(self.Deck_1.deal(), card2)


unittest.main()
