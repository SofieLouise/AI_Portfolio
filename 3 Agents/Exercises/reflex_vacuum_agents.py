A = 'A'
B = 'B'

Environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}


# Uses condition-action rules instead of tables
def REFLEX_VACUUM_AGENT(loc_st):  # Determine action
    if loc_st[1] == 'Dirty':
        return 'Suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Left'


def Sensors():  # Sense Environment (location of agent, status of square)
    location = Environment['Current']
    return (location, Environment[location])


def Actuators(action):  # Modify Environment
    location = Environment['Current']
    if action == 'Suck':
        Environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        Environment['Current'] = B
    elif action == 'Left' and location == B:
        Environment['Current'] = A


def run(n, make_agent):  # run the agent through n steps
    print(' Current New')
    print(' location status action location status')
    for i in range(1, n):
        (location, status) = Sensors()  # Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end='')
        action = make_agent(Sensors())
        Actuators(action)
        (location, status) = Sensors()  # Sense Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


if __name__ == '__main__':
    run(20, REFLEX_VACUUM_AGENT)

    # Output
    # Current New
    # location    status  action  location    status
    # A           Dirty   Suck    A           Clean
    # A           Clean   Right   B           Dirty
    # B           Dirty   Suck    B           Clean
    # B           Clean   Left    A           Clean
    # A           Clean   Right   B           Clean
    # B           Clean   Left    A           Clean
    # A           Clean   Right   B           Clean
    # B           Clean   Left    A           Clean
    # A           Clean   Right   B           Clean
