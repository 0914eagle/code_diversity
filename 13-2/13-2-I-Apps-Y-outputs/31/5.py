
def f1(N, K):
    # Initialize the probability of winning as 0
    prob = 0

    # Iterate over all possible values that the die can show
    for i in range(1, N+1):
        # Calculate the probability of getting a score of K or above with the current die value
        prob_score_k_or_above = (i / N) * (1 / 2)**(K-1)

        # Add the probability to the total probability of winning
        prob += prob_score_k_or_above

    # Return the probability of winning
    return prob

