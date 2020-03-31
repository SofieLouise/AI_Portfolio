import itertools

def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    :param state: State of the piles.
    :return: True if the state is a win.
    """
    return any(pile <= 2 for pile in state)

def utility_of(state):
    """
    This method assumes that min starts
    :param state: State of the piles.
    :return: +1 if winner is (MAX player), -1 if winner is (MIN player), or 0 otherwise
    """
    utility = 0
    if is_terminal(state):
        number_of_piles = len(state)
        if number_of_piles % 2 == 0:
            utility = -1
        else:
            utility = 1
    return utility


def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]


def successors_of(state):
    """
    :param state: State of the piles. Ex: [3,4]
    :return: a list of possible successor states as tuples (move, state)
    """
    successors = []
    i = 0
    for pile in state:
        state_copy = list.copy(state)
        changed_pile = state_copy[state.index(pile)]
        state_copy.remove(changed_pile)
        for partition in partitions(pile, 2):
            if all(pile > 0 for pile in partition) and all(partition.count(pile) <= 1 for pile in partition):
                state_copy.extend(partition)
                successors.append(tuple((i, state_copy)))
                i += 1
    return successors


def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = minmax_decision(state)
    return new_state


def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [7]

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            # TODO returns action instead of state
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))


if __name__ == '__main__':
    main()
