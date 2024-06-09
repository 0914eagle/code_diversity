
def get_max_sum(B):
    
    # Initialize the maximum sum and the current sum
    max_sum = 0
    current_sum = 0
    
    # Iterate through the elements of B
    for i in range(len(B)):
        # Add the current element to the current sum
        current_sum += B[i]
        
        # If the current sum is greater than the maximum sum, update the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
        
        # If the current element is greater than the next element, subtract the next element from the current sum
        if i < len(B) - 1 and B[i] > B[i+1]:
            current_sum -= B[i+1]
    
    # Return the maximum sum
    return max_sum

