
def solve(N, K):
    # Initialize the probability to 0
    probability = 0
    
    # Iterate over all possible values of the die
    for i in range(1, N+1):
        # Calculate the probability of getting a score of K or above on this turn
        probability_i = (i / N) * (0.5)**(K-1)
        
        # If the die shows i, Snuke needs to get (K-1) consecutive heads from (K-1) coin flips to obtain a score of K or above
        probability_i += (i / N) * (0.5)**(K-1)
        
        # Add the probability of winning to the total probability
        probability += probability_i
    
    # Return the probability that Snuke wins
    return probability

