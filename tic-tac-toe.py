board = ["-"] * 9
xMoves = []
oMoves = []
turnTracker = "X"  # whose turn it is
winConditions = [
    # horizontal
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    # vertical
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    # diagonal
    (0, 4, 8),
    (2, 4, 6),
]


def printBoard():
    for x in range(3):
        print(board[3 * x], "|", board[3 * x + 1], "|", board[3 * x + 2])


def makeMove():
    printBoard()
    move = int(input(turnTracker + " to move: "))
    print()

    # register move to the board
    if board[move] == "-" and move in range(8):
        board[move] = turnTracker
        return move
    else:
        print("Illegal move. Try again.")
        makeMove()


def registerMove(move):
    if turnTracker == "X":
        xMoves.append(move)
    else:
        oMoves.append(move)


def checkForWinstate():
    for condition in winConditions:
        if all(pos in xMoves for pos in condition):
            printBoard()
            print("X wins!")
            exit()
        elif all(pos in oMoves for pos in condition):
            printBoard()
            print("o wins!")
            exit()


def changeTurn(turnTracker):
    if turnTracker == "X":
        return "O"
    else:
        return "X"


# gameplay loop
while True:
    # one of the players is prompted to make a move
    move = makeMove()

    # register move to individual move list
    registerMove(move)

    # check if there is a win on the board
    checkForWinstate()

    # switch whose move it is
    turnTracker = changeTurn(turnTracker)
