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
def scoring_top_raw(cards:set):
    if len(cards) != 3:
        raise ValueError
    # print(cards)
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

# TODO #每種牌型都做成Function

def scoring_middle_raw(cards:set):
    print(cards)
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
