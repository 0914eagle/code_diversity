
def get_optimal_strategy(N, M):
    # Initialize a dictionary to store the probability of each number
    probabilities = {}
    
    # Loop through each number from 1 to M
    for i in range(1, M+1):
        # Calculate the probability of selecting number i
        probabilities[i] = (N-1) / (M*M)
    
    # Return the dictionary of probabilities
    return probabilities

