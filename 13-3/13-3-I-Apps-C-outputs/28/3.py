
def solve(n, m, a, w):
    # Calculate the sum of all weights
    total_weight = sum(w)
    
    # Initialize the expected weights
    expected_weights = [0] * n
    
    # Loop through each visit
    for i in range(m):
        # Calculate the probability of each picture being displayed
        probabilities = [wi / total_weight for wi in w]
        
        # Choose a picture randomly based on the probabilities
        picture_index = np.random.choice(n, p=probabilities)
        
        # If the picture is liked, increase its weight by 1
        if a[picture_index] == 1:
            w[picture_index] += 1
        # Otherwise, decrease its weight by 1
        else:
            w[picture_index] -= 1
        
        # Calculate the new expected weight for each picture
        for j in range(n):
            expected_weights[j] = (expected_weights[j] * i + w[j]) / (i + 1)
    
    # Return the expected weights modulo 998244353
    return [int(expected_weight % 998244353) for expected_weight in expected_weights]

