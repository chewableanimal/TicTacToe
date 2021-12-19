import os

#Select Game Mode
def gameMode():
    try:
        modeSelect = int(input("Enter 1 for single player, 2 for multiplayer, or 3 to exit: "))

        if modeSelect != 1 and modeSelect != 2 and modeSelect != 3: 
            return gameMode()
        else:
            return modeSelect

    except ValueError:
        print("\nPlease enter only numeric values.")
        return gameMode()


def displayBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j < 2:
                print(board[i][j] + " |", end= " ")
            else:
                print(board[i][j], end= " ")
        if i < 2:
            print("\n----------")
    print("\n")
        

def updateTurn(turn):
    if turn == True:
        turn = False
    else: 
        turn = True


print("Welcome to Tic Tac Toe!\n")
mode = gameMode()
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

os.system('cls' if os.name == "nt" else 'clear')

if mode == 1:
    displayBoard(board)

elif mode == 2:
    displayBoard(board)

else:
    quit()