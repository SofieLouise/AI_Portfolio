A = 'A'
B = 'B'

percepts = []
# The table matches the percept sequences with an action
table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Dirty'),): 'Suck',
    ((B, 'Clean'),): 'Left',
    ((B, 'Dirty'),): 'Suck',
    ((A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',
    # ....
    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, 'Clean'), (A, 'Dirty'), (B, 'Clean')): 'Left',
    # ....
}


def LOOKUP(percepts, table): # Lookup appropriate action for percepts
    action = table.get(tuple(percepts))
    return action


def TABLE_DRIVEN_AGENT(percept): # Determine action based on table and percepts
    percepts.append(percept) # Add percept
    action = LOOKUP(percepts, table) # Lookup appropriate action for percepts
    return action


def run():  # run agent on several sequential percepts
    print('Action\tPercepts' )
    print(TABLE_DRIVEN_AGENT((A, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((A, 'Dirty')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)
    print(TABLE_DRIVEN_AGENT((B, 'Clean')), '\t', percepts)

    # Output:
    # Action	Percepts
    # Right 	[('A', 'Clean')]
    # Suck 	    [('A', 'Clean'), ('A', 'Dirty')]
    # Left 	    [('A', 'Clean'), ('A', 'Dirty'), ('B', 'Clean')]
    # None 	    [('A', 'Clean'), ('A', 'Dirty'), ('B', 'Clean'), ('B', 'Clean')]
    # The last is None because we have no entry for the history in the table

run()
