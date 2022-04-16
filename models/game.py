class Game:
    def play_round(self, player1, player2):
        player1.choice = player1.choice.lower()
        player2.choice = player2.choice.lower()

        if player1.choice == player2.choice:
            return None
        elif player1.choice == "rock":
            if player2.choice == "paper":
                return f"{player1.name} wins by playing Rock."
            else:
                return f"{player2.name} wins by playing Paper."
        elif player1.choice == "paper":
            if player2.choice == "rock":
                return f"{player1.name} wins by playing Paper."
            else:
                return f"{player2.name} wins by playing Scissors."
        elif player1.choice == "scissors":
            if player2.choice == "paper":
                return f"{player1.name} wins by playing Scissors."
            else:
                return f"{player2.name} wins by playing Rock."