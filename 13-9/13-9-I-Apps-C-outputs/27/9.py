
import math

def solve(n, m, likes, weights):
    # Calculate the sum of all weights
    total_weight = sum(weights)
    
    # Initialize the expected weights
    expected_weights = [0] * n
    
    # Iterate through each visit
    for i in range(m):
        # Choose a picture randomly with a probability proportional to its weight
        picture_index = random.choices(population=range(n), weights=weights, k=1)[0]
        
        # If the picture is liked, add 1 to its weight
        if likes[picture_index] == 1:
            weights[picture_index] += 1
        # Otherwise, subtract 1 from its weight
        else:
            weights[picture_index] -= 1
        
        # Calculate the expected weight of the picture
        expected_weights[picture_index] = (expected_weights[picture_index] * i + weights[picture_index]) / (i + 1)
    
    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

