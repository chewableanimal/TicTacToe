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

#Used to display the current state of the board
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

#Receives the input from both the users and the AI if in singleplayer
def getInput(mode, turn):

    #Handles AI input
    if mode == 1 and turn == False:
          return getAI(turn)


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

    #Outputs error to user and asks for new input if space is not empty
    if checkBoard(row, col) == False:
        print("Sorry that area has been filled in, please pick an empty spot on the board.\n")
        return getInput(mode, turn)

    return row, col

#Gets the row and col for the AI by calling the minimax algorithim
def getAI(turn):
    global board
    bestMove = -1000
    nextMove = (-1, -1)
    for row in range(0,3):
        for col in range(0,3):
            if checkBoard(row, col) == True:
                board[row][col] = "O"
                move = miniMax(board, 0, turn)
                board[row][col] = " "

                if move > bestMove:
                    bestMove = move
                    nextMove = (row, col)


    return nextMove

#Minimax algorithim for picking AI move via recursion
def miniMax(board, depth, isMax):

    #Return values if game is in terminal state
    if gameOver(board) and isMax == True:
        return -10
    if gameOver(board) and isMax == False:
        return 10
    if boardFull(board) and not gameOver(board):
        return 0    

    #The maximizer picks the best move for the AI
    if isMax:
        bestScore = -1000
        for row in range(0,3):
            for col in range(0,3):
                if checkBoard(row, col) == True:
                    board[row][col] = "O"
                    score = miniMax(board, depth + 1, not isMax)
                    board[row][col] = " "

                    bestScore = max(bestScore, score)
        return bestScore 

    #The minimizer picks the best play for the human after each play by the AI
    else:
        bestScore = 1000
        for row in range(0,3):
            for col in range(0,3):
                if checkBoard(row, col) == True:
                    board[row][col] = "X"
                    score = miniMax(board, depth + 1, not isMax)
                    board[row][col] = " "

                    bestScore = min(bestScore, score)
        return bestScore


    

#Checks for board availability
def checkBoard(row, col):
    global board
    if board[row][col] != " ":
        return False
    return True

#Updates board with given coordinates
def updateBoard(row, col, turn, board):
    if turn == True:
        board[row][col] = "X"
    else:
        board[row][col] = "O"

#Updates turn to next player
def updateTurn(turn):
    if turn == True:
        turn = False
    else: 
        turn = True

    return turn

#Checks if the board is full
def boardFull(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                return False
    return True


#Checks if there is a winning sequence on the board
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

#Outputs terminal message for the end game
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

if mode == 3:
    quit()

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
turn = True

#Clear Terminal
clearScreen()

while not boardFull(board) and not gameOver(board):
    row, col = getInput(mode, turn)
    updateBoard(row, col, turn, board)
    turn = updateTurn(turn)

checkWinner(gameOver(board), turn)
        