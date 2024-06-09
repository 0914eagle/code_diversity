
def get_largest_sum(a, b, c, k):
    # Initialize a list to store the numbers
    numbers = [a, b, c]
    
    # Loop through the operations
    for i in range(k):
        # Find the largest number in the list
        largest = max(numbers)
        # Double the largest number
        largest *= 2
        # Replace the largest number with the new value
        numbers[numbers.index(largest)] = largest
    
    # Return the sum of the numbers
    return sum(numbers)

