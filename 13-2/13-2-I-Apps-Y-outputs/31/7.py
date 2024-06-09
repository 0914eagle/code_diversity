
def f1(N, K):
    # Initialize the probability of winning as 0
    prob = 0

    # Iterate over all possible values of the die
    for i in range(1, N+1):
        # Calculate the probability of getting a score of K or above with the current die value
        prob += (1/N) * (1/2)**(K-1)

    # Return the probability of winning
    return prob

