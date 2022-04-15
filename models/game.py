from models.player import Player

class Game:
    def play_round(self):
        if self.player1.choice == "Rock":
            if self.player2.choice == "Scissors":
                return f"{self.player1.name} wins by playing Rock."
