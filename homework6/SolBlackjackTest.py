from SolBlackjack import *
import unittest


class TestSolBlackjack(unittest.TestCase):

    def setUp(self):
        self.BJ = Blackjack()

    def testinit(self):
        '''test initialization of blackjack class'''
        self.assertEqual(len(self.BJ.Gamedeck.get_deck()), 51)
        self.assertEqual(
            self.BJ.Table['row1'], ['  1', '  2', '  3', '  4', '  5'])
        self.assertEqual(self.BJ.discardList, ['[ ]', '[ ]', '[ ]', '[ ]'])

    def testDeal(self):
        '''Test deal function'''
        card = self.BJ.Gamedeck.get_deck()[-1]
        self.BJ.Deal()
        self.assertEqual(card, self.BJ.dealcard)
        card = self.BJ.Gamedeck.get_deck()[-1]
        self.BJ.Deal()
        self.assertEqual(card, self.BJ.dealcard)

    def testDiscardcard(self):
        '''Test discardcard function'''
        card = self.BJ.dealcard
        self.BJ.Discard_card()
        self.assertEqual(str(card), self.BJ.discardList[0])
        self.BJ.discard_number = 4
        with self.assertRaises(ValueError):
            self.BJ.Discard_card()

    def testcheck_availability(self):
        '''test check_availability function'''
        self.assertTrue(self.BJ.check_availabitity(1))
        self.BJ.Table['availability'][0] = 1
        self.assertFalse(self.BJ.check_availabitity(1))

    def testcheck_user_input(self):
        '''test check_user_input function'''
        self.assertTrue(self.BJ.check_user_input(1))
        self.assertFalse(self.BJ.check_user_input(17))
        self.BJ.Table['availability'][0] = 1
        self.assertFalse(self.BJ.check_user_input(1))

    def testput_card_to_table(self):
        '''test put card to table function'''
        card1 = str(self.BJ.dealcard)
        self.BJ.put_card_to_table(12)
        self.assertEqual(card1, self.BJ.Table['row3'][1])
        card2 = str(self.BJ.dealcard)
        self.BJ.put_card_to_table(1)
        self.assertEqual(card2, self.BJ.Table['row1'][0])

    def testcheck_discard_full(self):
        '''test check discard full function'''
        self.assertFalse(self.BJ.check_discard_full())
        self.BJ.discard_number = 4
        self.assertTrue(self.BJ.check_discard_full())

    def testget_sum(self):
        '''Test get sum function'''
        lst = [' AC', '10S', ' QS', ' JH']
        self.assertEqual(self.BJ.get_sum(lst), 31)
        lst1 = [' AC', ' 5H']
        self.assertEqual(self.BJ.get_sum(lst1), 16)
        lst2 = []
        self.assertEquals(self.BJ.get_sum(lst2), 0)

    def testget_score(self):
        '''test get_score function'''
        lst = [' AC', '10S', ' QS', ' JH']
        self.assertEqual(self.BJ.get_score(lst), 0)
        lst1 = [' AC', ' QS']
        self.assertEqual(self.BJ.get_score(lst1), 10)
        lst1 = [' AC', ' 8S']
        self.assertEqual(self.BJ.get_score(lst1), 4)
        lst1 = [' 7C', ' 8S', ' 6D']
        self.assertEqual(self.BJ.get_score(lst1), 7)

    def testget_tot_score(self):
        '''test get_tot_score function'''
        self.BJ.Table['row1'] = [' AC', '10S', ' QS', ' JH', ' 5C']
        self.BJ.Table['row2'] = [' 3C', ' 7S', ' 2S', ' 5H', ' AH']
        self.BJ.Table['row3'] = [' 7C', ' 8S', ' 6D']
        self.BJ.Table['row4'] = [' 3C', ' 4S', ' AD']
        tot_score = self.BJ.get_tot_score()
        self.assertEquals(self.BJ.row1_score, 0)
        self.assertEquals(self.BJ.row2_score, 3)
        self.assertEquals(self.BJ.row3_score, 7)
        self.assertEquals(self.BJ.row4_score, 3)
        self.assertEquals(self.BJ.col1_score, 1)
        self.assertEquals(self.BJ.col2_score, 0)
        self.assertEquals(self.BJ.col3_score, 0)
        self.assertEquals(self.BJ.col4_score, 0)
        self.assertEquals(self.BJ.col5_score, 1)
        self.assertEquals(tot_score, 15)


unittest.main()
