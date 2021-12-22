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

    displayBoard()
    #Get row input
    while True:
        try:
            row = int(input("Please enter input for row(choose from 1-3): "))
            if row in range(1,4):
                break
        except ValueError:
            print("\nPlease enter only numeric values.")
            
    #Get column input
    while True:
        try:
            col = int(input("Please enter input for column(choose from 1-3): "))
            if col in range(1,4):
                break
        except ValueError:
            print("\nPlease enter only numeric values.")

    row-= 1
    col-= 1

    if checkBoard(row, col) == False:
        print("Sorry that area has been filled in, please pick an empty spot on the board.")
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


print("Welcome to Tic Tac Toe!\n")
mode = gameMode()
board = [["X", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
turn = True

os.system('cls' if os.name == "nt" else 'clear')

#Singleplayer
if mode == 1:
    displayBoard(board)

#Multiplayer
elif mode == 2:
    #Place holder before game over functionality is added
    while True:
        row, col = getInput()
        updateBoard(row, col, turn, board)
        turn = updateTurn(turn)
            

    

else:
    quit()