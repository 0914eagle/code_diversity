
def get_largest_sum(a, b, c, k):
    # Initialize a list to store the values of a, b, and c
    numbers = [a, b, c]
    
    # Loop through the list of numbers k times
    for _ in range(k):
        # Find the index of the largest number in the list
        largest_index = numbers.index(max(numbers))
        # Double the largest number
        numbers[largest_index] *= 2
    
    # Return the sum of the numbers
    return sum(numbers)

