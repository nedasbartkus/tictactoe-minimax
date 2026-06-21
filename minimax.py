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


global counter
counter = 0


# initialize subsequent gamestates
def initializeChildNodes(rootState):
    global counter
    if not rootState.openMoves:
        return

    for move in rootState.openMoves:
        counter += 1
        passOpenMoves = rootState.openMoves.copy()
        passxPlayed = rootState.xPlayed.copy()
        passoPlayed = rootState.oPlayed.copy()
        passNextToMove = None

        passOpenMoves.remove(move)

        if rootState.nextToMove == "X":
            passxPlayed.append(move)
            passNextToMove = "O"
        else:
            passoPlayed.append(move)
            passNextToMove = "X"

        rootState.children.append(
            GameState(
                rootState,
                [],
                None,
                passOpenMoves,
                passxPlayed,
                passoPlayed,
                passNextToMove,
            )
        )

    for child in rootState.children:
        initializeChildNodes(child)


# def calculateUtilityValue(rootState):


print(
    initializeChildNodes(
        GameState(None, [], None, [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [], "X")
    )
)

print(counter)


# def minimax(legalMoves, GameState):
#     childUtilityValues = []
#     for child in GameState.getAllChildren():
#         childUtilityValues.append(minimax(GameState.children[child]))
