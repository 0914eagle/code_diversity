
def get_max_or_value(numbers, k, x):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize the result with the first number
    result = numbers[0]
    
    # Loop through the remaining numbers
    for i in range(1, len(numbers)):
        # Check if we can perform an operation
        if k > 0:
            # Multiply the current number by x and add it to the result
            result += numbers[i] * x
            # Decrement the number of operations
            k -= 1
        else:
            # Add the current number to the result
            result |= numbers[i]
    
    return result

