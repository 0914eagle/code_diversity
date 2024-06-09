
def f1(N, K):
    # Initialize the probability of winning as 0
    probability = 0
    
    # Iterate over all possible values of the die
    for i in range(1, N+1):
        # Calculate the probability of getting i on the die
        die_probability = 1 / N
        
        # Calculate the probability of getting K or above on the coin flip
        coin_probability = 0
        for j in range(i, K+1):
            if j % 2 == 0:
                coin_probability += (1 / 2) ** (j // 2)
            else:
                coin_probability += (1 / 2) ** ((j + 1) // 2)
        
        # Add the probability of winning for this value of the die
        probability += die_probability * coin_probability
    
    # Return the probability of winning
    return probability

