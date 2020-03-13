"""
A* Search, Vacuum Problem
"""


class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''


def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_LOWEST_PATH_PLUS_HEURISTIC(fringe)
        if node.STATE[1] == GOAL_HEURISTIC:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''


def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''


def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''


def INSERT_ALL(list, queue):
    return list + queue


'''
Removes and returns the first element from fringe
'''


def calculatePathCost(path):
    cost = 0
    for i in range(len(path)):
        # ('A','B')
        if i < len(path) - 1:
            cost += COST_SPACE.get((path[i + 1].STATE[0], path[i].STATE[0]))
    return cost


def REMOVE_LOWEST_PATH_PLUS_HEURISTIC(queue):
    lowest = queue[0]
    lowest_f = lowest.STATE[1] + calculatePathCost(lowest.path())
    for node in queue:
        path_cost = calculatePathCost(node.path())
        f = node.STATE[1] + path_cost
        if f <= lowest_f:
            lowest = node
            lowest_f = f
    queue.remove(lowest)
    return lowest


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = (('A', 'Dirty', 'Dirty'), 3)
GOAL_HEURISTIC = 0
STATE_SPACE = {INITIAL_STATE:                   [(('B', 'Dirty', 'Dirty'), 3), (('A', 'Clean', 'Dirty'), 2)],
               (('B', 'Dirty', 'Dirty'), 3):    [(('A', 'Dirty', 'Dirty'), 3), (('B', 'Dirty', 'Clean'), 2)],
               (('A', 'Clean', 'Dirty'), 2):    [(('B', 'Clean', 'Dirty'), 1)],
               (('B', 'Dirty', 'Clean'), 2):    [(('A', 'Dirty', 'Clean'), 1)],
               (('A', 'Dirty', 'Clean'), 1):    [(('A', 'Clean', 'Clean'), 0), (('B', 'Dirty', 'Clean'), 1)],
               (('B', 'Clean', 'Dirty'), 1):    [(('A', 'Clean', 'Dirty'), 2), (('B', 'Clean', 'Clean'), 0)],
               (('A', 'Clean', 'Clean'), 0): [],
               (('B', 'Clean', 'Clean'), 0): []}

COST_SPACE = {
    ('A', 'B'): 1,
    ('A', 'C'): 2,
    ('A', 'D'): 4,
    ('B', 'F'): 5,
    ('B', 'E'): 4,
    ('C', 'E'): 1,
    ('D', 'H'): 1,
    ('D', 'I'): 2,
    ('D', 'J'): 2,
    ('F', 'G'): 1,
    ('E', 'H'): 3,
    ('E', 'G'): 2,
    ('I', 'L'): 3,
    ('H', 'L'): 5,
    ('H', 'K'): 6,
    ('G', 'K'): 6
}

'''
Run tree search and display the nodes in the path to goal node
'''


def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()