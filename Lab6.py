import random
import itertools
def make_deck():
    suit = 'HSDC'
    rank = 'A23456789XJQK'
    deck = [''.join(card) for card in itertools.product(rank, suit)]
    return deck
deck = make_deck()
random.shuffle(deck)
def deal_cards(deck, players):
    hands = []
    for m in range(players):
        playercards = []
        for n in range(4):
            cards = deck.pop(0)
            playercards.append(cards)
        hands.append(playercards)
    return hands
print(deal_cards(deck, 13))



