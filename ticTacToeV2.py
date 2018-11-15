from sys import exit
victory = False

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
            }


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def checkwin():
    if theBoard[top-L] == theBoard[top-M] == theBoard[top-R]:
        victory = True


def playTicTacToe():
    global victory
    turn = 'X'
#    winner = False
    while victory = False:
        printBoard(theBoard)

        legal = "unknown"

        while legal != "Y":

            move = input('\n Turn for ' + turn + '. Move on which space? > ')
            # Check if input is a key in the board, if not back to main loop
            if move not in theBoard:
                print("I don't understand that input.")
                break
            # Check if square is open, if not break back to main loop
            if theBoard[move] != " ":
                print("\nCannot move there.", theBoard[move], "is there.")
                legal = "N"
                break
            # If move legal update dict, change turn and break to main loop
            else:
                theBoard[move] = turn
                legal = "Y"
            if turn == 'X':
                checkwin(turn)
                turn = 'O'
                legal = "Y"
            else:
                checkwin(turn)
                turn = 'X'
                legal = "Y"

    printBoard(theBoard)


def checkwin(winner):

    def endgame():
        global victory
        print()
        print(winner, "wins!")
        print()
        victory = True

    if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] != ' ':
        endgame()

    if theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R'] != ' ':
        endgame()

    if theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] != ' ':
        endgame()

    if theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] != ' ':
        endgame()

    if theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] != ' ':
        endgame()

    if theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] != ' ':
        endgame()

    if theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] != ' ':
        endgame()

    if theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] != ' ':
        endgame()

    if ' ' not in theBoard.values():
        print("\nNobody wins. The game is a draw.")
        printBoard(theBoard)
        exit()


playTicTacToe()
