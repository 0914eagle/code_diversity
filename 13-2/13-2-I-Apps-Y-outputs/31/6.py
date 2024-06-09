
def f1(N, K):
    # Initialize the probability of winning as 0
    probability = 0
    
    # Iterate over all possible values that the die can show
    for i in range(1, N+1):
        # Calculate the probability of getting a score of K or above with the current die value
        probability_i = (i / N) * (0.5 ** (K-1))
        
        # Add the probability of winning with the current die value to the total probability
        probability += probability_i
    
    # Return the probability of winning
    return probability

