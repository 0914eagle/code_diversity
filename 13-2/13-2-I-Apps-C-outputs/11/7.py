
def get_max_or(numbers, k, x):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize the result
    result = 0
    
    # Loop through the numbers
    for i in range(len(numbers)):
        # Check if we can perform an operation
        if k > 0:
            # Multiply the current number by x
            numbers[i] *= x
            # Decrement the number of operations
            k -= 1
        # Update the result
        result |= numbers[i]
    
    # Return the result
    return result

