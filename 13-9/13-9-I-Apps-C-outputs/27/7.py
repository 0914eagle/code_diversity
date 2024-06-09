
import math

def solve(n, m, likes, weights):
    # Calculate the sum of the weights
    total_weight = sum(weights)
    
    # Initialize the expected weights
    expected_weights = [0] * n
    
    # Iterate through each visit
    for i in range(m):
        # Calculate the probability of each picture being displayed
        probabilities = [weight / total_weight for weight in weights]
        
        # Choose a picture randomly based on the probabilities
        chosen_picture = np.random.choice(n, p=probabilities)
        
        # Update the weight of the chosen picture
        if likes[chosen_picture]:
            weights[chosen_picture] += 1
        else:
            weights[chosen_picture] -= 1
        
        # Calculate the new total weight
        total_weight = sum(weights)
    
    # Calculate the expected weight of each picture
    for i in range(n):
        expected_weights[i] = weights[i] / total_weight
    
    # Return the expected weights modulo 998244353
    return [int(998244353 * weight) for weight in expected_weights]

