
def solve(N, K, A, F):
    # Initialize the minimum score to a large value
    min_score = float('inf')
    
    # Loop through all possible combinations of training sets
    for i in range(1 << N):
        # Convert the binary representation of i to a list of booleans
        training_sets = [bool(i & (1 << j)) for j in range(N)]
        
        # Calculate the total number of training sets used
        total_training_sets = sum(training_sets)
        
        # Check if the total number of training sets used is less than or equal to K
        if total_training_sets <= K:
            # Initialize the score to 0
            score = 0
            
            # Loop through all foods
            for j in range(N):
                # Calculate the time it takes for the member to finish the food
                time = A[j] - training_sets[j] * 1
                
                # Check if the time is negative
                if time < 0:
                    # Set the time to 0
                    time = 0
                
                # Add the time to the score
                score += time * F[j]
                
            # Check if the score is less than the minimum score
            if score < min_score:
                # Update the minimum score
                min_score = score
    
    # Return the minimum score
    return min_score

