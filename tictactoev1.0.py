import random

c = "--------------+" # Makes up the grid (horizontal lines)

fieldchart = [[" "," "," "],[" "," "," "],[" "," "," "]] # Makes up the selection of where to set marks

def playerpick():
    """
    Asks the players for their nick (if left blank, the name defaults to Player (1/2)). Afterwards
    player 1 is asked to pick head or tails to decide on who starts.
    """
    global player1name
    global player2name
    player1name = input("How do you want to be called, Player 1? Leave blank for default name\n")
    if player1name == "":
        player1name = "Player 1"
    while True:
        player2name = input("How do you want to be called, Player 2? Leave blank for default name\n")
        if player2name == "":
            player2name = "Player 2"
            break
        elif player2name == player1name:
            print(f"Please select a different name than {player1name}")
            continue
        break
    global headortailswinner
    global headortailsloser
    while True: # Rolls a random number and decides on who is to put his mark first
        try:
            playervaluepick1 = int(input(f"{player1name}, pick head(1) oder tails(2) to decide on who starts first!\n"))
            headortails = int(random.uniform(1, 3))
            if playervaluepick1 == headortails:
                print(f"{player1name} won and is the first one to set a mark on the grid!\n")
                headortailswinner = player1name
                headortailsloser = player2name
                break
            elif playervaluepick1 > 2 or playervaluepick1 <= 0:
                print(f"{player1name}, please input a valid number (1 for head, 2 for tails)\n")
                continue
            elif playervaluepick1 != headortails:
                print(f"{player1name} lost, {player2name} is the first one to set a mark on the grid!\n")
                headortailswinner = player2name
                headortailsloser = player1name
                break
            else:
                print("Something went wrong... This shouldn't have happened. Please just restart the game.\n")
                input()
                quit()
        except:
            print("Please type 1 to pick head or 2 to pick tails.\n")
            continue
        break
    return headortailswinner, player1name, player2name, headortailsloser

def winner():
    """
    Decides on whether one of the players won or the game tied. If a winner is found
    the game ends, if the game results in a tie, the game ends as well.
    """
    global gameison
    gameison = True
    #gameison = True
    if fieldchart[0][0] != " ": #HORIZONTAL
        if fieldchart[0][0] == fieldchart[0][1] and fieldchart[0][0] == fieldchart[0][2]:
            gameison = False
            if fieldchart[0][0] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()
    if fieldchart[1][0] != " ": #HORIZONTAL
        if fieldchart[1][0] == fieldchart[1][1] and fieldchart[1][0] == fieldchart[1][2]:
            gameison = False
            if fieldchart[1][0] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()
    if fieldchart[2][0] != " ": #HORIZONTAL
        if fieldchart[2][0] == fieldchart[2][1] and fieldchart[2][0] == fieldchart[2][2]:
            gameison = False
            if fieldchart[2][0] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()
    if fieldchart[0][0] != " ": #VERTICAL
        if fieldchart[0][0] == fieldchart[1][0] and fieldchart[0][0] == fieldchart[2][0]:
            gameison = False
            if fieldchart[0][0] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()
    if fieldchart[0][1] != " ": #VERTICAL
        if fieldchart[0][1] == fieldchart[1][1] and fieldchart[0][1] == fieldchart[2][1]:
            gameison = False
            if fieldchart[0][1] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()
    if fieldchart[0][2] != " ": #VERTICAL
        if fieldchart[0][2] == fieldchart[1][2] and fieldchart[0][2] == fieldchart[2][2]:
            gameison = False
            if fieldchart[0][2] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()

    if fieldchart[0][0] != " ": #DIAGONAL1
        if fieldchart[0][0] == fieldchart[1][1] and fieldchart[0][0] == fieldchart[2][2]:
            gameison = False
            if fieldchart[0][0] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()
    if fieldchart[0][2] != " ": #DIAGONAL2
        if fieldchart[0][2] == fieldchart[1][1] and fieldchart[0][2] == fieldchart[2][0]:
            gameison = False
            if fieldchart[0][2] == "X":
                print(f"{player1name} won! GG!")
                input()
            else:
                print(f"{player2name} won! GG!")
                input()
        if fieldchart[0][0] == "X" or fieldchart[0][0] == "O":
            if fieldchart[0][1] != " " and fieldchart[0][2] != " " and fieldchart[1][0] != " " and fieldchart[1][1] != " " and fieldchart[1][2] != " " and fieldchart[2][0] != " " and fieldchart[2][1] != " " and fieldchart[2][2] != " ":
                gameison = False
                print("The game tied! Nobody won!")
                input()
    return gameison

