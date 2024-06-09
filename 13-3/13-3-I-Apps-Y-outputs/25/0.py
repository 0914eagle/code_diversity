
def f1(N, K):
    # Initialize the probability of winning
    prob_win = 0

    # Iterate over all possible values of the die
    for i in range(1, N+1):
        # Calculate the probability of getting i heads in a row
        prob_heads = (1/2)**i

        # Calculate the probability of winning with i heads in a row
        prob_win_i = prob_heads * (K/i)

        # Add the probability of winning with i heads in a row to the total probability
        prob_win += prob_win_i

    # Return the probability of winning
    return prob_win

