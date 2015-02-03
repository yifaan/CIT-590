import random

deck = []
discard = []


def shuffle():
    global deck
    global discard
    discard = []
    deck = range(1, 61)
    random.shuffle(deck)


def check_racko(rack):
    for i in xrange(0, 9):
        if rack[i] < rack[i + 1]:
            return False
    return True


def deal_card():
    global deck
    return deck.pop()


def deal_initial_hand():
    global deck
    computer_hand = []
    human_hand = []
    for i in xrange(0, 10):
        computer_hand.append(deck.pop())
        human_hand.append(deck.pop())
    return (computer_hand, human_hand)


def does_user_begin():
    if random.choice(['head', 'tail']) == 'head':
        return True
    else:
        return False


def print_top_to_bottom(rack):
    print 'This is your rack'
    for i in xrange(0, len(rack)):
        print rack[i]


# determine whether card is in hand
def card_in_hand(number, hand):
    for i in xrange(0, len(hand)):
        if hand[i] == number:
            return True
    return False


def find_and_replace(newCard, cardToBeReplaced, hand):
    add_card_to_discard(cardToBeReplaced)
    hand[hand.index(cardToBeReplaced)] = newCard
    return hand


def draw_card_from_discard():
    global discard
    return discard.pop()


def add_card_to_discard(card):
    global discard
    discard.append(card)


def computer_play(hand):
    global deck
    global discard

    # print_top_to_bottom(hand)

    if len(discard) != 0:
        discard_index = 9 - (discard[-1] - 1) / 6

        if (hand[discard_index] - 1) / 6 != 9-discard_index:
            # print 'discard_draw'
            # print discard_index
            card_draw = draw_card_from_discard()
            hand = find_and_replace(card_draw, hand[discard_index], hand)
        else:
            card_draw = deal_card()
            deck_index = 9 - (card_draw - 1) / 6

            if (hand[deck_index] - 1) / 6 != 9 - deck_index:
                hand = find_and_replace(card_draw, hand[deck_index], hand)
                # print 'deck_draw'
                # print deck_index
            else:
                add_card_to_discard(card_draw)
    else:
        card_draw = deal_card()
        deck_index = 9 - (card_draw - 1) / 6

        if (hand[deck_index] - 1) / 6 != 9 - deck_index:
            hand = find_and_replace(card_draw, hand[deck_index], hand)
            # print 'deck_draw'
            # print deck_index
        else:
            add_card_to_discard(card_draw)

    if len(deck) == 0:
        shuffle()

    # print_top_to_bottom(hand)
    return hand


def main():
    global deck
    global discard
    shuffle()
    computer_hand, human_hand = deal_initial_hand()
    userStarts = does_user_begin()

    if userStarts:
        print 'User play first!!!'
    else:
        print 'computer play first'

    while 1:
        if not userStarts:
            print 'computer_playing'
            computer_hand = computer_play(computer_hand)
            if check_racko(computer_hand):
                break

        print_top_to_bottom(human_hand)
        if len(discard) != 0:
            discard_top = discard[-1]
            print 'the card on the top of discard pile is', discard_top
            choose_discard = raw_input(
                'input y to take it or n to draw from deck\n')

            if choose_discard == 'y':
                new_card = draw_card_from_discard
            else:
                new_card = deal_card()
        else:
            print('The discard pile is empty, you will draw card from deck\n')
            new_card = deal_card()

        print 'The card you get is', new_card

        card_to_be_replaced = input(
            '\nInput which card you want to replace it with \ninput 0 to discard this card\n')

        while not card_in_hand(card_to_be_replaced, human_hand)\
                and card_to_be_replaced != 0:
            card_to_be_replaced = input(
                'card is not in your hand, please choose another one\n')

        if card_to_be_replaced == 0:
            add_card_to_discard(new_card)
        else:
            human_hand = find_and_replace(
                new_card, card_to_be_replaced, human_hand)

        if len(deck) == 0:
            shuffle()

        if check_racko(human_hand):
            break

        if userStarts:
            print 'computer_playing'
            computer_hand = computer_play(computer_hand)
            if check_racko(computer_hand):
                break

    print 'Racko'
    if check_racko(computer_hand):
        print 'Computer win!!!'
        print 'computer hand is', computer_hand
    else:
        print 'You win'

    print 'game over'

if __name__ == '__main__':
    main()
