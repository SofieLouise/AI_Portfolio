import numpy as np

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.
The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a describtion of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 1, 3],
        # [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        # [None, 3, 3, 1, 1, 2, 3, 3, 1, 2],
    ]

    # Markov transition matrix
    # transitions[start, end]
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q), probability of number of ice creams v given observation q (hot, cold)
    # emission[state, observation]
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(path)))

        print('')


def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    T = len(observations)
    N = states.size
    forward = np.zeros((N, T))
    for s in range(1, N):
        # transitions, the probability of going from init to the different states
        # emission, the probability that we get the first observation given the current state
        forward[s][1] = transitions[0][s] * emissions[s][observations[1]]

    for t in range(2, T):
        for s in range(1, N):
            # The point here is that for each state, each previous state's probability is calculated,
            # multiplied by the probability of going from the previous state to the one we are in,
            # multiplied by the probability that there is x number of ice in the given state
            # In the end, we summarize all the previous ones that were there.
            # Therefore, we make a sum variable and loop through and add to it
            sum = 0
            for ss in range(1, N):
                sum += forward[ss][t - 1] * transitions[ss][s] * emissions[s][observations[t]]
            forward[s][t] = sum

    finalsum = 0
    for s in range(1, N):
        finalsum += forward[s][T - 1] * transitions[s][N - 1]
    forward[N - 1][T - 1] = finalsum
    return forward[N - 1][T - 1]


def compute_viterbi(states, observations, transitions, emissions):
    # On the contrary, Viterbi calculates the highest of its predecessor,
    # multiplied by the probability of transition,
    # multiplied by the probability of the amount of ice given the temperature.
    T = len(observations)
    N = states.size

    viterbi = np.zeros((N, T))
    backpointer = np.zeros((N, T), dtype=int)

    for s in range(1, N):
        viterbi[s][1] = transitions[0][s] * emissions[s][observations[1]]
        backpointer[s][1] = 0

    for t in range(2, T):
        for s in range(1, N - 1):
            probabilities_list = []
            backpointer_list = N * [0]
            # For each day t, we loop through every state s and every predecessor ss.
            # Times the predecessor's probability with transition to s,
            # and times the probability of the amount of ice given the state.
            for ss in range(1, N):
                probabilities_list.append(viterbi[ss][t - 1] * transitions[ss][s] * emissions[s][observations[1]])
                # The backpointer is calculated by multiplying the predecessor's probability with transition to s
                backpointer_list[ss] = viterbi[ss][t - 1] * transitions[ss][s]
            # we store the maximum value calculated for the loop above in our viterbi matrix
            viterbi[s][t] = max(probabilities_list)
            # we store the index of the highest backpointer
            backpointer[s][t] = argmax(backpointer_list)
    final_list = []
    final_backpointer_list = N * [0]
    for s in range(1, N):
        final_list.append(viterbi[s, T - 1] * transitions[s][N - 1])
        final_backpointer_list[s] = viterbi[s, T - 1] * transitions[s][N - 1]
    viterbi[N - 1][T - 1] = max(final_list)
    backpointer[N - 1][T - 1] = argmax(final_backpointer_list)

    # returns best path from end to start: [hot, hot, hot] ex.
    # N states.size
    # T len(observations)
    path = T * [0]
    path[0] = backpointer[N - 1][T - 1]
    for t in range(1, T):
        path[t] = backpointer[path[t - 1]][T - t]

    path.reverse()
    state_path = []
    for state_index in path:
        state_path.append(states[state_index])
    return state_path


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))
    return max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
