
def f1(N, K):
    # Initialize the probability of winning as 0
    probability = 0
    
    # Loop through each possible value that the die can show
    for i in range(1, N+1):
        # Calculate the probability of getting a score of K or above with the current die value
        probability += (1/N) * (1/2)**(K-1)
    
    # Return the probability of winning
    return probability

