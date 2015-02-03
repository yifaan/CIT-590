import random

deck = []
discard = []


def shuffle():
    global deck
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


def add_card_to_discard(card):
    global discard
    discard.append(card)


def computer_play(hand):
    return hand


def main():
    global deck
    global discard
    shuffle()
    computer_hand, human_hand = deal_initial_hand()
    userStarts = does_user_begin()
    print_top_to_bottom(human_hand)

    while not check_racko(human_hand) and not check_racko(computer_hand):
        computer_hand = computer_play(computer_hand)

        if len(discard) == 0:
            pass


if __name__ == '__main__':
    main()
