
def f1(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)
    
    # Initialize the expected weights
    expected_weights = [0] * n
    
    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on its weight
        picture_index = choose_picture(w)
        
        # Update the expected weight of the chosen picture
        expected_weights[picture_index] += 1
        
        # Update the weight of the chosen picture
        w[picture_index] += 1
    
    # Calculate the final expected weights
    final_expected_weights = [expected_weight * total_weight // sum(expected_weights) for expected_weight in expected_weights]
    
    # Return the final expected weights
    return final_expected_weights

def f2(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)
    
    # Initialize the expected weights
    expected_weights = [0] * n
    
    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on its weight
        picture_index = choose_picture(w)
        
        # Update the expected weight of the chosen picture
        expected_weights[picture_index] += 1
        
        # Update the weight of the chosen picture
        w[picture_index] += 1
    
    # Calculate the final expected weights
    final_expected_weights = [expected_weight * total_weight // sum(expected_weights) for expected_weight in expected_weights]
    
    # Return the final expected weights
    return final_expected_weights

def choose_picture(weights):
    # Calculate the cumulative weights
    cumulative_weights = [0] + list(np.cumsum(weights))
    
    # Choose a random number between 0 and the sum of all weights
    random_number = np.random.randint(0, sum(weights))
    
    # Find the index of the chosen picture
    for i in range(len(cumulative_weights)):
        if random_number < cumulative_weights[i]:
            return i - 1
    
    # If the random number is greater than the sum of all weights, return the last index
    return len(cumulative_weights) - 1

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    
    print(*f1(n, m, a, w), sep='\n')
    print(*f2(n, m, a, w), sep='\n')

