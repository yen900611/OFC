from src.easy_gameMode import OFC_easy

if __name__ == "__main__":
    game = OFC_easy()
    while game.is_Running():
        game.update()
    print("player 1:")
    game.p1.show_card()
    print("player 2:")
    game.p2.show_card()