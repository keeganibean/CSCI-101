import random
import itertools
def make_deck():
    suit = 'HSDC'
    rank = 'A23456789XJQK'
    deck = [''.join(card) for card in itertools.product(suit, rank)]
    return deck
deck = make_deck()
random.Random('HA').shuffle(deck)#extra credit(first card on left is always Ace of Hearts)
#random.shuffle(deck) #not extra credit just regular shuffle
def deal_cards(deck, players):
    hands = []
    for m in range(players):
        playercards = []
        for n in range(4):
            cards = deck.pop(0)
            playercards.append(cards)
        hands.append(playercards)
    return hands
piles=(deal_cards(deck, 13))
def show_deck(dealtdeck, number):
    print('    A  2  3  4  5  6  7  8  9  X  J  Q  K')
    rows=4
    index=0
    card=''
    for index in range(4):
        if piles[number][index] != '    ':
            card = piles[number][index]
            break
    while rows>0:
        print('%d: ' %rows, end='')
        for hand in piles:
            if len(hand)>=rows:
                if hand[index]==card:
                    print(hand[index], end=' ')
                    hand.remove(hand[index])
                else:
                    print('** ', end='')
            else:
                print('   ', end='')
        print('')
        rows -= 1
    return
def main():
    value=12
    kingcount=0
    while kingcount<4:
        for index in range(4):
            if piles[value][index] != '   ':
                card = piles[value][index]
                break
        plays=show_deck(piles, value)
        if card[1]=='K':
            kingcount+=1
            value=12
        elif card[1]=='A':
            value=0
        elif card[1]=='X':
            value=9
        elif card[1]=='J':
            value=10
        elif card[1]=='Q':
            value=11
        elif card[1]=='2':
            value=1
        elif card[1]=='3':
            value=2
        elif card[1]=='4':
            value=3
        elif card[1]=='5':
            value=4
        elif card[1]=='6':
            value=5
        elif card[1]=='7':
            value=6
        elif card[1]=='8':
            value=7
        else:
            value=8
        print('King count: %d' %kingcount)
main()
        
            
    
    
                
                   


