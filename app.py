from flask import Flask, render_template, request, redirect, url_for
from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax

app = Flask(__name__)

# Initialize the game board
board = initial_state()
game_over = False

@app.route("/")
def index():
    global board, game_over
    if terminal(board):
        game_over = True
    return render_template("index.html", board=board, game_over=game_over, winner=winner(board))

@app.route("/move", methods=["POST"])
def move():
    global board, game_over
    if not terminal(board):
        # Get the player's move
        row = int(request.form["row"])
        col = int(request.form["col"])
        action = (row, col)
        if action in actions(board):
            board = result(board, action)
            # AI's move
            if not terminal(board):
                ai_move = minimax(board)
                board = result(board, ai_move)
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    global board, game_over
    board = initial_state()
    game_over = False
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
