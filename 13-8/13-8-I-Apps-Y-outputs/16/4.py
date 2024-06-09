
def solve(N, K):
    # Initialize the probability to 0
    probability = 0
    
    # Iterate over all possible values of the die
    for i in range(1, N+1):
        # Calculate the probability of getting a score of i
        p = 1 / N
        
        # If the score is between 1 and K-1, inclusive, we need to consider the probability of getting consecutive heads
        if i >= 1 and i < K:
            # Calculate the number of consecutive heads needed to get a score of K or above
            num_consecutive_heads = K - i
            
            # Calculate the probability of getting consecutive heads
            p *= (1/2)**num_consecutive_heads
        
        # Add the probability to the total probability
        probability += p
    
    # Return the probability that Snuke wins
    return probability

