import random as rd
from operator import itemgetter
import numpy as np


class Guandan:
    def __init__(self):
        self.deck = list(range(1,55))*2
        self.p = []

    def shuffle(self):
        rd.shuffle(self.deck)

    def draw(self):
        for i in range(4):
            self.p.append(self.deck[i*27+1:i*27+28])

    def decode(self, card_code):
        if card_code <= 13:
            suit = 's' #Spades
            rank = card_code
        elif card_code > 13 and card_code <= 26:
            suit = 'c' #Clubs
            rank = card_code - 13
        elif card_code > 26 and card_code <= 39:
            suit = 'h' #Hearts
            rank = card_code - 26
        elif card_code > 39 and card_code <= 52:
            suit = 'd' #Diamonds
            rank = card_code - 39
        elif card_code == 53:
            suit = 'j'
            rank = card_code
        else:
            suit = 'J'
            rank = card_code
        if rank == 1:
            rank = 13.5
        return rank, suit

    def read(self, n):
        hand = []
        hand_raw = self.p[n]
        for card in hand_raw:
            rank, suit = self.decode(card)
            hand.append([rank, suit])
        hand.sort(key=itemgetter(0))
        for index, card in enumerate(hand):
            if card[0] == 13.5:
                card[0] = 'A'
            elif card[0] == 11:
                card[0] = 'J'
            elif card[0] == 12:
                card[0] = 'Q'
            elif card[0] == 13:
                card[0] = 'K'
            if card[1] == 'j':
                hand[index] = ['joker']*2
            elif card[1] == 'J':
                hand[index] = ['JOKER']*2
        hand_1 = []
        for card in hand:
            hand_1.append(card[0])
            hand_1.append(card[1])
        hand = np.array(hand_1).reshape(-1, 2)
        hand = np.transpose(hand)
        print(hand)





if __name__ == '__main__':
    trial = Guandan()
    trial.shuffle()
    trial.draw()
    trial.read(1)
