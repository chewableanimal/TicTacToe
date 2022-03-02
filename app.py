from flask import Flask, redirect, render_template, url_for, redirect
from gamefile import *

app = Flask(__name__)
if __name__ == "__main__":
    app.debug = True
    

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/newgame")
def new_game():
    global turn
    turn = True
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    return redirect(url_for("home"))

@app.route("/singleplayer")
def run_single():
    global turn
    if gameOver(board) or boardFull(board):
        return redirect(url_for("game_over"))

    return render_template("single_player.html", isMax=turn, game=board)

@app.route("/multiplayer")
def run_game():
    
    if gameOver(board) or boardFull(board):
        return redirect(url_for("game_over"))

    return render_template("multi_player.html", game=board)

@app.route("/gameover")
def game_over():
    if gameOver(board) and turn == False:
        return render_template("game_over.html",gameWon=1,game=board)
    elif gameOver(board) and turn == True:    
        return render_template("game_over.html",gameWon=0,game=board)

    return render_template("game_over.html", gameWon=-1,game=board)


    

@app.route("/play/<int:row>/<int:col>")
def get(row, col):
    global board
    global turn
    if turn == True:
        board[row][col] = "X"
    else:
        board[row][col] = "O"

    turn = updateTurn(turn)

    return redirect(url_for("run_game"))

@app.route("/play2/<int:row>/<int:col>")
def getSingle(row, col): 
    global board
    global turn
    if turn == False:
        aiRow, aiCol = getAI(turn, board)
        board[aiRow][aiCol] = "O"
    else:
        board[row][col] = "X"

    turn = updateTurn(turn)

    return redirect(url_for("run_single"))

# def getAi(board, turn):
#     aiRow, aiCol = getAI(turn, board)
#     board[aiRow][aiCol] = "O"
#     turn = updateTurn()
    