def gamegrid(fieldchart):
    """
    Creates and prints the tictactoe grid based on the players inputs.
    """
    e = (f"\n|              |              |              |\n|              |              |              |\n|      {fieldchart[0][0]}       |      {fieldchart[0][1]}       |      {fieldchart[0][2]}       |\n|              |              |              |\n|              |              |              |\n|              |              |              |") # Makes up the grid (vertical lines)
    f = (f"\n|              |              |              |\n|              |              |              |\n|      {fieldchart[1][0]}       |      {fieldchart[1][1]}       |      {fieldchart[1][2]}       |\n|              |              |              |\n|              |              |              |\n|              |              |              |") # Makes up the grid (vertical lines)
    g = (f"\n|              |              |              |\n|              |              |              |\n|      {fieldchart[2][0]}       |      {fieldchart[2][1]}       |      {fieldchart[2][2]}       |\n|              |              |              |\n|              |              |              |\n|              |              |              |") # Makes up the grid (vertical lines)

    printgrid1 = ("+" + 3*c)
    printgrid2 = (e)
    printgrid3 = (f)
    printgrid4 = (g)
    printgridfinal = (f"{printgrid1}{printgrid2}\n{printgrid1}{printgrid3}\n{printgrid1}{printgrid4}\n{printgrid1}\n")

    print(f"{printgridfinal} The grid is ready.\n")

def winnerfieldselect(headortailswinner, headortailsloser):
    """
    The field select system itself. Lets the player decide on what field he wants to pick
    and then checks whether the field is free or not. The whosturn variable decides on whos next
    to place his mark. This function is looped until a winner has been found or the game tied.
    """
    while gameison == True:
        if player1name == whosturn:
            try:
                player1select = int(input(f"It's {player1name}'s turn! Please select a field to place your mark in (e.g. 1 for the top left field, 7 for the bottom left field\n)"))
                if player1select >= 1 and player1select <= 3:
                    if fieldchart[0][player1select-1] == " ":
                        fieldchart[0][player1select-1] = "X"
                    else:
                        print("Please select a free field.")
                        continue
                elif player1select >= 4 and player1select <= 6:
                    if fieldchart[1][player1select-4] == " ":
                        fieldchart[1][player1select-4] = "X"
                    else:
                        print("Please select a free field.")
                        continue
                elif player1select >= 7 and player1select <= 9:
                    if fieldchart[2][player1select-7] == " ":
                        fieldchart[2][player1select-7] = "X"
                    else:
                        print("Please select a free field.")
                        continue
                else:
                    print("Please enter a valid field number (1-9)")
                    continue
            except:
                print("Please enter a valid field number (1-9)")
                continue
        elif player2name == whosturn:
            try:
                player2select = int(input(f"It's {player2name}'s turn! Please select a field to place your mark in (e.g. 1 for the top left field, 7 for the bottom left field\n)"))
                if player2select >= 1 and player2select <= 3:
                    if fieldchart[0][player2select-1] == " ":
                        fieldchart[0][player2select-1] = "O"
                    else:
                        print("Please select a free field.")
                        continue
                elif player2select >= 4 and player2select <= 6:
                    if fieldchart[1][player2select-4] == " ":
                        fieldchart[1][player2select-4] = "O"
                    else:
                        print("Please select a free field.")
                        continue
                elif player2select >= 7 and player2select <= 9:
                    if fieldchart[2][player2select-7] == " ":
                        fieldchart[2][player2select-7] = "O"
                    else:
                        print("Please select a free field.")
                        continue
                else:
                    print("Please enter a valid field number (1-9)")
                    continue
            except:
                print("Please enter a valid field number (1-9)")
                continue
        break

def maingame():
    """
    prints the welcome screen, afterwards only runs the functions (which are
    looped until one person wins or the game ties)
    """
    print("\nWelcome to\n")
    print("""
  _______     ______          ______
 /_  __(_)___/_  __/___ _____/_  __/___  ___
  / / / / ___// / / __ `/ ___// / / __ \/ _ |
 / / / / /__ / / / /_/ / /__ / / / /_/ /  __/
/_/ /_/\___//_/  \__,_/\___//_/  \____/\___/  Version 1.0\n

By ᴋᴇʟʟᴇᴋᴇʀᴇʟʟ 2020\n
Press Enter to continue!\n
""")
    input()
    playerpick()
    gamegrid(fieldchart)
    global whosturn
    while gameison == True:
        whosturn = headortailswinner
        winnerfieldselect(headortailswinner, headortailsloser)
        gamegrid(fieldchart)
        winner()
        while gameison == True:
            whosturn = headortailsloser
            winnerfieldselect(headortailswinner, headortailsloser)
            gamegrid(fieldchart)
            winner()
            break
        continue

        input()

winner()
maingame() # The game itself lul
