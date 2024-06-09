
def get_largest_sum(A, B, C, K):
    # Initialize a list to store the integers
    numbers = [A, B, C]
    
    # Loop through the operations
    for _ in range(K):
        # Find the largest number in the list
        largest = max(numbers)
        # Double the largest number
        largest *= 2
        # Replace the largest number with the doubled number
        numbers[numbers.index(largest)] = largest
    
    # Return the sum of the numbers
    return sum(numbers)

