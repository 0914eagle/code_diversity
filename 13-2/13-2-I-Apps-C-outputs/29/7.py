
def get_winner_probability(N, M, p_list):
    # Initialize the probability of Anthony winning as 0
    probability = 0

    # Loop through each round
    for i in range(N + M - 1):
        # Calculate the probability of Anthony winning the current round
        win_probability = p_list[i]

        # If Anthony wins the current round, he will have N - 1 points left
        # and Cora will have M - 1 points left
        if i < N - 1:
            N = N - 1
        else:
            M = M - 1

        # Calculate the probability of Anthony winning the next round
        if N == 0 or M == 0:
            # If one of them has no points left, the game is over and Anthony wins
            probability = 1
            break
        else:
            # If neither of them has no points left, calculate the probability of Anthony winning the next round
            probability += win_probability * (N / (N + M))

    return probability

