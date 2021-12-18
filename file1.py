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

print("Welcome to Tic Tac Toe!\n")
mode = gameMode()

if mode == 1:
    print("Singleplayer")

elif mode == 2:
    print("Multiplayer")

else:
    quit()