from Cards import *


class Blackjack(object):

    def __init__(self):
        '''initialize deck, Table and discard'''
        self.Gamedeck = Deck()
        self.Gamedeck.shuffle()
        self.Table = {}
        self.Table['row1'] = ['  1', '  2', '  3', '  4', '  5']
        self.Table['row2'] = ['  6', '  7', '  8', '  9', ' 10']
        self.Table['row3'] = [' 11', ' 12', ' 13']
        self.Table['row4'] = [' 14', ' 15', ' 16']
        self.Table['availability'] = [0] * 16
        self.discardList = ['[ ]', '[ ]', '[ ]', '[ ]']
        self.discard_number = 0
        self.table_number = 0
        self.dealcard = self.Gamedeck.deal()

    def Deal(self):
        '''Deal card'''
        self.dealcard = self.Gamedeck.deal()

    def Discard_card(self):
        '''Put deal card into discard, and deal card'''
        if self.discard_number != 4:
            self.discardList[self.discard_number] = str(self.dealcard)
            self.discard_number += 1
            self.Deal()
        else:
            raise ValueError('full')

    def check_availabitity(self, number):
        '''0check whether a position in table is available'''
        if self.Table['availability'][number - 1] == 0:
            return True
        else:
            return False

    def check_user_input(self, user_input):
        '''test whether a user_input is valid'''
        if user_input >= 1 and user_input <= 16:
            if self.check_availabitity(user_input):
                return True
            else:
                print 'The position already has a card'
                return False
        else:
            print 'If discard is full, number must within 1 to 16'
            return False

    def put_card_to_table(self, number):
        '''Put card into the table follow use instruction and deal card'''
        row_num = ''
        if number <= 5:
            row_num = 'row1'
            position = number - 1
        elif number <= 10:
            row_num = 'row2'
            position = number - 6
        elif number <= 13:
            row_num = 'row3'
            position = number - 11
        elif number <= 16:
            row_num = 'row4'
            position = number - 14
        self.Table[row_num][position] = str(self.dealcard)
        self.table_number += 1
        self.Table['availability'][number - 1] = 1
        self.Deal()

    def ask_user_input(self):
        '''ask user to decide where to put the card'''
        user_input = []
        while user_input == [] or user_input > 16 or user_input < 0:
            try:
                user_input = input(
                    'choose which position you want put in table, \
input 0 to discard\t')
                if user_input >= 0 and user_input <= 16:
                    return user_input
                else:
                    raise NameError
            except NameError:
                print 'Numbers need to be within 0 to 16'
            except SyntaxError:
                pass

    def check_discard_full(self):
        '''Check whether discard is full'''
        if self.discard_number == 4:
            return True
        else:
            return False

    def get_sum(self, lst):
        '''Get sum from a list of card'''
        sum_of_list = 0
        Ace = False
        for num in lst:
            if num[0:2] == ' J' or num[0:2] == ' Q' or num[0:2] == ' K':
                num = '10'
            elif num[0:2] == ' A':
                num = ' 1'
                Ace = True
            sum_of_list += int(num[0:2])
        if Ace and sum_of_list <= 11:
            sum_of_list += 10
        return sum_of_list

    def get_score(self, lst):
        '''Get score for each lst of cards'''
        lenth = len(lst)
        sum_of_list = self.get_sum(lst)

        if sum_of_list > 21:
            score = 0
        elif sum_of_list == 21:
            if lenth == 2:
                score = 10
            else:
                score = 7
        elif sum_of_list == 20:
            score = 5
        elif sum_of_list == 19:
            score = 4
        elif sum_of_list == 18:
            score = 3
        elif sum_of_list == 17:
            score = 2
        else:
            score = 1
        return score

    def get_tot_score(self):
        '''Get the total score'''
        self.row1_score = self.get_score(self.Table['row1'])
        self.row2_score = self.get_score(self.Table['row2'])
        self.row3_score = self.get_score(self.Table['row3'])
        self.row4_score = self.get_score(self.Table['row4'])
        col1 = [self.Table['row1'][0], self.Table['row2'][0]]
        col2 = [self.Table['row1'][1], self.Table['row2'][1],
                self.Table['row3'][0], self.Table['row4'][0]]
        col3 = [self.Table['row1'][2], self.Table['row2'][2],
                self.Table['row3'][1], self.Table['row4'][1]]
        col4 = [self.Table['row1'][3], self.Table['row2'][3],
                self.Table['row3'][2], self.Table['row4'][2]]
        col5 = [self.Table['row1'][4], self.Table['row2'][4]]
        self.col1_score = self.get_score(col1)
        self.col2_score = self.get_score(col2)
        self.col3_score = self.get_score(col3)
        self.col4_score = self.get_score(col4)
        self.col5_score = self.get_score(col5)
        tot_score = self.row1_score + self.row2_score + \
            self.row3_score + self.row4_score + self.col1_score + \
            self.col2_score + self.col3_score + \
            self.col4_score + self.col5_score
        return tot_score

    def check_high_score(self, new_score):
        f = open('highScore.txt', 'r+')
        original_score = int(f.readline())
        f.seek(0)
        if new_score > original_score:
            f.writelines(str(new_score))
            print '\nBest Score!!! Congrats!!!'

    def play(self):
        '''Play the game'''
        while self.table_number != 16:
            print self
            user_input = ''
            if self.check_discard_full():
                while not self.check_user_input(user_input):
                    user_input = self.ask_user_input()
                self.put_card_to_table(user_input)
            else:
                while not self.check_user_input(user_input) and user_input != 0:
                    user_input = self.ask_user_input()
                if user_input == 0:
                    self.Discard_card()
                else:
                    self.put_card_to_table(user_input)
        print self
        new_score = self.get_tot_score()
        self.check_high_score(new_score)
        print 'Your score is', new_score

    def __str__(self):
        discard_1 = '\t'.join(self.discardList[0:2])
        discard_2 = '\t'.join(self.discardList[2:4])
        tablestring = '\nThe current Table, Discard and dealcard are\n'
        tablestring += '\t' * 2 + 'Table' + '\t' * 4 + \
            'Discard' + '\t' * 2 + 'Dealcard' + '\n'
        tablestring += '\t'.join(self.Table['row1']) + '\t' * \
            2 + discard_1 + '\t' + str(self.dealcard) + '\n'
        tablestring += '\t'.join(self.Table['row2']
                                 ) + '\t' * 2 + discard_2 + '\n'
        tablestring += '\t' + \
            '\t'.join(self.Table['row3']) + '\n'
        tablestring += '\t' + \
            '\t'.join(self.Table['row4']) + '\n'
        return tablestring


def main():
    bj_solitaire = Blackjack()
    bj_solitaire.play()


if __name__ == '__main__':
    main()
