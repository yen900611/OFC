import random

from .setting import *
from .player import Player

class OFC_easy():
    '''
    2 player
    no fantasy land
    single card per time
    rank by personal score
    '''
    def __init__(self):
        self.all_cards = []
        for suit in SUIT:
            for number in NUMBER:
                self.all_cards.append(suit + number)
        self.unshowed_cards = self.all_cards.copy()
        self.showed_cards = []
        self.p1 = Player(0)
        self.p2 = Player(1)
        self.deal_times = 0
        self.is_running = True

    def update(self):
        if self.deal_times == 0:
            self.deal(self.p1.new_card, 5)
            self.deal(self.p2.new_card, 5)
        elif self.deal_times < 9:
            self.deal(self.p1.new_card, 1)
            self.deal(self.p2.new_card, 1)
        else:
            self.is_running = False
        self.deal_times += 1
        self.p1.update()
        self.p2.update()

    def is_Running(self):
        return self.is_running



    def deal(self, hands:list, num):
        for i in range(num):
            card = random.choice(list(self.unshowed_cards))
            hands.append(card)
            self.showed_cards.append(card)
            self.unshowed_cards.remove(card)
        self.showed_cards = self.sort_cards(self.showed_cards)

    def sort_cards(self, cards: list):
        """
        把牌根據數字由大排到小，不檢查張數。
        :param cards: list
        :return: list
        """
        card_value = []
        result = []
        for card in cards:
            card_value.append(CARD_VALUE[card[1]])
        for i in sorted(card_value, reverse=True):
            for c in cards:
                if CARD_VALUE[c[1]] == i:
                    result.append(c)
                    cards.remove(c)
                    break
        return result

if __name__ == "__main__":
    game = OFC_easy()
    game.p1.card = {
        "top row": ["DK", "CK", "D2"],
        "middle row": ["SQ", "HJ", "ST", "D9", "D8"],
        "bottom row": ["D8", "D6", "C6", "C5", "C4"]
    }
    game.p1.show_card()
#     game.deal(5)
#     for i in range(8):
#         game.deal(1)
#     print(game.showed_cards)
