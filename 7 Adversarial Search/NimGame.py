def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
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
    return state


def alpha_beta_decision(state):
    infinity = float('inf')

    def max_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for successor in successors_of(state):
            v = max(v, min_value(successor, alpha, beta))
            if v >= beta:
                return v
            alpha = min(alpha, v)
        return v

    def min_value(state, alpha, beta):
        if is_terminal(state):
            return utility_of(state)
        v = infinity

        for successor in successors_of(state):
            v = min(v, max_value(successor, alpha, beta))
            if v <= alpha:
                return v
            beta = max(beta, v)
        return v

    state = argmax(successors_of(state), lambda a: min_value(a, infinity, -infinity))
    return state[1]


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    return True if len([s for s in state if s > 2]) == 0 else False


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    return 1 if len(state) % 2 == 0 else -1


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    result = []
    for i in state:
        j = 1
        k = i - 1
        count = 0
        while j < k:
            statecopy = [o for o in state]
            statecopy.remove(i)
            statecopy.extend([k, j])
            result.append((count, statecopy))
            j += 1
            count += 1
            k -= 1
    return result


def display(state):
    print("-----")
    print(state)


def main():
    board = [16]
    while not is_terminal(board):
        board = minmax_decision(board)
        if not is_terminal(board):
            display(board)
            valid = False
            while not valid:
                initial_pile = int(input('What pile would you like to split? '))
                pile_one = int(input('Select size of pile 1: '))
                pile_two = initial_pile - pile_one
                if initial_pile in board and pile_one != pile_two and pile_one != 0 and pile_two != 0:
                    valid = True
                    board.remove(initial_pile)
                    board.append(pile_one)
                    board.append(pile_two)
                else:
                    print('You entered a wrong input. Try again.')
                display(board)
    display(board)
    result = utility_of(board)
    if result == 1:
        print('Game over. Computer won.')
    elif result == -1:
        print('Congratulation. You won.')
    else:
        print('Game finished.')


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()