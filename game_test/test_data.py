CARD_VALUE = {
    "2":2,
    '3':3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}
def scoring_top_raw(cards:list):
    if len(cards) != 3:
        raise ValueError
    card_value = []
    for card in cards:
        card_value.append(CARD_VALUE[card[1]])
    if card_value.count(card_value[0]) == 3:
        return card_value[0] + 8
    elif card_value.count(card_value[0]) == 2:
        return card_value[0] - 5
    elif card_value.count(card_value[1]) == 2:
        return card_value[1] - 5
    else:
        return 0

def scoring_middle_raw(cards:list):
    if len(cards) != 5:
        raise ValueError
    card_suit = []
    card_value = []
    for card in cards:
        card_suit.append(card[0])
        card_value.append(CARD_VALUE[card[1]])
    if card_suit.count(card_suit[0]) == 5: # FLUSH
        card_value.sort(reverse = True)
        for i in range(len(card_value)-1):
            if card_value[i] - card_value[i +1] == 1:
                continue #TODO #A2345
            else:
                return 8
        if card_value[0] == 14:
            return 50
        else:
            return 30
    else:
        for i in range(len(card_value)):
            count = card_value.count(card_value[i])
            if count == 4:
                value = card_value[i]
                return 20
            elif count == 3:
                value = card_value[i]
                for c in card_value:
                    if c != value:
                        if card_value.count(c) == 2:
                            return 12
                        else:
                            return 2

        card_value.sort(reverse=True)
        for i in range(len(card_value) - 1):
            if card_value[i] - card_value[i + 1] == 1:
                continue
            else:
                return 0
        return 4

def sort_cards(cards:list):# Done
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

def is_royal_flush(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_suit = []
    card_value = []
    for card in cards:
        card_suit.append(card[0])
        card_value.append(CARD_VALUE[card[1]])

    if card_suit.count(card_suit[0]) == 5: # FLUSH
        if sum(card_value) == 60:
            return True
        else:
            return False
    else:
        return False


def is_straight_flush(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_suit = []
    card_value = []
    for card in cards:
        card_suit.append(card[0])
        card_value.append(CARD_VALUE[card[1]])

    if card_suit.count(card_suit[0]) == 5:  # FLUSH
        card_value.sort(reverse = True)
        if card_value[0] == 14:
            for i in range(1, len(card_value)-1):
                if card_value[i] + i == 6:
                    continue
                else:
                    return False
            return True
        for i in range(len(card_value)-1):
            if card_value[i] - card_value[i + 1] == 1:
                continue
            else:
                return False
        return True
    else:
        return False


def is_four_of_a_kind(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_value = []
    for card in cards:
        card_value.append(CARD_VALUE[card[1]])

    if card_value.count(card_value[0]) == 4 or card_value.count(card_value[1]) == 4:
        return True
    return False

def is_full_house(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_value = []
    for card in cards:
        card_value.append(CARD_VALUE[card[1]])

    if card_value.count(card_value[0]) == 3 and card_value.count(card_value[3]) == 2:
        return True
    elif card_value.count(card_value[0]) == 2 and card_value.count(card_value[1]) == 3:
        return True
    return False

def is_flush(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_suit = []
    for card in cards:
        card_suit.append(card[0])
    if card_suit.count(card_suit[0]) == 5:
        return True
    else:
        return False

def is_straight(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_suit = []
    card_value = []
    for card in cards:
        card_suit.append(card[0])
        card_value.append(CARD_VALUE[card[1]])

    if card_suit.count(card_suit[0]) != 5:  # not FLUSH
        card_value.sort(reverse = True)
        if card_value[0] == 14:
            for i in range(1, len(card_value)-1):
                if card_value[i] + i == 6:
                    continue
                else:
                    return False
            return True
        for i in range(len(card_value)-1):
            if card_value[i] - card_value[i + 1] == 1:
                continue
            else:
                return False
        return True
    else:
        return False

def is_three_of_a_kind(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_value = []
    for card in cards:
        card_value.append(CARD_VALUE[card[1]])
    for i in range(3):
        if card_value.count(card_value[i]) == 3:
            return True
        else:
            continue
    return False

def is_double_pairs(cards:list):
    if len(cards) != 5:
        raise ValueError
    cards = sort_cards(cards)
    card_value = []
    for card in cards:
        card_value.append(CARD_VALUE[card[1]])
    x = 0
    for i in range(0, 5, 2):
        x += card_value.count(card_value[i])
    if x == 5:
        return True
    return False