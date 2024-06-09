
def get_maximum_happiness(N, V, C):
    # Initialize the maximum happiness value
    max_happiness = 0
    
    # Iterate over all possible combinations of ingredients
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j % N == 0:
                # Calculate the happiness value for this combination
                happiness = V[i] + V[j]
                
                # Calculate the cost of this combination
                cost = i ** 2 * C[i] + j ** 2 * C[j]
                
                # Check if the happiness value is greater than the maximum happiness value
                if happiness > max_happiness:
                    max_happiness = happiness
    
    # Return the maximum happiness value
    return max_happiness

