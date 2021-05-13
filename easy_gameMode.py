import random

from setting import *

class OFC_easy():
    def __init__(self):
        self.all_cards = set()
        for suit in SUIT:
            for number in NUMBER:
                self.all_cards.add(suit + number)
        self.showed_cards = set()

    def distribute(self):
        if len(self.showed_cards) == 0:
            for i in range(5):
                card = random.choice(list(self.all_cards - self.showed_cards))
                self.showed_cards.add(card)
                print(card)
        else:
            card = random.choice(list(self.all_cards - self.showed_cards))
            self.showed_cards.add(card)
            print(card)

if __name__ == "__main__":
    game = OFC_easy()
    for i in range(9):
        game.distribute()
    print(game.showed_cards)
