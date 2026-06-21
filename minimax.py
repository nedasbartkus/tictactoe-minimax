# minimax algorithm
# current state
# all next states
# continue computing all next states until terminal state is reached
# assign value to each terminal state
#
# then its just minimax algorithm as i know it:
# for max: choose path w/ higher number
# for min: choose path w/ lower number
# what heuristic? try: how many possible wins does this route have?


class GameState:  # tree node
    def __init__(
        self, parent, children, utilityValue, openMoves, xPlayed, oPlayed, nextToMove
    ):
        self.parent = parent
        self.children = children
        self.utilityValue = utilityValue
        self.openMoves = openMoves
        self.xPlayed = xPlayed
        self.oPlayed = oPlayed
        self.nextToMove = nextToMove

    def getAllChildren(self, children):
        allChildren = []
        for child in children:
            allChildren.append(child)
        return allChildren

    def changeTurn(self, nextToMove):
        if nextToMove == "X":
            nextToMove = "O"
        else:
            nextToMove = "X"


# initialize all nodes (generate gamestates)
def initializeTree(rootState):
    if not rootState.openMoves:
        return

    tempOpenMoves = rootState.openMoves.copy()
    tempxPlayed = rootState.xPlayed.copy()
    tempoPlayed = rootState.oPlayed.copy()

    if rootState.nextToMove == "X":
        # make a quick copy of the list WITHIN the for loop definition (sneaky sneaky)
        for move in list(rootState.openMoves):
            print("open moves: ", rootState.openMoves)
            print()
            print("move: ", move)

            passxPlayed = tempxPlayed
            passOpenMoves = tempOpenMoves

            passxPlayed.append(move)
            passOpenMoves.remove(move)

            rootState.xPlayed.append(move)
            rootState.openMoves.remove(move)
            rootState.children.append(
                GameState(
                    rootState,
                    None,
                    None,
                    passOpenMoves,
                    rootState.xPlayed,
                    rootState.oPlayed,
                    "O",
                )
            )
    else:
        for move in list(rootState.openMoves):
            print("open moves: ", rootState.openMoves)
            print()
            print("move: ", move)

            passoPlayed = tempoPlayed
            passOpenMoves = tempOpenMoves

            passoPlayed.append(move)
            passOpenMoves.remove(move)

            rootState.oPlayed.append(move)
            rootState.openMoves.remove(move)
            rootState.children.append(
                GameState(
                    rootState,
                    None,
                    None,
                    rootState.openMoves,
                    rootState.xPlayed,
                    rootState.oPlayed,
                    "O",
                )
            )


print(
    initializeTree(GameState(None, [], None, [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [], "X"))
)
# def minimax(legalMoves, GameState):
#     childUtilityValues = []
#     for child in GameState.getAllChildren():
#         childUtilityValues.append(minimax(GameState.children[child]))
