from models.player import Player

class Game:
    def __init__(self, input_player1, input_player2):
        self.player1 = Player(input_player1)
        self.player2 = Player(input_player2)