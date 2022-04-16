from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route("/play")
def home():
    return render_template("play.html.jinja", title = "Rock Paper Scissors")

@app.route("/result", methods=["POST"])
def round():
    # Get info from the players that is collected from the form in the template index
    player1 = Player(request.form["player1_name"], request.form["player1_choice"])
    player2 = Player(request.form["player2_name"], request.form["player2_choice"])

    # Create a new instance of the class Game with the information of the players and store it in the variable result_info    
    # Play a round of the game
    result_info = Game().play_round(player1, player2)

    # Render a new html with the result of the round
    return render_template("result.html.jinja", title = "Game result", result_info = result_info)

@app.route("/")
def welcome():
    return render_template("root.html.jinja", title = "Welcome & Rules")