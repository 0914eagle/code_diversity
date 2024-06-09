
def get_maximum_sum(A, B, C, K):
    # Initialize the maximum sum to 0
    max_sum = 0
    
    # Loop through all possible combinations of cards
    for i in range(0, K + 1):
        for j in range(0, min(K - i, B)):
            for k in range(0, min(K - i - j, C)):
                # Calculate the sum of the current combination
                current_sum = i * 1 + j * 0 + k * -1
                
                # Update the maximum sum if necessary
                if current_sum > max_sum:
                    max_sum = current_sum
    
    # Return the maximum sum
    return max_sum

