import time

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


def checkForWinstate(moveList):
    for condition in winConditions:
        if all(pos in moveList for pos in condition):
            return True
    return False


class GameState:  # tree node
    def __init__(
        self,
        parent,
        children,
        utilityValue,
        openMoves,
        xPlayed,
        oPlayed,
        player,
        lastMove,
    ):
        self.parent = parent
        self.children = children
        self.utilityValue = utilityValue
        self.openMoves = openMoves
        self.xPlayed = xPlayed
        self.oPlayed = oPlayed
        self.player = player
        self.lastMove = lastMove

    def getAllChildren(self, children):
        allChildren = []
        for child in children:
            allChildren.append(child)
        return allChildren


# initialize all possible (and sometimes impossible) gamestates
# sum of all game states = sum(i = 0 to 9, (9! / (9-depth)!) )
def initializeGameTree(rootState):
    # global counter
    if not rootState.openMoves:
        return

    for move in rootState.openMoves:
        # counter += 1
        passOpenMoves = rootState.openMoves.copy()
        passxPlayed = rootState.xPlayed.copy()
        passoPlayed = rootState.oPlayed.copy()
        passPlayer = None

        passOpenMoves.remove(move)

        if rootState.player == "X":
            passxPlayed.append(move)
            passPlayer = "O"
        else:
            passoPlayed.append(move)
            passPlayer = "X"

        rootState.children.append(
            GameState(
                rootState,
                [],
                0,
                passOpenMoves,
                passxPlayed,
                passoPlayed,
                passPlayer,
                move,
            )
        )

    for child in rootState.children:
        initializeGameTree(child)


def calculateUtilityValues(currentNode):
    # check for winstate or draw
    if checkForWinstate(currentNode.xPlayed):
        currentNode.utilityValue = 1
        return 1  # 1 means the node is an x win
    elif checkForWinstate(currentNode.oPlayed):
        currentNode.utilityValue = -1
        return -1  # -1 means the node is an O win
    elif not currentNode.openMoves:
        currentNode.utilityValue = 0
        return 0  # 0 means draw

    childrenUtilityValues = []

    for child in currentNode.children:
        childrenUtilityValues.append(calculateUtilityValues(child))

    if currentNode.player == "X":
        xWants = max(childrenUtilityValues)
        currentNode.utilityValue = xWants
        return xWants
    elif currentNode.player == "O":
        oWants = min(childrenUtilityValues)
        currentNode.utilityValue = oWants
        return oWants


def chooseMove(currentNode):
    childrenUtilityValues = []
    maxUtility = None
    minUtility = None

    for child in currentNode.children:
        childrenUtilityValues.append(child.utilityValue)

    for child in currentNode.children:
        maxUtility = max(childrenUtilityValues)
        minUtility = min(childrenUtilityValues)

    if currentNode.player == "X":
        for child in currentNode.children:
            if child.utilityValue == maxUtility:
                return child.lastMove
    else:
        for child in currentNode.children:
            if child.utilityValue == minUtility:
                return child.lastMove
    return -1


rootNode = GameState(None, [], 0, [0, 1, 2, 3, 4, 5, 6, 7, 8], [], [], "X", None)


start_time = time.time()
initializeGameTree(rootNode)

print("--- %s seconds ---" % (time.time() - start_time))

calculateUtilityValues(rootNode)
