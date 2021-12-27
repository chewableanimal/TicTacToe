import os

#Quick function to clear terminal
def clearScreen():
    os.system('cls' if os.name == "nt" else 'clear')

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


def displayBoard():
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j < 2:
                print(board[i][j] + " |", end= " ")
            else:
                print(board[i][j], end= " ")
        if i < 2:
            print("\n----------")
    print("\n")

#Get input function
def getInput():
    #Get row input
    while True:
        try:
            displayBoard()
            row = int(input("Please enter input for row(choose from 1-3): "))
            clearScreen()
            if row in range(1,4):
                break
        except ValueError:
            clearScreen()
            print("Please enter only numeric values.\n")
            
    #Get column input
    while True:
        try:
            displayBoard()
            print("Current row selection:", row)
            col = int(input("Please enter input for column(choose from 1-3): "))
            clearScreen()
            if col in range(1,4):
                break
        except ValueError:
            clearScreen()
            print("Please enter only numeric values.\n")

    row-= 1
    col-= 1

    if checkBoard(row, col) == False:
        print("Sorry that area has been filled in, please pick an empty spot on the board.\n")
        return getInput()

    return row, col
    

#Create check board function
def checkBoard(row, col):
    global board
    if board[row][col] != " ":
        return False
    return True

def updateBoard(row, col, turn, board):
    if turn == True:
        board[row][col] = "X"
    else:
        board[row][col] = "O"


def updateTurn(turn):
    if turn == True:
        turn = False
    else: 
        turn = True

    return turn

def boardFull(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                return False
    return True

def gameOver(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
            return True  
    else:
        return False

def checkWinner(gameOver, turn):
    displayBoard()
    if gameOver and turn == False:
        print("Game over, X wins!")
    elif gameOver and turn == True:
        print("Game over, O wins!")
    else:
        print("Game over, Tie!")



print("Welcome to Tic Tac Toe!\n")
mode = gameMode()
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
turn = True

#Clear Terminal
clearScreen()

#Singleplayer
if mode == 1:
    displayBoard()

#Multiplayer
elif mode == 2:
    while not boardFull(board) and not gameOver(board):
        row, col = getInput()
        updateBoard(row, col, turn, board)
        turn = updateTurn(turn)

    checkWinner(gameOver(board), turn)
            
else:
    quit()