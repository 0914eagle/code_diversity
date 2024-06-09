
def f1(N, K):
    # Initialize the probability of winning
    prob_win = 0

    # Iterate over all possible values of the die
    for i in range(1, N+1):
        # Calculate the probability of getting a score of K or above with the current die value
        prob_score_K_above = (i / N) * (1 / 2) ** (K-1)

        # Add the probability of winning to the total probability
        prob_win += prob_score_K_above

    # Return the probability of winning
    return prob_win

