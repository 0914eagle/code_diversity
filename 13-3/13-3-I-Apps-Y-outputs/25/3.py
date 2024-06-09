
def f1(N, K):
    # Initialize the probability of winning
    prob_win = 0

    # Iterate over all possible values of the die
    for i in range(1, N+1):
        # Calculate the probability of getting a score of i
        prob_i = 1/N

        # Calculate the probability of getting K or more with score i
        if i >= K:
            prob_k_or_more = 1
        else:
            prob_k_or_more = 0

        # Calculate the probability of getting a score of i and then K or more
        prob_i_and_k_or_more = prob_i * prob_k_or_more

        # Add the probability of winning with score i to the total probability
        prob_win += prob_i_and_k_or_more

    # Return the probability of winning
    return prob_win

