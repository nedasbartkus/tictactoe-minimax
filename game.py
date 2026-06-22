import minimax

board = ["-"] * 9
xMoves = []
oMoves = []
legalMoves = {0, 1, 2, 3, 4, 5, 6, 7, 8}
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
    if move in legalMoves:
        board[move] = turnTracker
        legalMoves.remove(move)
        return move
    else:
        print("Illegal move. Try again.")
        makeMove()


def botMove(rootNode):
    # printBoard()
    move = minimax.chooseMove(rootNode)
    print()

    board[move] = turnTracker
    legalMoves.remove(move)
    return move


def registerMove(move):
    if turnTracker == "X":
        xMoves.append(move)
    else:
        oMoves.append(move)


def checkForWinstate():
    if not legalMoves:
        printBoard()
        print("Draw...")
        exit()

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


# minimax.rootNode = minimax.GameState(
#     None, [], 0, [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [], "X", None
# )
rootNode = minimax.rootNode

# gameplay loop
while True:
    # player move
    move = makeMove()

    registerMove(move)

    checkForWinstate()

    turnTracker = changeTurn(turnTracker)

    # now its minimax time B)
    for child in rootNode.children:
        if child.lastMove == move:
            rootNode = child

    move = botMove(rootNode)

    registerMove(move)

    checkForWinstate()

    turnTracker = changeTurn(turnTracker)

    for child in rootNode.children:
        if child.lastMove == move:
            rootNode = child
