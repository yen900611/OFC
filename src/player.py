class Player():
    def __init__(self, id):
        self.card = {"top row":[],
                     "middle row":[],
                     "bottom row":[]}
        self.new_card = []
        self.id = id

    def update(self):
        self.deal_card()

    def deal_card(self):
        while self.new_card:
            print(self.new_card)
            print(self.new_card[-1])
            place = input("This card is for player"+str(self.id+1)+":")
            if place == ("t" or "T"):
                if len(self.card["top row"])<3:
                    self.card["top row"].append(self.new_card[-1])
                else:
                    print("Top row is full.")
                    continue
            elif place == ("m" or "M"):
                if len(self.card["middle row"])<5:
                    self.card["middle row"].append(self.new_card[-1])
                else:
                    print("Middle row is full.")
                    continue
            elif place == ("b" or "B"):
                if len(self.card["bottom row"])<5:
                    self.card["bottom row"].append(self.new_card[-1])
                else:
                    print("Bottom row is full.")
                    continue
            else:
                print("Unknown input.Please type 't', 'm' or 'b'.")
                continue
            self.new_card.pop()
        self.show_card()

    def show_card(self):
        for i in self.card:
            for j in self.card[i]:
                print(j, end=", ")
            print("\b\b\n")