board = ["-"] * 9
xMoves = []
oMoves = []
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


# print entire board
def printBoard():
    for x in range(3):
        print(board[3 * x], "|", board[3 * x + 1], "|", board[3 * x + 2])


# gameplay loop
turnTracker = "X"  # whose turn it is
while True:
    printBoard()

    move = int(input(turnTracker + " to move: "))
    print()

    # register move to the board and individual move list
    board[move] = turnTracker
    if turnTracker == "X":
        xMoves.append(move)
    else:
        oMoves.append(move)

    # check if there is a win on the board
    for condition in winConditions:
        if all(pos in xMoves for pos in condition):
            printBoard()
            print("X wins!")
            exit()
        elif all(pos in oMoves for pos in condition):
            printBoard()
            print("o wins!")
            exit()

    # switch whose move it is
    if turnTracker == "X":
        turnTracker = "O"
    else:
        turnTracker = "X"
