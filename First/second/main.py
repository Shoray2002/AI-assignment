import argparse
import timeit

# use command line arguments to read in the initial state
# TEST CASE: python main.py 3,1,4,2,0,6,7,8,5


class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

    def __str__(self):
        return str(self.map)


GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
GoalNode = None
NodesExpanded = 0


def dfs(startState):
    global GoalNode
    boardVisited = set()
    stack = list([PuzzleState(startState, None, None, 0, 0, 0)])
    while stack:
        node = stack.pop()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return stack
        posiblePaths = reversed(subNodes(node))
        for path in posiblePaths:
            if path.map not in boardVisited:
                stack.append(path)
                boardVisited.add(path.map)


def subNodes(node):
    global NodesExpanded
    NodesExpanded = NodesExpanded+1
    nextPaths = []
    nextPaths.append(PuzzleState(move(node.state, 1), node,
                     1, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 2), node,
                     2, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 3), node,
                     3, node.depth + 1, node.cost + 1, 0))
    nextPaths.append(PuzzleState(move(node.state, 4), node,
                     4, node.depth + 1, node.cost + 1, 0))
    nodes = []
    for procPaths in nextPaths:
        if(procPaths.state != None):
            nodes.append(procPaths)
    return nodes


def move(state, direction):
    newState = state[:]
    index = newState.index(0)

    if(index == 0):
        if(direction == 1):
            return None
        if(direction == 2):
            temp = newState[0]
            newState[0] = newState[3]
            newState[3] = temp
        if(direction == 3):
            return None
        if(direction == 4):
            temp = newState[0]
            newState[0] = newState[1]
            newState[1] = temp
        return newState
    if(index == 1):
        if(direction == 1):
            return None
        if(direction == 2):
            temp = newState[1]
            newState[1] = newState[4]
            newState[4] = temp
        if(direction == 3):
            temp = newState[1]
            newState[1] = newState[0]
            newState[0] = temp
        if(direction == 4):
            temp = newState[1]
            newState[1] = newState[2]
            newState[2] = temp
        return newState
    if(index == 2):
        if(direction == 1):
            return None
        if(direction == 2):
            temp = newState[2]
            newState[2] = newState[5]
            newState[5] = temp
        if(direction == 3):
            temp = newState[2]
            newState[2] = newState[1]
            newState[1] = temp
        if(direction == 4):
            return None
        return newState
    if(index == 3):
        if(direction == 1):
            temp = newState[3]
            newState[3] = newState[0]
            newState[0] = temp
        if(direction == 2):
            temp = newState[3]
            newState[3] = newState[6]
            newState[6] = temp
        if(direction == 3):
            return None
        if(direction == 4):
            temp = newState[3]
            newState[3] = newState[4]
            newState[4] = temp
        return newState
    if(index == 4):
        if(direction == 1):
            temp = newState[4]
            newState[4] = newState[1]
            newState[1] = temp
        if(direction == 2):
            temp = newState[4]
            newState[4] = newState[7]
            newState[7] = temp
        if(direction == 3):
            temp = newState[4]
            newState[4] = newState[3]
            newState[3] = temp
        if(direction == 4):
            temp = newState[4]
            newState[4] = newState[5]
            newState[5] = temp
        return newState
    if(index == 5):
        if(direction == 1):
            temp = newState[5]
            newState[5] = newState[2]
            newState[2] = temp
        if(direction == 2):
            temp = newState[5]
            newState[5] = newState[8]
            newState[8] = temp
        if(direction == 3):
            temp = newState[5]
            newState[5] = newState[4]
            newState[4] = temp
        if(direction == 4):
            return None
        return newState
    if(index == 6):
        if(direction == 1):
            temp = newState[6]
            newState[6] = newState[3]
            newState[3] = temp
        if(direction == 2):
            return None
        if(direction == 3):
            return None
        if(direction == 4):
            temp = newState[6]
            newState[6] = newState[7]
            newState[7] = temp
        return newState
    if(index == 7):
        if(direction == 1):
            temp = newState[7]
            newState[7] = newState[4]
            newState[4] = temp
        if(direction == 2):
            return None
        if(direction == 3):
            temp = newState[7]
            newState[7] = newState[6]
            newState[6] = temp
        if(direction == 4):
            temp = newState[7]
            newState[7] = newState[8]
            newState[8] = temp
        return newState
    if(index == 8):
        if(direction == 1):
            temp = newState[8]
            newState[8] = newState[5]
            newState[5] = temp
        if(direction == 2):
            return None
        if(direction == 3):
            temp = newState[8]
            newState[8] = newState[7]
            newState[7] = temp
        if(direction == 4):
            return None
        return newState


def main():

    global GoalNode

    parser = argparse.ArgumentParser()
    parser.add_argument('initialBoard')
    args = parser.parse_args()
    data = args.initialBoard.split(",")
    InitialState = []
    InitialState.append(int(data[0]))
    InitialState.append(int(data[1]))
    InitialState.append(int(data[2]))
    InitialState.append(int(data[3]))
    InitialState.append(int(data[4]))
    InitialState.append(int(data[5]))
    InitialState.append(int(data[6]))
    InitialState.append(int(data[7]))
    InitialState.append(int(data[8]))
    start = timeit.default_timer()
    dfs(InitialState)
    stop = timeit.default_timer()
    time = stop-start
    deep = GoalNode.depth
    moves = []
    while InitialState != GoalNode.state:
        if GoalNode.move == 1:
            path = 'Up'
        if GoalNode.move == 2:
            path = 'Down'
        if GoalNode.move == 3:
            path = 'Left'
        if GoalNode.move == 4:
            path = 'Right'
        moves.append(path)
        GoalNode = GoalNode.parent
        print(GoalNode.state)

    print("COST: ", len(moves))
    print("NODES CREATED: ", str(NodesExpanded))
    print("DEPTH: ", str(deep))
    print("RUNTIME: ", format(time, '.8f'))

    file = open('output.txt', 'w')
    file.write("PATH: " + str(moves) + "\n")
    file.write("COST: " + str(len(moves)) + "\n")
    file.write("NODES CREATED: " + str(NodesExpanded) + "\n")
    file.write("DEPTH: " + str(deep) + "\n")
    file.write("RUNTIME: " + format(time, '.8f') + "\n")
    file.close()


if __name__ == '__main__':
    main()
